import streamlit as st
import pandas as pd
import plotly.express as px
from databaseConnection import mydb
import json
import os
import reports.intake.intake_parameters as intake_parameters

# Cache the loading of the column mapping to avoid repeated file I/O
@st.cache_data
def load_columns_mapping():
    """
    Loads a column mapping from a JSON file for renaming columns in the dataset.
    """
    json_file_path = 'reports/intake/intake_columns.json'  # Path to the JSON file
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            return json.load(f)
    else:
        st.error(f"Mapping file '{json_file_path}' not found.")
        return {}

# Memoize the database connection function to prevent multiple connections
@st.cache_resource
def get_db_engine():
    return mydb()

# Function to create and display cards for key metrics
def display_metrics(data):
    """
    Displays 'cards' for key metrics such as row count, unique materials, total weight.
    """

# Main function to handle the intake page
def intake_page(mindate, maxdate):
    """
    Defines the layout and logic for the intake report page where users can input
    parameters and generate a report with statistics and charts.
    """
    
    # Input parameters   
    # Importing the intake_parameters function from the reports/intake/intake_parameters.py file
    # This function returns the values of the input parameters    
    # The function is called only once and the results are cached for subsequent runs    
    # The function is also used to generate the SQL query for the report    
    suppliercode, supplier, hauliercode, haulier, intakestatustypes, rminclude, keytypes, calloff, siteid = intake_parameters.intake_parameters()
    
    # Run the report logic
    if 'run_report' not in st.session_state:
        st.session_state.run_report = False

    if st.session_state.run_report:
        try:
            with st.spinner('Running Report...'):
                suppliercode = f"'{suppliercode}'" if suppliercode != 'NULL' else 'NULL'
                hauliercode = f"'{hauliercode}'" if hauliercode != 'NULL' else 'NULL'
                haulier = f"'{haulier}'" if haulier != 'NULL' else 'NULL'
                supplier = f"'{supplier}'" if supplier != 'NULL' else 'NULL'
                calloff = f"'{calloff}'" if calloff != 'NULL' else 'NULL'
                keytypes = f"'{keytypes}'" if keytypes != 'NULL' else 'NULL'

                # Use cached database connection
                engine = get_db_engine()

                # SQL Stored Procedure execution
                storedProcedure = f"""
                    EXEC [Report].[SSRS_IntakeReport]
                    @mindate = '{mindate}',
                    @maxdate = '{maxdate}',
                    @suppliercode = {suppliercode},
                    @hauliercode = {hauliercode},
                    @intakestatustypes = '{intakestatustypes}',
                    @rminclude = '{rminclude}',
                    @haulier = {haulier},
                    @supplier = {supplier},
                    @calloff = {calloff},
                    @siteid = {siteid},
                    @keytypes = {keytypes}
                """
                dataSource = pd.read_sql(storedProcedure, engine)
                dataSource.sort_values(by='timein',axis=0, ascending=False,inplace=False,kind='quicksort')
                dataSource['timein'] = pd.to_datetime(dataSource['timein'], errors='coerce')
                dataSource['date'] = dataSource['timein'].dt.date
                dataSource['nettweight'] = dataSource['nettweight'].fillna(0)

                if dataSource.empty:
                    st.write("No data available to display.")
                else:
                    columns_to_display = load_columns_mapping()
                    if columns_to_display:
                        existing_columns = [col for col in columns_to_display.keys() if col in dataSource.columns]
                        dataSource_filtered = dataSource[existing_columns]
                        dataSource_filtered.rename(columns=columns_to_display, inplace=True)

                        # Display key metrics
                        display_metrics(dataSource_filtered)

                        # Organize the content in tabs
                        tab1, tab2, tab3, tab4 = st.tabs(["📅 Table", "📊 Charts", "📈 Statistics", "🔍 Insights"])

                        # Full table tab
                        with tab1:
                            st.dataframe(dataSource_filtered.sort_values('Time In'), hide_index=True, use_container_width=True, height=600)

                        # Charts tab
                        with tab2:
                            grouped_data = dataSource_filtered.groupby('RM Name').agg({'Nett Weight': 'sum'}).reset_index()

                            fig_rmName = px.bar(grouped_data.sort_values("Nett Weight"),
                                                x='Nett Weight', y='RM Name', orientation='h',
                                                title="Net Weight Intake by Raw Material Code",
                                                labels={'Nett Weight': 'Net Weight', 'RM Name': 'Raw Material Name'},
                                                color_discrete_sequence=['#475b7d'])
                            st.plotly_chart(fig_rmName, use_container_width=True)

                            fig_bayNumber = px.line(dataSource_filtered,
                                                    x="Time In", y="Nett Weight", color="Site ID",
                                                    title="Net Weight by Bay Number and Site",
                                                    hover_data=['RM Name'])
                            st.plotly_chart(fig_bayNumber, use_container_width=True)

                        # Statistics tab
                        with tab3:
                            st.write("### Descriptive Statistics of the Data")
                            st.write(dataSource_filtered.describe())

                        # Insights tab
                        with tab4:
                            st.write("### Key Insights")
                            st.write(f"- The raw material with the highest total weight is: {grouped_data.iloc[0]['RM Name']} "
                                    f"with {grouped_data.iloc[0]['Nett Weight']} kg.")
                            st.write(f"- A total of {len(dataSource_filtered['RM Name'].unique())} different raw materials were processed.")
                            st.write(f"- The highest site ID in the data is: {dataSource_filtered['Site ID'].max()}.")

                    else:
                        st.write("No column mapping found. Please check the mapping file.")

                st.session_state.run_report = False

        except Exception as e:
            st.error(f"An error occurred: {e}")
