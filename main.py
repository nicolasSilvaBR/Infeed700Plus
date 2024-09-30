import streamlit as st
from leftMenu.leftMenu import LeftMenu
from embeddedSSRS import embed_ssrs_report
import pandas as pd
from reports.Intake.intake import intake_page  # Importando a função intake_page corretamente

# Configurar layout da página
st.set_page_config(layout="wide")

# Exibir o menu lateral
LeftMenu()

# Verificar se o projeto está definido no session_state
if 'Project' not in st.session_state:
    st.session_state['Project'] = 'Dashboards'  # Definir Dashboards como valor padrão

# Obter as datas do session_state ou definir valores padrão
minDate = st.session_state.get('minDate', pd.to_datetime("2024-08-01")).strftime('%Y-%m-%d')
maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-08-31")).strftime('%Y-%m-%d')

def display_ssrs_report():
    """Função para exibir o relatório SSRS."""
    if 'selected_report' not in st.session_state:
        st.session_state['selected_report'] = "Intake"  # Valor padrão
    
    # Obter o nome do relatório do session_state
    reportRDLname = st.session_state['selected_report']    
    # Chamar a função para incorporar o relatório SSRS
    embed_ssrs_report(reportRDLname, minDate, maxDate)


def display_dashboard():
    """Função para exibir o conteúdo do dashboard."""
    # st.write(f"Displaying dashboard content for the dates: {minDate} to {maxDate}")
    # Chamar a função intake_page para exibir o dashboard do Intake
    intake_page(mindate=minDate, maxdate=maxDate)

# Exibir o conteúdo com base na seleção do menu
if st.session_state['Project'] == 'SSRS Reports':
    st.header(f"SSRS Report{st.session_state['selected_report']}")
    display_ssrs_report()
else:
    st.header("Dashboard")
    display_dashboard()
