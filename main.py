import config as config
import streamlit as st
from leftMenu.leftMenu import LeftMenu
from embeddedSSRS import embed_ssrs_report
import pandas as pd
from reports.intake.intake import intake_page  # Importing the intake_page function
import logging

config.set_page_config()

# Define the level of logging (if needed)
# logging.basicConfig(filename='debug.log', 
#                     level=logging.DEBUG, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')

def main():       

    LeftMenu()  # Display the left sidebar menu

    # Section for selecting dates with a calendar icon
    with st.expander(label="📅 Date Input", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            # Start Date input field
            minDate = st.date_input("Start Date", value=pd.to_datetime("2024-08-01"))
        with col2:
            # End Date input field
            maxDate = st.date_input("End Date", value=pd.to_datetime("2024-08-31"))

        # Save the selected dates in session_state for later use
        st.session_state['minDate'] = minDate
        st.session_state['maxDate'] = maxDate  

    # Check if the "Project" is defined in session_state, otherwise default to "Dashboards"
    if 'Project' not in st.session_state:
        st.session_state['Project'] = 'Dashboards'  # Default value

    logging.info(f"Project: {st.session_state['Project']}")  # Log the current project

    # Get the dates from session_state or set default values
    minDate = st.session_state.get('minDate', pd.to_datetime("2024-10-01")).strftime('%Y-%m-%d')
    maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-10-30")).strftime('%Y-%m-%d')

    def display_ssrs_report():
        """ Function to display the SSRS report. """
        try:
            with st.spinner('Running Report...'):  # Show a spinner while the report is loading
                # Set default report to "Intake" if no report is selected
                if 'selected_report' not in st.session_state:
                    st.session_state['selected_report'] = "Intake"  # Default report
                
                # Get the report name from session_state
                reportRDLname = st.session_state['selected_report']    
                
                # Call the function to embed the SSRS report
                embed_ssrs_report(reportRDLname, minDate, maxDate)
        except:
            st.error("An error occurred while loading the report. Verify that the SSRS server is online.")  # Error message

    def display_dashboard():
        """ Function to display the dashboard content. """  
        # Call the intake_page function to display the Intake dashboard
        intake_page(mindate=minDate, maxdate=maxDate)

    # Display content based on the menu selection
    if st.session_state['Project'] == 'SSRS Reports':
        # If "SSRS Reports" is selected, display the SSRS report
        display_ssrs_report()
        st.cache_data.clear()  # Clear cached data after displaying the report
    else:
        # If "Dashboards" is selected, display the dashboard
        display_dashboard()

# Entry point of the application
if __name__ == '__main__':
    main()
