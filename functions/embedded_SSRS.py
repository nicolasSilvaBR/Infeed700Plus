import streamlit as st
import requests
from requests_ntlm import HttpNtlmAuth
from functions.get_datetime_input import get_datetime_input

import toml
import os

def embed_ssrs_report(reportRDLname, minDate, maxDate):
    """
    Embeds an SSRS report into the Streamlit app.

    Args:
        reportRDLname (str): Name of the report to display.
        minDate (str): Start date.
        maxDate (str): End date.
    """      
    # Section for selecting dates with a calendar icon
    with st.expander(label=f"📶 {st.session_state['select_report_options']} Parameters ", expanded=False):  
        minDate, maxDate, StartHour, EndHour, StartMinute, EndMinute = get_datetime_input()

    # Retrieve the configuration file name from Streamlit secrets
    secrets_config = st.secrets.get("secrets_config", {"secrets_name": "secrets.toml"})
    secrets_name = secrets_config.get("secrets_name", "secrets.toml")

    # Ensure the file is located in the `.streamlit` directory
    if not secrets_name.endswith(".toml"):
        secrets_name = f".streamlit/{secrets_name}.toml"
    else:
        secrets_name = f".streamlit/{secrets_name}"

    # Convert to absolute path and check if the file exists
    absolute_path = os.path.abspath(secrets_name)
    if not os.path.isfile(absolute_path):
        st.error(f"The configuration file '{absolute_path}' was not found. Please check the path and file name.")
        return  # Stop execution if the file does not exist

    # Load configuration from the TOML file
    try:
        ssrs_config = toml.load(absolute_path)["ssrs_config"]
    except KeyError:
        st.error("The 'ssrs_config' section was not found in the configuration file.")
        return  # Stop execution if the section is missing
    except Exception as e:
        st.error(f"Error loading the configuration file: {e}")
        return  # Stop execution on loading error
    
    if 'selected-project' not in st.session_state:
        st.session_state['selected-project'] = 'Infeed700'
    
    # Select the database based on the project
    project = st.session_state['selected-project']
    if project == 'Infeed700':
        database_session = ssrs_config['database']
    elif project == 'Enecoms':
        database_session = ssrs_config.get('database-enecoms')
    else:
        st.write(st.session_state['selected-project'])
        st.error("Invalid project name. Use 'Infeed700' or 'Enecoms'. Ensure database names are specified in secrets.")
        return  # Stop execution on invalid project

    # Check required configuration keys
    required_keys = ["ipAddress", "port", "ReportServerName", "username", "password"]
    if not all(key in ssrs_config for key in required_keys):
        st.error("Missing SSRS configuration keys. Please check your secrets.toml.")
        return  # Stop execution if keys are missing

    # Retrieve SSRS credentials and settings
    ipAddress = ssrs_config["ipAddress"]
    port = ssrs_config["port"]
    database = database_session
    ReportServerName = ssrs_config['ReportServerName']
    username = ssrs_config['username']
    password = ssrs_config['password']

    # Prepare URL parameters
    StartHour, EndHour = str(StartHour), str(EndHour)
    StartMinute, EndMinute = str(StartMinute), str(EndMinute)
    site_id = str(st.session_state.get('selected_site_id', ''))

    # Construct the SSRS report URL based on the selected project
    if project == 'Infeed700':        
        # URL for Infeed700 with optional SiteId
        ssrs_url = ( 
            f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&rs:Command=Render"
            f"&MinDate={minDate}&MaxDate={maxDate}&StartHour={StartHour}&EndHour={EndHour}"
            f"&StartMinute={StartMinute}&EndMinute={EndMinute}"
        )
        
        # Add SiteId if multi-site is enabled
        if st.session_state.get('is_multi_site_enabled'):
            ssrs_url += f"&SiteId={site_id}"
            
    elif project == 'Enecoms':
        # URL for Enecoms without time or SiteId parameters
        selected_report = st.session_state.get('selected_report')
        if selected_report:
            ssrs_url = (
                f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&rs:Command=Render"
            )
        else:
            st.write("💬 Please select a Category and Report from the left menu.")
            return  # Stop execution if no report is selected

    # Function to render the iframe
    def render_iframe(url):
        report_url = f"{url}&rs:Embed=true&rc:Parameters=Collapsed"            
        iframe_code = f"""
        <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
                src="{report_url}" frameborder="0" allowfullscreen></iframe>
        """
        st.components.v1.html(iframe_code, height=820, scrolling=False)

    # Attempt to access the SSRS report
    try:
        response = requests.get(ssrs_url, auth=HttpNtlmAuth(username, password), timeout=100)
        if response.status_code == 200:
            render_iframe(ssrs_url)
        else:
            if st.session_state['selected_header']:
                st.error(f"Error accessing the report: {response.status_code}. Check the report name or parameters.")
            else:
                st.write("💬 Please select a Category and Report from the left menu.")                    
    except requests.exceptions.ConnectTimeout:
        st.error("Connection error: Timeout while trying to access the server.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error accessing the report: {e}. Check your network connection and try again.")
