import streamlit as st
from streamlit_option_menu import option_menu
from styles import menu_styles  # Import custom styles
from utilities import load_svg  # Import function to load SVGs
import os  # For file path manipulation

# Define headers and reports for the menu
headers = {1: "Intake", 2: "Blending", 3: "Press"}
reports = {
    1: [["Intakes", "Intake"], ["Intake Tips", "TipBreakdown"]],
    2: [["Blending / Batching", "Batch"], ["Blending / Run", "BatchByRunNumber"]]
}

def LeftMenu():
    # Load local CSS for custom styles
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    local_css("leftMenu/expanderStyle.css")   
    svg_file_path = os.path.join("images", "home.svg")  # Path to the SVG file in images folder

    with st.sidebar:
        # Main options menu
        with st.expander(label='', expanded=True):
            # Load the SVG icon
            svg_icon = load_svg(svg_file_path)  

            selectedMenu = option_menu(
                menu_title="Infeed700",
                menu_icon="bar-chart-fill",
                options=["Dashboards", "SSRS Reports"],
                icons=["pie-chart-fill", "grid-3x3-gap-fill"],
                default_index=0,
                styles=menu_styles  # Apply custom styles
            )

        # Create the option menu for SSRS Reports
        if selectedMenu == "SSRS Reports":
            for headerskey, headerName in headers.items():
                # Check if the header key exists in reports
                if headerskey in reports:
                    with st.expander(headerName, expanded=False):
                        # Create sub-menu for report options
                        report_option = option_menu(
                            menu_title=None,
                            menu_icon="reception-4",
                            options=[report[0] for report in reports[headerskey]],
                            icons=["table"] * len(reports[headerskey]),
                            default_index=0,
                            key=headerName,
                            styles=menu_styles  # Apply custom styles
                        )

                        # Update the selected report based on user choice
                        for report in reports[headerskey]:
                            if report[0] == report_option:
                                st.session_state['selected_report'] = report[1]
