import streamlit as st
from streamlit_option_menu import option_menu
from styles import menu_styles  # Import custom styles for the menu
import os  # File and path handling
import utilities as utl # Function to load local CSS files

# Path to the logo image file
sidebar_logo_image_name = "ICM_300X80_OPT14.png"  

# Define headers and reports for the menu
headers = {1: "Intake", 2: "Blending", 3: "Press"}
reports = {
    1: [
        ["Intakes", "Intake"], 
        ["Intake Tips", "TipBreakdown"], 
        ['Intake Summary', 'IntakeSummary'], 
        ['Raw Material Mass Balance', 'RMUsageVsRMintake']
    ],
    # 2: [["Blending / Batching", "Batch"], ["Blending / Run", "BatchByRunNumber"]],
}

# Function to display report selection menu
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
                    options=options,
                    icons=["table"] * len(options),
                    default_index=0,  # Default to the first option
                    key=f"option_menu_{headerName}",
                    styles={
                        "container": menu_styles["container"], # styles.py sets the container style
                        "icon": menu_styles["icon"],
                        "nav-link": menu_styles["nav-link"],
                        "nav-link-selected": menu_styles["nav-link-selected"],
                        "icon-selected": menu_styles["icon-selected"], 
                    }
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
                    st.cache_data.clear()

# Function to generate the sidebar menu
def LeftMenu():
    """Build the sidebar menu for the Streamlit app.
    The first menu at top of the sidebar below the logo is the "Infeed700" menu.
    """
    
    utl.load_local_css("left_menu/expander_style.css")  # Load the CSS from the file

    png_file_path = os.path.join(f"images", sidebar_logo_image_name)  # Load the PNG icon          

    with st.sidebar:
        # Display the logo directly using st.image
        if os.path.exists(png_file_path):
            st.image(png_file_path, use_column_width=True)  # Adjust the width to fit the sidebar

        # Main menu
        with st.expander(label='', expanded=True):            
            selectedMenu = option_menu(
                menu_title="Infeed700",     
                menu_icon='bar-chart',
                options=["Dashboards", "SSRS Reports"],
                icons=["pie-chart-fill", "grid-3x3-gap-fill"],
                default_index=0,  # Default to Dashboards
                styles={
                        "container": menu_styles["container"], # styles.py sets the container style
                        "icon": menu_styles["icon"],
                        "nav-link": menu_styles["nav-link"],
                        "nav-link-selected": menu_styles["nav-link-selected"],
                        "icon-selected": menu_styles["icon-selected"], 
                        "menu_title": menu_styles["menu_title"],  # Apply the menu title style
                }
            )

            # Save the project selection in session_state
            st.session_state['Project'] = selectedMenu        

        # Show report menu if "SSRS Reports" is selected
        if selectedMenu == "SSRS Reports":
            display_report_selection(headers, reports)
            # Set "Intake" as the default global report if nothing else is selected
            if 'selected_report' not in st.session_state:
                st.session_state['selected_report'] = "Intake"          


        st.divider()  # Divider before footer

        # Call the footer function from utilities.py
        utl.display_footer()

       
# Execute LeftMenu only if the file is run directly
if __name__ == "__main__":
    LeftMenu()
