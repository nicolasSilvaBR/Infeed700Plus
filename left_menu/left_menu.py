import streamlit as st
from streamlit_option_menu import option_menu
from styles import menu_styles  # Import custom styles for the menu
import os  # File and path handling
from functions.utilities import load_local_css,display_footer,get_header_dict,get_report_dict,get_report_headers_and_reports_names  # Import custom functions from utilities.py
from database_connection import mydb
import pandas as pd

# Path to the logo image file
sidebar_logo_image_name = "ICM_300X80_OPT14.png"  

# Function to generate the sidebar menu
def LeftMenu(engine):
    """Build the sidebar menu for the Streamlit app.
    The first menu at top of the sidebar below the logo is the "Infeed700" menu.
    """    
    load_local_css("left_menu/expander_style.css")  # Load the CSS from the file
    png_file_path = os.path.join(f"assets/images", sidebar_logo_image_name) 
    with st.sidebar:
        
        # Display the logo directly using st.image
        if os.path.exists(png_file_path):
            st.image(png_file_path, use_column_width=True)  # Adjust the width to fit the sidebar
            
        headers_name, reports_names = get_report_headers_and_reports_names(engine)
        # Selectbox to choose a category
        selected_header = st.selectbox(
            label='',
            options=headers_name['HeaderName'],
            index=None,
            placeholder='Choose a category',
            key='selected_header'
        ) 
        # Filter reports based on the selected header
        filtered_reports = reports_names[reports_names['HeaderName'] == selected_header]      
        
        
        # If there are filtered reports, display them in the option menu
        if not filtered_reports.empty:
            reports_option = option_menu(
                menu_title="Reports",
                menu_icon="bar-chart",
                icons=["chevron-double-right"] * len(filtered_reports),
                default_index= 0 ,  # Default to the first option
                options=filtered_reports['ReportDisplayName'].tolist(),  # Use ReportDisplayName as options
                key="select_report_options",                
            )        
            # Filter the reports based on the selected option from the option menu
            selected_report_details = filtered_reports[filtered_reports['ReportDisplayName'] == reports_option]
            
            # Extract the 'ReportName' value as a simple string
            if not selected_report_details.empty:
                selected_report_name = selected_report_details['ReportName'].iloc[0]
                st.session_state['selected_report'] = selected_report_name                
            else:
                st.session_state['selected_report']  
                
        else:
            st.write("No reports available for the selected category.")
        
        
        st.divider()  # Divider before footer

        # Call the footer function from utilities.py
        display_footer()

       
# Execute LeftMenu only if the file is run directly
if __name__ == "__main__":
    LeftMenu()
