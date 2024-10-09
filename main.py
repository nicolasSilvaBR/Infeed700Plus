import config as config
import streamlit as st
from leftMenu.leftMenu import LeftMenu
from embeddedSSRS import embed_ssrs_report
import pandas as pd
from reports.intake.intake import intake_page  # Importing the intake_page function
import logging

config.set_page_config()

# Load the custom CSS file
def load_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Correct path to load the CSS from leftMenu directory or root directory
load_local_css("main_content.css")  # Update this path as needed

def main():
    LeftMenu()  # Display the left sidebar menu

    # # Section for selecting dates with a calendar icon
    # with st.expander(label="📅 Date Input", expanded=False):
    #     col1, col2 = st.columns(2)
    #     with col1:
    #         minDate = st.date_input("Start Date", value=pd.to_datetime("2024-10-01"))
    #     with col2:
    #         maxDate = st.date_input("End Date", value=pd.to_datetime("2024-10-30"))

    #     # Save the selected dates in session_state for later use
    #     st.session_state['minDate'] = minDate
    #     st.session_state['maxDate'] = maxDate  

    # Check if the "Project" is defined in session_state, otherwise default to "Dashboards"
    if 'Project' not in st.session_state:
        st.session_state['Project'] = 'Dashboards'  # Default value

    logging.info(f"Project: {st.session_state['Project']}")  # Log the current project

    minDate = st.session_state.get('minDate', pd.to_datetime("2024-10-01")).strftime('%Y-%m-%d')
    maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-10-30")).strftime('%Y-%m-%d')

    def display_ssrs_report():
        """ Function to display the SSRS report. """
        try:
            with st.spinner('Running Report...'):
                if 'selected_report' not in st.session_state:
                    st.session_state['selected_report'] = "Intake"  # Default report
                reportRDLname = st.session_state['selected_report']    
                embed_ssrs_report(reportRDLname, minDate, maxDate)
        except:
            st.error("An error occurred while loading the report. Verify that the SSRS server is online.") 

    def display_dashboard():
        """ Function to display the dashboard content. """  
        intake_page(mindate=minDate, maxdate=maxDate)

    # Apply custom CSS class to the main content area
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # Display content based on the menu selection
    if st.session_state['Project'] == 'SSRS Reports':
        display_ssrs_report()
        st.cache_data.clear()  # Clear cached data after displaying the report
    else:
        display_dashboard()

    # Close the main content div
    st.markdown('</div>', unsafe_allow_html=True)

# Entry point of the application
if __name__ == '__main__':
    main()
