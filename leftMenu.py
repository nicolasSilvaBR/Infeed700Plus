import streamlit as st
import pandas as pd
from databaseConnection import mydb
import streamlit.components.v1 as components

# Establish database connection
engine = mydb()

# Credenciais
ipAddress = "10.202.2.22"
port = "80"
database = "Infeed700"
ReportServerName = "ReportServer"
username = "icm\\ndasilva"
password = "1984Icm022*"
reportRDLname = "Intake"

headers = {"Intake": 1, "Blending": 2, "Press": 3}
reports = {"Intake": 1, "IntakeTip": 1, "Blending": 2,"Press Summary": 3}

def LeftMenu():
    # Carregar o arquivo CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Chamar a função para carregar o CSS
    local_css("style.css")


    with st.sidebar:
        for header, valor in headers.items():
            with st.expander(header, expanded=False):
                for report, valor2 in reports.items():
                    if valor2 == valor:
                        st.markdown(f"""
                            <a target="_self" class="sidebar-item" href="http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{report}&rs:Command=Render">{report} <span>›</span></a>
                        """, unsafe_allow_html=True)
