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

# From function folder import config > set_page_config()
config.set_page_config()

# Load custom CSS
load_local_css("assets/css/style.css")

def main():
    # Initial settings and database connection log
    engine = mydb()
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
    
    # st.write(st.session_state['selected-project'])
    # st.write(st.session_state['selected_header'])
    # st.write(st.session_state['selected_report'])

    # Function to display the SSRS report
    def display_ssrs_report():
        """Display the SSRS report."""
        try:
            #with st.spinner('Running Report...'):
                reportRDLname = st.session_state['selected_report']
                embed_ssrs_report(reportRDLname, minDate, maxDate)                
        except Exception as e:
            if st.session_state['selected_report']:
                logging.error(f"Error loading report: {e}")
                st.error("An error occurred while loading the report. Verify that the SSRS server is online.") 
            elif not st.session_state['selected_report']:
                st.write('Choose a Category and Report on left menu')

    # Function to display the dashboard
    def display_dashboard():
        """Display dashboard content."""
        intake_page(mindate=minDate, maxdate=maxDate)

    # Display main content based on session state
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # Update `show_content` and `show_report` based on the selected report
    if st.session_state['selected_report'] is not None:
        st.session_state['show_report'] = True
        st.session_state['show_content'] = True

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
        components.html(index_html, height=1000, scrolling=True) 
    
    # If  report header was selected, display specific content
    else:  
        # Show the SSRS report if a report header was selected
        if st.session_state['show_report']:
            #st.write('Show the SSRS report if a report header was selected')
            display_ssrs_report()

    # Close main div
    st.markdown('</div>', unsafe_allow_html=True)

# Entry point of the application
if __name__ == '__main__':
    main()
