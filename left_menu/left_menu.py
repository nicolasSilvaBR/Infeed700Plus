import streamlit as st
from streamlit_option_menu import option_menu
import os
from functions.footer import display_footer as footer
from functions.report_header_name import get_report_headers_and_reports_names
from functions.sites import IsMultiSiteEnabled

# Path to the logo image file
sidebar_logo_image_name = "ICM_300X80_OPT14.png"  

# Function to generate the sidebar menu
def LeftMenu(engine):
    """Build the sidebar menu for the Streamlit app."""
    
    png_file_path = os.path.join("assets/images", sidebar_logo_image_name) 
    with st.sidebar:               
        # Display the logo directly using st.image
        if os.path.exists(png_file_path):
            st.image(png_file_path, use_column_width=True)  # Adjust the width to fit the sidebar  
        
        # Set default project if not already set in session state
        if "selected-project" not in st.session_state:
            st.session_state["selected-project"] = "Infeed700"
        
        # Function to clear the selected report session
        def clean_report_session():
            st.session_state['selected_report'] = False
        
        # Create buttons for "Infeed700" and "Enecoms" projects
        left, middle = st.columns(2)
        if left.button("Infeed700", icon="📊", use_container_width=True, type='secondary', on_click=clean_report_session):
            st.session_state["selected-project"] = "Infeed700"
            
        if middle.button("Enecoms", icon="⚡", use_container_width=True, on_click=clean_report_session):
            st.session_state["selected-project"] = "Enecoms"            
        
        project = st.session_state["selected-project"]
        
        # Check if MultiSiteEnabled is active and show site list if true
        IsMultiSiteEnabled(engine)        
        
        # Get report headers and report names based on the selected project
        headers_name, reports_names = get_report_headers_and_reports_names(project, engine)
        
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
        
        # Set icon based on the selected project
        menu_icon = "bar-chart" if st.session_state["selected-project"] == "Infeed700" else "bi-lightning"        
              
        # Display option menu
        if not filtered_reports.empty:
            reports_option = option_menu(
                menu_title=st.session_state["selected-project"],
                menu_icon=menu_icon,
                icons=["circle-fill"] * len(filtered_reports),
                default_index=0,  # Default to the first option
                options=filtered_reports['ReportDisplayName'].tolist(),  # Use ReportDisplayName as options
                key="select_report_options",   
                styles={
                    "icon": {                
                        "font-size": "8px",  # Font size for icons
                        "justify-content": "center",
                        "height": "10px",                                      
                        "line-height": "9px",
                    },
                    "nav-link": {
                        "font-size": "14px",  # Font size for options
                        "text-align": "left",
                        "margin": "2px",
                        "--hover-color": "#eee",
                        "line-height": "9px",
                    },
                    "nav-link-selected": {
                        "background-color": "#475b7c"
                    }
                }
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
            if 'selected_header' not in st.session_state:
                st.write("💬 No reports available for the selected category.")
            else:
                st.write("💬 Let's start by selecting the report category.")
        
        # Divider before footer
        st.divider()

        # Call the footer function
        footer()

# Execute LeftMenu only if the file is run directly
if __name__ == "__main__":
    LeftMenu()
