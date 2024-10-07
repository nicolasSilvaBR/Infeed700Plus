import streamlit as st

def set_page_config():
    """Set page configuration for Streamlit app."""

    st.set_page_config(
        page_title="Infeed700 Reports",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# Infeed700. Version 1.0 *BETA* ICM CSL"
        }
    )
