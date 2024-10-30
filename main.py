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

config.set_page_config()
    
# Função para carregar e converter CSS
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
    engine = mydb()
    logging.info(f"Database engine: {engine}")

    LeftMenu(engine)
    
    if 'selected_report' not in st.session_state:
        st.session_state['selected_report'] = None
    if 'selected_header' not in st.session_state:
        st.session_state['selected_header'] = None

    # Inicializa 'see_demo' na sessão se ainda não estiver definido
    if 'see_demo' not in st.session_state:
        st.session_state['see_demo'] = False
    
    minDate = st.session_state.get('minDate', pd.to_datetime("2024-10-01")).strftime('%Y-%m-%d')
    maxDate = st.session_state.get('maxDate', pd.to_datetime("2024-10-30")).strftime('%Y-%m-%d')

    def display_ssrs_report():
        """Function to display the SSRS report."""
        try:
            with st.spinner('Running Report...'):
                if 'selected_report' not in st.session_state:
                    st.session_state['selected_report'] = 'Home'  # Default report
                
                reportRDLname = st.session_state['selected_report']    
                embed_ssrs_report(reportRDLname, minDate, maxDate)
        except:
            st.error("An error occurred while loading the report. Verify that the SSRS server is online.") 

    def display_dashboard():
        """Function to display the dashboard content."""
        intake_page(mindate=minDate, maxdate=maxDate)

    # CSS customizado na área principal
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # Se "See Demo" não foi clicado, exibir a home
    if not st.session_state['see_demo']:
        # Carregar a imagem em Base64
        image_path = Path("assets/images/home_header.png")
        if image_path.exists():
            image_base64 = get_base64_image(image_path)
            image_url = f"data:image/png;base64,{image_base64}"
        else:
            st.error("Imagem not found.")
            image_url = ""  # Caso a imagem não seja encontrada

        # Ler e substituir no HTML
        with open("index.html", "r") as file:
            index_html = file.read()
        
        index_html = index_html.replace("assets/images/home_header.png", image_url)
        components.html(index_html, height=1000, scrolling=True)
        
        col_,col1,col_,col_ = st.columns([5,1,4,1])
        with col1:
            if st.button("See Demo"):
                st.session_state['see_demo'] = True  # Define o estado da sessão para 'see_demo'
            
    else:
        # Se "See Demo" foi clicado, exibir apenas o dashboard
        display_dashboard()

    # Fechar div principal
    st.markdown('</div>', unsafe_allow_html=True)

# Ponto de entrada da aplicação
if __name__ == '__main__':
    main()
