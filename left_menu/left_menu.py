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
    """Build the sidebar menu for the Streamlit app.
    The first menu at top of the sidebar below the logo is the "Infeed700" menu.
    """    
    #load_local_css("left_menu/expander_style.css")  # Load the CSS from the file
    png_file_path = os.path.join(f"assets/images", sidebar_logo_image_name) 
    with st.sidebar:               
        # Display the logo directly using st.image
        if os.path.exists(png_file_path):
            st.image(png_file_path, use_column_width=True)  # Adjust the width to fit the sidebar  
           
        if "selected-project" not in st.session_state:
            st.session_state["selected-project"] = "Infeed700"
            
        def clean_report_session():
            st.session_state['selected_report'] = False
        
        left, middle = st.columns(2)
        if left.button("Infeed700", icon="📊",use_container_width=True,type='secondary',on_click=clean_report_session):
            st.session_state["selected-project"] = "Infeed700"
            
        if middle.button("Enecoms", icon="⚡", use_container_width=True,on_click=clean_report_session):
            st.session_state["selected-project"] = "Enecoms"            
            
        project = st.session_state["selected-project"]
        
        # Check if the MultiSiteEnabled is enable and call the function to show the site list
        IsMultiSiteEnabled(engine)        
        
        headers_name, reports_names = get_report_headers_and_reports_names(project,engine)
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
        
        menu_icon = "bar-chart" if st.session_state["selected-project"] == "Infeed700" else "bi-lightning"
        
        # If there are filtered reports, display them in the option menu
        if not filtered_reports.empty:
            reports_option = option_menu(
                menu_title=st.session_state["selected-project"],
                menu_icon= menu_icon,
                icons=["circle-fill"] * len(filtered_reports),
                default_index= 0 ,  # Default to the first option
                options=filtered_reports['ReportDisplayName'].tolist(),  # Use ReportDisplayName as options
                key="select_report_options",   
                styles=  {    
                        "icon":{                
                        "font-size": "8px",  # Font size for icons
                        "justify-content": "center",
                        "Hight":"10px",
                        "line-height":"9px",                                        
                        },
                        "nav-link": {
                        "font-size": "14px",  # Tamanho da fonte das opções
                        "text-align": "left",
                        "margin": "2px",
                        "--hover-color": "#eee", 
                        "line-height":"9px" ,                                                                   
                        },
                        "nav-link-selected": {"background-color": "#475b7c"},
                        "nav-link:hover": {"color": "#FF5733",  # Cor do texto ao passar o mouse
                        "line-height":"9px"                   
                        }   
                    },  
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
        footer()

       
# Execute LeftMenu only if the file is run directly
if __name__ == "__main__":
    LeftMenu()
