import streamlit as st
from leftMenu_custom_css import leftMenu_custom_css  # Custom CSS for the left menu
from leftMenu import LeftMenu  # Import the left menu functionality
import requests
from requests_ntlm import HttpNtlmAuth  # Autenticação NTLM

st.set_page_config(layout="wide")

# Display the left menu
LeftMenu()

# Call the intake page with predefined dates
# intake_page('2024-08-01', '2024-09-17')

# Credenciais
ipAddress = "10.202.2.22"
port = "80"
database = "Infeed700"
ReportServerName = "ReportServer"
username = "icm\\ndasilva"
password = "1984Icm022*"
reportRDLname ="Intake"

# https://learn.microsoft.com/en-us/sql/reporting-services/url-access-parameter-reference?view=sql-server-ver16
# rs:: Targets the report server.
# rc:: Targets an HTML Viewer.
# rv:: Targets the Report Viewer web part.

# URL do SSRS com parâmetros codificados
#ssrs_url = f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&ShowReportParameters=False&rs:Command=Render"
ssrs_url = f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&rs:Command=Render"

# Faz a requisição usando autenticação NTLM
response = requests.get(ssrs_url, auth=HttpNtlmAuth(username, password))

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Define a URL com o parâmetro de incorporação do SSRS
    report_url = f"{ssrs_url}&rs:Embed=true&rc:Parameters=Collapsed"    

    # Código HTML para incorporar o iframe
    iframe_code = f"""
    <iframe width="100%" height="100%" style="min-height: 120vh;" src="{report_url}" frameborder="0" allowfullscreen></iframe>
    """

   # Renderiza o iframe no Streamlit
    st.components.v1.html(iframe_code, height=800, scrolling=True)
else:
    st.error(f"Erro ao acessar o relatório: {response.status_code}")

