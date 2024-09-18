import streamlit as st
import pandas as pd
from databaseConnection import mydb
import streamlit.components.v1 as components
from leftMenu_custom_css import leftMenu_custom_css  # Custom CSS for left menu

# Establish database connection
engine = mydb()

# Function to create the sidebar with navigation links and logo
def LeftMenu():
    # Sidebar image (logo)
    st.sidebar.image("icmLogo.png", use_column_width=False, width=100)

    # Function to create the navigation menu in the sidebar
    def create_sidebar_menu():
        st.sidebar.markdown("""
        <div class="sidebar-menu">
            <a target="_self" class="sidebar-item" href="?page=intake">Intake <span>›</span></a>
            <a target="_self" class="sidebar-item" href="?page=intakeDashboard">Intake Dashboard <span>›</span></a>
            <a target="_self" class="sidebar-item" href="?page=intakeTips">Intake Tips <span>›</span></a>
        </div>
        """, unsafe_allow_html=True)

    # Inject custom CSS for the menu
    leftMenu_custom_css()

    # Display the sidebar menu
    create_sidebar_menu()
