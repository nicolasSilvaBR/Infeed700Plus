import streamlit as st
from leftMenu.leftMenu import LeftMenu
import requests
from requests_ntlm import HttpNtlmAuth

st.set_page_config(layout="wide")

# Display the left menu
LeftMenu()

# Initialize session state if not already set
if 'selected_report' not in st.session_state:
    st.session_state['selected_report'] = "Intake"

reportRDLname = st.session_state['selected_report']

# Database credentials and configuration settings
ipAddress = "10.202.2.22"
port = "80"
database = "Infeed700"
ReportServerName = "ReportServer"
username = "icm\\ndasilva"
password = "1984Icm022*"

# Construct the URL for the SSRS report
ssrs_url = f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&rs:Command=Render&MinDate=2024-08-01"

# Make the request using NTLM authentication
response = requests.get(ssrs_url, auth=HttpNtlmAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    report_url = f"{ssrs_url}&rs:Embed=true&rc:Parameters=Collapsed"
    iframe_code = f"""
    <iframe width="100%" height="100%" style="min-height: 120vh;" src="{report_url}" frameborder="0" allowfullscreen></iframe>
    """
    st.components.v1.html(iframe_code, height=900, scrolling=False)
else:
    st.error(f"Error accessing the report: {response.status_code}")
