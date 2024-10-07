import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from databaseConnection import mydb
import json
import os
from functions.create_card import create_card


# Function to load the column mapping from a JSON file
def load_columns_mapping():
    """
    This function reads a JSON file that contains the column mappings for renaming
    columns in the final dataset. If the JSON file is not found, it returns an error message.
    """
    

    json_file_path = 'reports/intake/intake_columns.json'  # Path to the JSON file
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            return json.load(f)
    else:
        st.error(f"Mapping file '{json_file_path}' not found.")
        return {}

# Function to create and display cards for key metrics
def display_metrics(data):
    """
    This function generates 'cards' displaying key metrics from the dataset,
    such as the total number of rows, unique materials, total weight, etc.
    It uses Streamlit's column feature to display the cards side by side.
    """
    total_rows = len(data)
    unique_materials = data['RM Name'].nunique()
    total_weight = data['Nett Weight'].sum()

    # Card for total rows
    # Display the cards
    # Display the cards with customized attributes
    col1, col2, col3 = st.columns(3)

    # Display the card for total rows
    # with col1:
    #     st.markdown(create_card("Total Rows", total_rows, 
    #                             width="200px", height="100px",  # Adjusted height
    #                             title_color="white", value_color="white",  
    #                             title_font_size="18px", value_font_size="22px", 
    #                             background_gradient_start="#1b4e57", 
    #                             background_gradient_end="#1b4e57"),  
    #                 unsafe_allow_html=True)

    # # Display the card for unique materials
    # with col2:
    #     st.markdown(create_card("Unique Materials", unique_materials, 
    #                             width="200px", height="100px",  # Adjusted height
    #                             title_color="white", value_color="white",  
    #                             title_font_size="18px", value_font_size="22px", 
    #                             background_gradient_start="#1b4e57", 
    #                             background_gradient_end="#1b4e57"),  
    #                 unsafe_allow_html=True)

    # # Display the card for total weight
    # with col3:
    #     st.markdown(create_card("Total Weight (kg)", total_weight, 
    #                             width="200px", height="100px",  # Adjusted height
    #                             title_color="white", value_color="white",  
    #                             title_font_size="18px", value_font_size="22px", 
    #                             background_gradient_start="#1b4e57", 
    #                             background_gradient_end="#1b4e57"),  
    #                 unsafe_allow_html=True)


