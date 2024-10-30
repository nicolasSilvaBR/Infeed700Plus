import functions.config as config
import streamlit as st
from left_menu.left_menu import LeftMenu
from embedded_SSRS import embed_ssrs_report
import pandas as pd
from reports.intake.intake import intake_page
import logging
from database_connection import mydb
import streamlit.components.v1 as components
from pathlib import Path
import base64

# Configuração inicial da página
config.set_page_config()

# Função para carregar e aplicar CSS
def load_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Carregar o CSS personalizado
load_local_css("assets/css/style.css")

# Função para converter imagem em Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def main():
    # Configurações iniciais e log de conexão com o banco de dados
    engine = mydb()
    logging.info(f"Database engine: {engine}")
    LeftMenu(engine)
    
    # Inicializar variáveis de sessão
    if 'selected_report' not in st.session_state:
        st.session_state['selected_report'] = None
    if 'show_report' not in st.session_state:
        st.session_state['show_report'] = False  # Controla a exibição do relatório
    if 'show_content' not in st.session_state:
        st.session_state['show_content'] = False  # Controla a exibição de conteúdo específico (dashboard ou relatório)

    # Datas padrão
    minDate = st.session_state.get('minDate', pd.to_datetime("2024-10-01")).strftime('%Y-%m-%d')
    maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-10-30")).strftime('%Y-%m-%d')

    # Função para exibir o relatório SSRS
    def display_ssrs_report():
        """Exibir o relatório SSRS."""
        try:
            with st.spinner('Running Report...'):
                reportRDLname = st.session_state['selected_report']
                embed_ssrs_report(reportRDLname, minDate, maxDate)
        except Exception as e:
            if st.session_state['selected_report']:
                logging.error(f"Error loading report: {e}")
                st.error("An error occurred while loading the report. Verify that the SSRS server is online.") 
            elif not st.session_state['selected_report']:
                st.write('Choose a Category and Report')

    # Função para exibir o dashboard
    def display_dashboard():
        """Exibir o conteúdo do dashboard."""
        intake_page(mindate=minDate, maxdate=maxDate)

    # Exibir conteúdo principal com base no estado da sessão
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # Atualizar `show_content` e `show_report` com base no relatório selecionado
    if st.session_state['selected_report'] is not None:
        st.session_state['show_report'] = True
        st.session_state['show_content'] = True

    # Exibir a home (index.html) apenas se `show_content` for False
    if not st.session_state['show_content']:
        # Carregar a imagem em Base64
        image_path = Path("assets/images/home_header.png")
        image_url = ""
        if image_path.exists():
            image_base64 = get_base64_image(image_path)
            image_url = f"data:image/png;base64,{image_base64}"
        else:
            st.error("Image not found.")

        # Carregar e exibir HTML da página inicial
        with open("index.html", "r") as file:
            index_html = file.read()
        
        index_html = index_html.replace("assets/images/home_header.png", image_url)
        components.html(index_html, height=1000, scrolling=True)
        
        # Centralizar o botão "See Demo"
        col_left, col_center, col_right = st.columns([5, 1, 5])
        with col_center:
            if st.button("See Demo"):
                st.session_state['show_content'] = True  # Define para mostrar o dashboard
    
    # Se "See Demo" foi clicado ou um cabeçalho de relatório foi selecionado, exibir o conteúdo específico
    else:
        # Mostrar o dashboard se "See Demo" foi clicado e nenhum cabeçalho foi selecionado
        if st.session_state['show_content'] and not st.session_state['show_report']:
            display_dashboard()
        
        # Mostrar o relatório SSRS se um cabeçalho de relatório foi selecionado
        elif st.session_state['show_report']:
            display_ssrs_report()

    # Fechar div principal
    st.markdown('</div>', unsafe_allow_html=True)

# Ponto de entrada da aplicação
if __name__ == '__main__':
    main()
