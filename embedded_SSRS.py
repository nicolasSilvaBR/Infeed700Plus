import streamlit as st
import requests
from requests_ntlm import HttpNtlmAuth
import pandas as pd
import datetime as datetime


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
        st.divider()
        col1, col2,col3,col4,col5,col6,col_ = st.columns([2,2,1,1,1,1,6])
        
        with col1:
            minDate = st.date_input("Start Date", value=pd.to_datetime("2024-10-01"), format="DD/MM/YYYY")
        with col2:
            maxDate = st.date_input("End Date", value=pd.to_datetime("2024-10-30"),format="DD/MM/YYYY")
        with col3:
            StartHour = st.selectbox(label='Start Hour',options=list(range(24)),index=0)
        with col4:
            EndHour = st.selectbox(label='End Hour',options=list(range(24)),index=23)
        with col5:
            StartMinute = st.selectbox(label='Start Minute',options=list(range(60)),index=0)
        with col6:
            EndMinute = st.selectbox(label='End Minute',options=list(range(60)),index=59)

        
    
    # ssrs credentials
    ssrs_config = st.secrets["ssrs_config"]
    required_keys = ["ipAddress", "port", "database", "ReportServerName", "username","password"]
    if not all(key in ssrs_config for key in required_keys):
        st.error("SSRS configuration not found in secrets.toml. Please add it to use this feature.")
        return    

    ipAddress = ssrs_config["ipAddress"]
    port = ssrs_config["port"]
    database = ssrs_config['database']
    ReportServerName = ssrs_config['ReportServerName']
    username = ssrs_config['username']
    password = ssrs_config['password']
    
    StartHour = str(StartHour)
    EndHour = str(EndHour)
    StartMinute = '00'
    EndMinute = '30'    

    # Build the SSRS report URL
    ssrs_url = f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&rs:Command=Render&MinDate={minDate}&MaxDate={maxDate}&StartHour={StartHour}&EndHour={EndHour}"

    # Make the request to the SSRS report
    try:
        response = requests.get(ssrs_url, auth=HttpNtlmAuth(username, password), timeout=100)

        if response.status_code == 200:
            report_url = f"{ssrs_url}&rs:Embed=true&rc:Parameters=Collapsed"
            iframe_code = f"""
            <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
                    src="{report_url}" frameborder="0" allowfullscreen></iframe>
            """
            # Usar height grande o suficiente para preencher a tela e garantir que o iframe ocupe 100% da área
            st.components.v1.html(iframe_code, height=780, scrolling=False)
        else:
            st.error(f"Error accessing the report: {response.status_code}. Check the report name or parameters. Check if the SSRS report '{reportRDLname}.rdl' exist in the web server.")
    except requests.exceptions.ConnectTimeout:
        st.error("Connection error: Timeout while trying to access the server.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error accessing the report: {e}. Check your network connection and try again.")
