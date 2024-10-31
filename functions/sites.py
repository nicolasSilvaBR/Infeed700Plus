import pandas as pd
import streamlit as st

def IsMultiSiteEnabled(engine):
    # Execute the stored procedure and retrieve the returned value
    storedProcedure = "EXEC [Report].[SSRS_IsMultiSiteEnabled]"
    IsMultiSiteEnabled = pd.read_sql(storedProcedure, engine)

    # Access the first returned value directly using 'iat' first rows first column
    is_multi_site_enabled = IsMultiSiteEnabled.iat[0, 0]  # Gets the first cell value

    if 'is_multi_site_enabled' not in st.session_state:
        st.session_state['is_multi_site_enabled'] = is_multi_site_enabled
    if 'site_id_list' not in st.session_state:
        st.session_state['site_id_list'] = '0'

    # Check if the value is 1 (True) or not
    if is_multi_site_enabled == '1':          
        storedProcedure = "EXEC [Report].[SSRS_ListSites]"
        listSites = pd.read_sql(storedProcedure, engine)  
        # Configuração do st.radio para seleção
        site_desc = st.selectbox("Site", listSites['SiteDesc'])

        # Encontrando o SiteId correspondente
        selected_site_id = listSites[listSites['SiteDesc'] == site_desc]['SiteId'].values[0]

        # Armazenando o SiteId na sessão
        st.session_state['selected_site_id'] = selected_site_id
        
    else:
        st.session_state['is_multi_site_enabled'] = False
        st.session_state['selected_site_id'] = '0'
        
    

