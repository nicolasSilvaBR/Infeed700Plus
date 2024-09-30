import streamlit as st
import requests
from requests_ntlm import HttpNtlmAuth

@st.cache_resource
def embed_ssrs_report(reportRDLname, minDate, maxDate):
    """
    Embeds an SSRS report into the Streamlit app.

    Args:
        reportRDLname (str): Name of the report to display.
        minDate (str): Start date.
        maxDate (str): End date.
    """
    ipAddress = "10.202.2.22"
    port = "80"
    database = "Infeed700"
    ReportServerName = "ReportServer"
    username = "icm\\ndasilva"
    password = "1984Icm022*"

    # Build the SSRS report URL
    ssrs_url = f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&rs:Command=Render&MinDate={minDate}&MaxDate={maxDate}"

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
            st.components.v1.html(iframe_code, height=800, scrolling=False)
        else:
            st.error(f"Error accessing the report: {response.status_code}. Check the report name or parameters.")
    except requests.exceptions.ConnectTimeout:
        st.error("Connection error: Timeout while trying to access the server.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error accessing the report: {e}. Check your network connection and try again.")
