import config as config
import streamlit as st
from leftMenu.leftMenu import LeftMenu
from embeddedSSRS import embed_ssrs_report
import pandas as pd
from reports.Intake.intake import intake_page  # Importando a função intake_page corretamente
import logging

config.set_page_config()

logging.basicConfig(filename='streamlit.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
def main():       

    LeftMenu()    

    # Verificar se o projeto está definido no session_state
    if 'Project' not in st.session_state:
        st.session_state['Project'] = 'Dashboards'  # Definir Dashboards como valor padrão

    logging.info(f"Project: {st.session_state['Project']}")
    # Obter as datas do session_state ou definir valores padrão
    minDate = st.session_state.get('minDate', pd.to_datetime("2024-10-01")).strftime('%Y-%m-%d')
    maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-10-30")).strftime('%Y-%m-%d')

    def display_ssrs_report():
        """ Function to view the SSRS report."""
        try:
            with st.spinner('Running Report...'):           
                if 'selected_report' not in st.session_state:
                    st.session_state['selected_report'] = "Intake"  # Valor padrão
                
                # Obter o nome do relatório do session_state
                reportRDLname = st.session_state['selected_report']    
                # Chamar a função para incorporar o relatório SSRS
                embed_ssrs_report(reportRDLname, minDate, maxDate)
        except:
            st.error("An error occurred while loading the report. Verify that the SSRS server is online.")


    def display_dashboard():
        """Função para exibir o conteúdo do dashboard."""  
        # Chamar a função intake_page para exibir o dashboard do Intake
        intake_page(mindate=minDate, maxdate=maxDate)

    # Exibir o conteúdo com base na seleção do menu
    if st.session_state['Project'] == 'SSRS Reports':
       # st.header(f"SSRS Report{st.session_state['selected_report']}")
        display_ssrs_report()
        st.cache_data.clear()
    else:
        display_dashboard()
        

if __name__ == '__main__':
    main()




# # Configurar layout da página
# st.set_page_config(
#     page_title="Infeed700 Reports",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# Infeed700. Version 1.0 *BETA* ICM CSL"
#     }
# )

# # Exibir o menu lateral
# LeftMenu()

# # Verificar se o projeto está definido no session_state
# if 'Project' not in st.session_state:
#     st.session_state['Project'] = 'Dashboards'  # Definir Dashboards como valor padrão

# # Obter as datas do session_state ou definir valores padrão
# minDate = st.session_state.get('minDate', pd.to_datetime("2024-10-01")).strftime('%Y-%m-%d')
# maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-10-30")).strftime('%Y-%m-%d')

# def display_ssrs_report():
#     """Função para exibir o relatório SSRS."""
#     if 'selected_report' not in st.session_state:
#         st.session_state['selected_report'] = "Intake"  # Valor padrão
    
#     # Obter o nome do relatório do session_state
#     reportRDLname = st.session_state['selected_report']    
#     # Chamar a função para incorporar o relatório SSRS
#     embed_ssrs_report(reportRDLname, minDate, maxDate)


# def display_dashboard():
#     """Função para exibir o conteúdo do dashboard."""  
#     # Chamar a função intake_page para exibir o dashboard do Intake
#     intake_page(mindate=minDate, maxdate=maxDate)

# # Exibir o conteúdo com base na seleção do menu
# if st.session_state['Project'] == 'SSRS Reports':
#    # st.header(f"SSRS Report{st.session_state['selected_report']}")
#     display_ssrs_report()
#     st.cache_data.clear()
# else:
#     display_dashboard()
