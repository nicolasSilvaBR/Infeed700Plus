import functions.config as config
import streamlit as st
from left_menu.left_menu import LeftMenu
from functions.embedded_SSRS import embed_ssrs_report
import pandas as pd
from reports.intake.intake import intake_page
import logging
from functions.database_connection import mydb
import streamlit.components.v1 as components
from pathlib import Path
from functions.utilities import load_local_css, get_base64_image
from functions.web_app_enabled import IsWebAppEnabled
from functions.login_form import login_form

# From function folder import config > set_page_config()
config.set_page_config()

# Load custom CSS
load_local_css("assets/css/style.css")

# Create a database connection engine
engine = mydb()

def main():
    # Initial settings and database connection log
    logging.info(f"Database engine: {engine}")
    LeftMenu(engine)
    
    # Initialize session variables
    if 'selected_report' not in st.session_state:
        st.session_state['selected_report'] = None
    if 'show_report' not in st.session_state:
        st.session_state['show_report'] = False  # Controls report display
    if 'show_content' not in st.session_state:
        st.session_state['show_content'] = False  # Controls specific content display (dashboard or report)

    # Default dates
    minDate = st.session_state.get('minDate', pd.to_datetime("2024-10-01")).strftime('%Y-%m-%d')
    maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-10-30")).strftime('%Y-%m-%d')
    
    # Function to display the SSRS report
    def display_ssrs_report():
        """Display the SSRS report."""
        try:
            reportRDLname = st.session_state['selected_report']
            embed_ssrs_report(reportRDLname, minDate, maxDate)
        except Exception as e:
            if st.session_state['selected_report']:
                logging.error(f"Error loading report: {e}")
                st.error("An error occurred while loading the report. Verify that the SSRS server is online.")
            else:
                st.write("💬 Please select a Category and Report from the left menu.")

    # Function to display the dashboard
    def display_dashboard():
        """Display dashboard content."""
        intake_page(mindate=minDate, maxdate=maxDate)

    # Display main content based on session state
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # Update `show_content` and `show_report` based on the selected report
    if st.session_state['selected_report'] is not None:
        st.session_state['show_report'] = True
        st.session_state['show_content'] = True  # Show SSRS Report

    # Display the home (index.html) only if `show_content` is False
    if not st.session_state['show_content']:
        # Load image in Base64
        image_path = Path("assets/images/home_silo.png")
        image_url = ""
        if image_path.exists():
            image_base64 = get_base64_image(image_path)
            image_url = f"data:image/png;base64,{image_base64}"
        else:
            st.error("Image not found.")

        # Load and display HTML for the home page
        with open("index.html", "r") as file:
            index_html = file.read()
        
        index_html = index_html.replace("assets/images/home_silo.png", image_url)
        components.html(index_html, height=900, scrolling=True) 
    
    # If report header was selected, display specific content
    else:
        if st.session_state['show_report']:
            if st.session_state['selected-project'] in ['Infeed700', 'Enecoms']:
                display_ssrs_report()
            elif st.session_state['selected-project'] == 'Python':
                display_dashboard()

    # Close main div
    st.markdown('</div>', unsafe_allow_html=True)

# Entry point of the application
if __name__ == '__main__':
    # Initialize login state
    if 'is_logged_in' not in st.session_state:
        st.session_state['is_logged_in'] = False

    # Check if login is required
    if IsWebAppEnabled(engine) == '1':  # Login required
        if not st.session_state['is_logged_in']:
            if login_form():  # Successful login
                st.session_state['is_logged_in'] = True                
        if st.session_state['is_logged_in']:
            main()  # Display the main app
    else:  # Login not required
        main()