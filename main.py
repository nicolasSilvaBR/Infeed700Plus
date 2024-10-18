import config as config
import streamlit as st
from left_menu.left_menu import LeftMenu
from embedded_SSRS import embed_ssrs_report
import pandas as pd
from reports.intake.intake import intake_page  # Importing the intake_page function
import logging
from database_connection import mydb  # Importing the mydb function

config.set_page_config()

# Load the custom CSS file
def load_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Correct path to load the CSS from leftMenu directory or root directory
load_local_css("main_content.css")  # Update this path as needed

def main():
    engine = mydb()  # Get the database engine
    logging.info(f"Database engine: {engine}")  # Log the database engine

    LeftMenu(engine)  # Display the left sidebar menu   

    minDate = st.session_state.get('minDate', pd.to_datetime("2024-10-01")).strftime('%Y-%m-%d')
    maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-10-30")).strftime('%Y-%m-%d')

    def display_ssrs_report():
        """ Function to display the SSRS report. """
        try:
            with st.spinner('Running Report...'):
                if 'selected_report' not in st.session_state:
                    st.session_state['selected_report'] = 'Home'  # Default report
                    
                reportRDLname = st.session_state['selected_report']    
                embed_ssrs_report(reportRDLname, minDate, maxDate)
        except:
            st.error("An error occurred while loading the report. Verify that the SSRS server is online.") 

    def display_dashboard():
        """ Function to display the dashboard content. """  
        intake_page(mindate=minDate, maxdate=maxDate)

    # Apply custom CSS class to the main content area
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # Display content based on the menu selection    :
    
    
    display_ssrs_report()
      

    # Close the main content div
    st.markdown('</div>', unsafe_allow_html=True)

# Entry point of the application
if __name__ == '__main__':
    main()
