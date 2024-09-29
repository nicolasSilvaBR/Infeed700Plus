import streamlit as st
from leftMenu.leftMenu import LeftMenu
from embeddedSSRS import embed_ssrs_report
import pandas as pd  # Import pandas for date handling

# Set the page layout for the Streamlit app
st.set_page_config(layout="wide")

# Display the left menu for navigation
LeftMenu()

# Initialize session state for the project type
if 'Project' not in st.session_state:
    st.session_state['Project'] = 'Dashboards'  # Set default project to Dashboards

# Retrieve the dates from session state with default values
minDate = st.session_state.get('minDate', pd.to_datetime("2024-08-01")).strftime('%Y-%m-%d')  # Default start date
maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-08-31")).strftime('%Y-%m-%d')  # Default end date

def display_ssrs_report():
    """Function to display the SSRS report."""
    # Initialize session state for the selected report if not already set
    if 'selected_report' not in st.session_state:
        st.session_state['selected_report'] = "Intake"  # Set default report to Intake

    reportRDLname = st.session_state['selected_report']  # Get the selected report name
    embed_ssrs_report(reportRDLname, minDate, maxDate)  # Call function to embed the SSRS report

def display_dashboard():
    """Function to display the dashboard content."""
    # Display a message with the selected date range
    st.write(f"Displaying dashboard content for dates: {minDate} to {maxDate}")

# Check which project is selected
if st.session_state['Project'] == 'SSRS Reports':
    st.header("SSRS Report")  # Add a header for the SSRS Report section
    display_ssrs_report()  # Call the function to display the SSRS report
else:
    st.header("Dashboard")  # Add a header for the Dashboard section
    display_dashboard()  # Call the function to display the dashboard content
