import streamlit as st  # Importing Streamlit for building the web application
from leftMenu import LeftMenu  # Import the left menu functionality
import requests  # Importing the requests library for making HTTP requests
from requests_ntlm import HttpNtlmAuth  # Import NTLM authentication support

st.set_page_config(layout="wide")  # Setting the page layout to wide for better space utilization

# Display the left menu
LeftMenu()

# Call the intake page with predefined dates
# intake_page('2024-08-01', '2024-09-17')

# Database credentials and configuration settings
ipAddress = "10.202.2.22"  # The IP address of the database server
port = "80"                 # The port number to connect to the database
database = "Infeed700"     # The name of the database to be accessed
ReportServerName = "ReportServer"  # The name of the report server
username = "icm\\ndasilva" # Username for database authentication
password = "1984Icm022*"   # Password for database authentication
reportRDLname = "Intake"   # The name of the report to be generated

# SSRS URL parameter reference:
# https://learn.microsoft.com/en-us/sql/reporting-services/url-access-parameter-reference?view=sql-server-ver16
# rs:: Targets the report server.
# rc:: Targets an HTML Viewer.
# rv:: Targets the Report Viewer web part.

# Construct the URL for the SSRS report with encoded parameters
ssrs_url = f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&rs:Command=Render"

# Make the request using NTLM authentication
response = requests.get(ssrs_url, auth=HttpNtlmAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Define the URL with the embedding parameter for SSRS
    report_url = f"{ssrs_url}&rs:Embed=true&rc:Parameters=Collapsed"    

    # HTML code to embed the report in an iframe
    iframe_code = f"""
    <iframe width="100%" height="100%" style="min-height: 120vh;" src="{report_url}" frameborder="0" allowfullscreen></iframe>
    """

    # Render the iframe in Streamlit
    st.components.v1.html(iframe_code, height=800, scrolling=True)
else:
    # Display an error message if the request was not successful
    st.error(f"Error accessing the report: {response.status_code}")
