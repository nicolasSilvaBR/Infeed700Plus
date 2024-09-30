import streamlit as st
from leftMenu.leftMenu import LeftMenu
from embeddedSSRS import embed_ssrs_report
import pandas as pd

# Set page layout
st.set_page_config(layout="wide")

# Display the sidebar menu
LeftMenu()

# Check if the project is defined in session_state
if 'Project' not in st.session_state:
    st.session_state['Project'] = 'Dashboards'

# Get dates from session_state
minDate = st.session_state.get('minDate', pd.to_datetime("2024-08-01")).strftime('%Y-%m-%d')
maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-08-31")).strftime('%Y-%m-%d')

def display_ssrs_report():
    """Function to display the SSRS report."""
    if 'selected_report' not in st.session_state:
        st.session_state['selected_report'] = "Intake"  # Default value
    
    # Get the report name from session_state
    reportRDLname = st.session_state['selected_report']    
    # Call the function to embed the SSRS report
    embed_ssrs_report(reportRDLname, minDate, maxDate)

def display_dashboard():
    """Function to display dashboard content."""
    st.write(f"Displaying dashboard content for the dates: {minDate} to {maxDate}")

# Display content based on menu selection
if st.session_state['Project'] == 'SSRS Reports':
    st.header("SSRS Report")
    display_ssrs_report()
else:
    st.header("Dashboard")
    display_dashboard()
