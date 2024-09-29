import streamlit as st
from streamlit_option_menu import option_menu
from styles import menu_styles  # Import custom styles for the menu
from utilities import load_svg  # Import function to load SVGs for icons
import os  # For file path manipulation
import pandas as pd  # Import pandas for date handling

# Define headers and reports for the menu
headers = {1: "Intake", 2: "Blending", 3: "Press"}
reports = {
    1: [["Intakes", "Intake"], ["Intake Tips", "TipBreakdown"]],
    2: [["Blending / Batching", "Batch"], ["Blending / Run", "BatchByRunNumber"]]
}

def load_local_css(file_name):
    """Load local CSS for custom styles."""
    try:
        with open(file_name) as f:
            # Load CSS styles into the Streamlit app
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        # Warn the user if the CSS file is not found
        st.warning(f"CSS file '{file_name}' not found.")

def display_report_selection(headers, reports):
    """Display the report selection menu based on defined headers and reports."""
    for headerskey, headerName in headers.items():
        if headerskey in reports:
            with st.expander(headerName, expanded=False):
                # Create an option menu for report selection
                report_option = option_menu(
                    menu_title=None,
                    menu_icon="reception-4",
                    options=[report[0] for report in reports[headerskey]],  # Get report names
                    icons=["table"] * len(reports[headerskey]),  # Use the same icon for each report
                    default_index=0,
                    key=headerName,
                    styles=menu_styles  # Apply custom styles
                )
                # Update the selected report based on user choice
                for report in reports[headerskey]:
                    if report[0] == report_option:
                        # Save the selected report in session state
                        st.session_state['selected_report'] = report[1]

def LeftMenu():
    """Construct the left menu for the Streamlit application."""
    # Load local CSS for custom styles
    load_local_css("leftMenu/expanderStyle.css")
    svg_file_path = os.path.join("images", "home.svg")  # Path to the SVG file in images folder

    with st.sidebar:
        # Main options menu
        with st.expander(label='', expanded=True):
            # Load the SVG icon for the application
            svg_icon = load_svg(svg_file_path)  
            
            # Create the main menu for selecting between Dashboards and SSRS Reports
            selectedMenu = option_menu(
                menu_title="Infeed700",
                menu_icon="bar-chart-fill",
                options=["Dashboards", "SSRS Reports"],
                icons=["pie-chart-fill", "grid-3x3-gap-fill"],
                default_index=0,
                styles=menu_styles  # Apply custom styles
            )

            # Set the selected project in session state
            st.session_state['Project'] = selectedMenu
        
        # Add date inputs for minDate and maxDate in the sidebar
        with st.expander(label="Date Input", expanded=True, icon="📅"):
            col1, col2 = st.columns(2)  # Create two columns for date inputs
            with col1:
                # User input for minimum date
                minDate = st.date_input("Start Date", value=pd.to_datetime("2024-08-01"))  
            with col2:
                # User input for maximum date
                maxDate = st.date_input("End Date", value=pd.to_datetime("2024-08-31"))  
            
            # Save selected dates in session state for later use
            st.session_state['minDate'] = minDate  
            st.session_state['maxDate'] = maxDate  
        
        # Create the option menu for SSRS Reports if selected
        if selectedMenu == "SSRS Reports":
            display_report_selection(headers, reports)  # Display the report selection menu
