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
try:
    response = requests.get(ssrs_url, auth=HttpNtlmAuth(username, password), timeout=10)

    # Check if the request was successful
    if response.status_code == 200:
        report_url = f"{ssrs_url}&rs:Embed=true&rc:Parameters=Collapsed"
        iframe_code = f"""
        <iframe width="100%" height="100%" style="min-height: 150vh;" src="{report_url}" frameborder="0" allowfullscreen></iframe>
        """
        st.components.v1.html(iframe_code, height=900, scrolling=False)
    else:
        st.error(f"Error accessing the report: {response.status_code}")

except requests.exceptions.ConnectTimeout:
    error_message = """
    **Connection Timeout Error**

    Possible reasons for this issue:
    1. Verify that the provided IP address `10.202.2.22` is correct and reachable.
    2. Ensure that the port `80` is open and accessible on the target server.
    3. Double-check the database name `Infeed700` in your report URL.
    4. Go to the `.secrets.toml` file and verify that the credentials (username and password) are correctly configured.

    Please resolve these potential issues and try again.
    """
    st.error(error_message)

except requests.exceptions.RequestException as e:
    st.error(f"Error accessing the report: {e}")
