import streamlit as st
import requests
from requests_ntlm import HttpNtlmAuth
import pandas as pd
from functions.utilities import get_datetime_input

def embed_ssrs_report(reportRDLname, minDate, maxDate):
    """
    Embeds an SSRS report into the Streamlit app.

    Args:
        reportRDLname (str): Name of the report to display.
        minDate (str): Start date.
        maxDate (str): End date.
    """
    # Section for selecting dates with a calendar icon
    with st.expander(label="📆 Date Input", expanded=False):  
        minDate, maxDate, StartHour, EndHour, StartMinute, EndMinute = get_datetime_input()
    
    # Load SSRS configuration from secrets
    ssrs_config = st.secrets["ssrs_config"]  

    # Select the database based on the project
    if st.session_state['selected-project'] == 'Infeed700':
        database_session = ssrs_config['database']
    elif st.session_state['selected-project'] == 'Enecoms':
        database_session = ssrs_config['database-enecoms']
    else:
        st.error("Check the Project name: Infeed700 / Enecoms and ensure database names are correctly specified in secrets.")
        return
    
    # Check required configuration keys
    required_keys = ["ipAddress", "port", "database", "ReportServerName", "username", "password"]
    if not all(key in ssrs_config for key in required_keys):
        st.error("SSRS configuration not found in secrets.toml. Please add it to use this feature.")
        return    

    # Retrieve SSRS credentials
    ipAddress = ssrs_config["ipAddress"]
    port = ssrs_config["port"]
    database = database_session
    ReportServerName = ssrs_config['ReportServerName']
    username = ssrs_config['username']
    password = ssrs_config['password']

    # Prepare URL parameters
    StartHour, EndHour = str(StartHour), str(EndHour)
    StartMinute, EndMinute = str(StartMinute), str(EndMinute)
    site_id = str(st.session_state['selected_site_id'])
   
    
    # Construct the SSRS report URL based on the selected project
    if st.session_state['selected-project'] == 'Infeed700':        
        # URL for Infeed700 with optional SiteId
        ssrs_url = ( 
            f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&rs:Command=Render"
            f"&MinDate={minDate}&MaxDate={maxDate}&StartHour={StartHour}&EndHour={EndHour}"
            f"&StartMinute={StartMinute}&EndMinute={EndMinute}"
        )
        
        # Add SiteId if multi-site is enabled
        if st.session_state['is_multi_site_enabled']:
            ssrs_url += f"&SiteId={site_id}"
            
    elif st.session_state['selected-project'] == 'Enecoms':
        # URL for Enecoms without time or SiteId parameters
        if st.session_state['selected_report']:
            ssrs_url = ( 
                f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&rs:Command=Render"
            )
        else:
            st.error("Please select a report for Enecoms.")
            return

    # Function to render the iframe
    def render_iframe(url):
        report_url = f"{url}&rs:Embed=true&rc:Parameters=Collapsed"            
        iframe_code = f"""
        <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
                src="{report_url}" frameborder="0" allowfullscreen></iframe>
        """
        st.components.v1.html(iframe_code, height=780, scrolling=False)

    # Attempt to access the SSRS report
    try:
        response = requests.get(ssrs_url, auth=HttpNtlmAuth(username, password), timeout=100)
        if response.status_code == 200:
            render_iframe(ssrs_url)
        else:
            st.error(f"Error accessing the report: {response.status_code}. Check the report name or parameters.")
    except requests.exceptions.ConnectTimeout:
        st.error("Connection error: Timeout while trying to access the server.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error accessing the report: {e}. Check your network connection and try again.")
