import streamlit as st
from leftMenu_custom_css import leftMenu_custom_css  # Custom CSS for the left menu
from leftMenu import LeftMenu  # Import the left menu functionality
import requests
from requests_ntlm import HttpNtlmAuth  # Autenticação NTLM

# Configure the page layout to "wide" (esta linha deve ser a primeira)
st.set_page_config(layout="wide")

# Apply custom left menu styles (if necessary)
leftMenu_custom_css()

# Display the left menu
LeftMenu()

# Call the intake page with predefined dates
# intake_page('2024-08-01', '2024-09-17')

# Credenciais
username = "icm\\ndasilva"
password = "1984Icm022*"

# URL do SSRS com parâmetros codificados
ssrs_url = "http://10.202.2.22:80/ReportServer/Pages/ReportViewer.aspx?%2fInfeed700%2fIntake&rs:Command=Render"

# Faz a requisição usando autenticação NTLM
response = requests.get(ssrs_url, auth=HttpNtlmAuth(username, password))

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Define a URL com o parâmetro de incorporação do SSRS
    report_url = f"{ssrs_url}&rs:Embed=true"    

    # Código HTML para incorporar o iframe
    iframe_code = f"""
    <iframe width="100%" height="900px" src="{report_url}" frameborder="0" allowfullscreen></iframe>
    """

    # Renderiza o iframe no Streamlit
    st.components.v1.html(iframe_code, height=1024)
else:
    st.error(f"Erro ao acessar o relatório: {response.status_code}")

