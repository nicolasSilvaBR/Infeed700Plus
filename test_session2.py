import streamlit as st
from streamlit_option_menu import option_menu
from functions.utilities import get_header_dict, get_report_dict,get_report_headers_and_reports_names  # Import custom functions from utilities.py
from database_connection import mydb
import pandas as pd


  
# This is already included in the main.py
engine = mydb()

with st.sidebar:
    headers_name, reports_names = get_report_headers_and_reports_names(engine)
    # Selectbox to choose a category
    selected_header = st.selectbox(
        label='Choose a category',
        options=headers_name['HeaderName']
    ) 
    # Filter reports based on the selected header
    filtered_reports = reports_names[reports_names['HeaderName'] == selected_header]
     
    # If there are filtered reports, display them in the option menu
    if not filtered_reports.empty:
        reports_option = option_menu(
            menu_title="Reports",
            menu_icon="bar-chart",
            icons=["chevron-double-right"] * len(filtered_reports),
            default_index=0,  # Default to the first option
            options=filtered_reports['ReportDisplayName'].tolist(),  # Use ReportDisplayName as options
            key="select_report_options"
        )        
        # Filter the reports based on the selected option from the option menu
        selected_report_details = filtered_reports[filtered_reports['ReportDisplayName'] == reports_option]
    else:
        st.write("No reports available for the selected category.")

    # Display the selected header
    if 'selected_report' not in st.session_state:
        st.session_state['selected_report']= None

    st.write(f"Selected header: {selected_header}")

    # Extract the 'ReportName' value as a simple string
    if not selected_report_details.empty:
        selected_report_name = selected_report_details['ReportName'].iloc[0]
        st.session_state['selected_report'] = selected_report_name
        st.session_state['selected_report']
    else:
        st.session_state['selected_report']
