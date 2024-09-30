import streamlit as st
from streamlit_option_menu import option_menu
from styles import menu_styles  # Import custom styles for the menu
from utilities import load_svg  # Function to load SVG icons
import os  # File and path handling
import pandas as pd  # Date handling

# Define headers and reports for the menu
headers = {1: "Intake", 2: "Blending", 3: "Press"}
reports = {
    1: [["Intakes", "Intake"], ["Intake Tips", "TipBreakdown"]],
    2: [["Blending / Batching", "Batch"], ["Blending / Run", "BatchByRunNumber"]],   
}

def load_local_css(file_name):
    """Load local CSS for custom styles."""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file '{file_name}' not found.")
        
st.cache_data.clear()
def display_report_selection(headers, reports):
    """Display report selection menu based on headers and defined reports."""
    for headerskey, headerName in headers.items():
        if headerskey in reports:  # Ensure the header key exists in reports
            with st.expander(headerName, expanded=False):
                # Get the list of report options
                options = [report[0] for report in reports[headerskey]]

                # Create the report option menu using option_menu
                report_option = option_menu(
                    menu_title=None,
                    menu_icon="reception-4",
                    options=options,  # Report name options
                    icons=["table"] * len(options),
                    default_index=0,  # Always default to the first option
                    key=f"option_menu_{headerName}",  # Unique key per header
                    styles=menu_styles
                )

                # Get the selected report based on the user's selection
                selected_report = reports[headerskey][options.index(report_option)][1]

                # Check if the user made a new selection in this specific header
                session_key = f'selected_report_{headerName}'  # Unique session state key for each header
                if st.session_state.get(session_key) != selected_report:
                    # Update the session state for this header
                    st.session_state[session_key] = selected_report
                    # Update the global selected report only when user makes a new selection
                    st.session_state['selected_report'] = selected_report

    # Display the final selected report for debugging purposes
    #st.write(f"Global Selected Report: {st.session_state['selected_report']}")  # Debugging output

def LeftMenu():
    """Build the sidebar menu for the Streamlit app."""
    load_local_css("leftMenu/expanderStyle.css")
    svg_file_path = os.path.join("images", "home.svg")  # Load the SVG icon

    with st.sidebar:
        # Main menu with SVG icon
        with st.expander(label='', expanded=True):
            svg_icon = load_svg(svg_file_path)
            selectedMenu = option_menu(
                menu_title="Infeed700",
                menu_icon="bar-chart-fill",
                options=["Dashboards", "SSRS Reports"],
                icons=["pie-chart-fill", "grid-3x3-gap-fill"],
                default_index=0,  # Default to Dashboards
                styles=menu_styles
            )

            # Save the project selection in session_state
            st.session_state['Project'] = selectedMenu
        
        # Section for selecting dates with calendar icon
        with st.expander(label="📅 Date Input", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                minDate = st.date_input("Start Date", value=pd.to_datetime("2024-08-01"))
            with col2:
                maxDate = st.date_input("End Date", value=pd.to_datetime("2024-08-31"))
            
            # Save the selected dates in session_state
            st.session_state['minDate'] = minDate
            st.session_state['maxDate'] = maxDate
        
        # Show report menu if "SSRS Reports" is selected
        if selectedMenu == "SSRS Reports":
            display_report_selection(headers, reports)

            # Set "Intake" as the default global report if nothing else is selected
            if 'selected_report' not in st.session_state:
                st.session_state['selected_report'] = "Intake"