# Main function to handle the intake page
def intake_page(mindate, maxdate):
    """
    This function defines the layout for the intake report page, where users can input 
    various parameters, generate the report, and display insights, statistics, and charts.
    """
    
    # Input fields and report generation button layout
    with st.container():
        # Two columns, one wider for input fields and another for the "Run Report" button
        col1, col2 = st.columns([10, 1])

        # Input parameters section
        with col1:
            # Expander for input parameters (collapsed by default)
            with st.expander("Input Parameters", expanded=False):
                input_col1, input_col2, input_col3 = st.columns(3)

                # Different input fields for filtering
                with input_col1:
                    suppliercode = st.text_input('Supplier Code', value='NULL', key='input_suppliercode')
                    supplier = st.text_input('Supplier', value='NULL', key='input_supplier')
                    hauliercode = st.text_input('Haulier Code', value='NULL', key='input_hauliercode')
                    haulier = st.text_input('Haulier', value='NULL', key='input_haulier')

                with input_col2:
                    intakestatustypes = st.text_input('Intake Status Types', value='1,2,3', key='input_intakestatustypes')
                    rminclude = st.text_input('RM Include', value='-1', key='input_rminclude')
                    keytypes = st.text_input('Key Types', value='1,31,41,51', key='input_keytypes')

                with input_col3:
                    calloff = st.text_input('Call Off', value='NULL', key='input_calloff')
                    siteid = st.number_input('Site ID', value=0, key='input_siteid')

        # Run report button
        with col2:
            if st.button('Run Report', key='run_report_button'):
                st.session_state.run_report = True

    # Check if the report should be generated
    if 'run_report' not in st.session_state:
        st.session_state.run_report = False

    if st.session_state.run_report:
        try:
            # Show spinner while the SQL query is executed
            with st.spinner('Running Report...'):
                # Format parameters for SQL stored procedure
                suppliercode = f"'{suppliercode}'" if suppliercode != 'NULL' else 'NULL'
                hauliercode = f"'{hauliercode}'" if hauliercode != 'NULL' else 'NULL'
                haulier = f"'{haulier}'" if haulier != 'NULL' else 'NULL'
                supplier = f"'{supplier}'" if supplier != 'NULL' else 'NULL'
                calloff = f"'{calloff}'" if calloff != 'NULL' else 'NULL'
                keytypes = f"'{keytypes}'" if keytypes != 'NULL' else 'NULL'

                # Establish a connection to the database using a custom function (mydb)
                engine = mydb()

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

                # Fetch data from the database
                dataSource = pd.read_sql(storedProcedure, engine).sort_values('timein')

                # Convert 'timein' to datetime format to avoid errors with .dt accessor
                dataSource['timein'] = pd.to_datetime(dataSource['timein'], errors='coerce')

                # Extract date part
                dataSource['date'] = dataSource['timein'].dt.date

                # Check for NaN values and handle them in the scatter plot size
                dataSource['nettweight'] = dataSource['nettweight'].fillna(0)

                # Check if data exists
                if dataSource.empty:
                    st.write("No data available to display.")
                else:
                    # Continue with the rest of your code
                    # Load the column mapping
                    columns_to_display = load_columns_mapping()

                    if columns_to_display:
                        # Filter and rename columns based on the mapping
                        existing_columns = [col for col in columns_to_display.keys() if col in dataSource.columns]
                        dataSource_filtered = dataSource[existing_columns]
                        dataSource_filtered.rename(columns=columns_to_display, inplace=True)

                        # Display key metrics using cards
                        display_metrics(dataSource_filtered)

                        # Organize the content in tabs
                        tab1, tab2, tab3, tab4 = st.tabs(["📅 Table", "📊 Charts", "📈 Statistics", "🔍 Insights"])

                        # Full table tab
                        with tab1:                            
                            st.dataframe(data=dataSource_filtered.sort_values('Time In'), hide_index=True,use_container_width=True,height=600)                       

                        # Charts
                        with tab2:   
                            # Group data for visualization
                            grouped_data = dataSource_filtered.groupby('RM Name').agg({'Nett Weight': 'sum'}).reset_index()

                            # Bar chart for Net Weight by Material
                            fig_rmName = px.bar(
                                grouped_data.sort_values("Nett Weight"),
                                x='Nett Weight',
                                y='RM Name',
                                orientation='h',
                                title="Net Weight Intake by Raw Material Code",
                                labels={'Nett Weight': 'Net Weight', 'RM Name': 'Raw Material Name'},
                                color_discrete_sequence=['#475b7d'],
                            )
                            st.plotly_chart(fig_rmName, use_container_width=True)

                            # Scatter plot for Net Weight by Bay Number
                            fig_bayNumber = px.line(
                                dataSource_filtered,
                                x="Time In",
                                y="Nett Weight",
                                color="Site ID",
                                title="Net Weight by Bay Number and Site",
                                hover_data=['RM Name']
                            )
                            st.plotly_chart(fig_bayNumber, use_container_width=True)

                        # Statistics tab
                        with tab3:
                            st.write("### Descriptive Statistics of the Data")
                            st.write(dataSource_filtered.describe())

                        # Insights tab
                        with tab4:
                            st.write("### Key Insights")

                            # Adding more detailed insights based on the data
                            st.write(f"- The raw material with the highest total weight is: {grouped_data.iloc[0]['RM Name']} "
                                    f"with {grouped_data.iloc[0]['Nett Weight']} kg.")
                            st.write(f"- A total of {len(dataSource_filtered['RM Name'].unique())} different raw materials were processed.")
                            st.write(f"- The highest site ID in the data is: {dataSource_filtered['Site ID'].max()}.")

                    else:
                        st.write("No column mapping found. Please check the mapping file.")

                # Reset the session state to avoid continuous re-execution
                st.session_state.run_report = False

        except Exception as e:
            st.error(f"An error occurred: {e}")

