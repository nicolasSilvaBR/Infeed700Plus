import streamlit as st


def leftMenu_custom_css():    
        
        st.markdown("""
        <style>
            /* Modern style for the sidebar menu */
            .sidebar-menu {
                display: flex;
                flex-direction: column;
                padding: 15px;
                background-color: #ffffff;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border: 1px solid #eee;
            }
            .sidebar-item {
                padding: 12px;
                text-align: left;
                text-decoration: none;
                color: #333;
                font-size: 18px;
                font-family: 'Helvetica Neue', sans-serif;
                transition: all 0.3s ease;
                border-radius: 10px;
                margin-bottom: 10px;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            .sidebar-item:hover {
                background-color: #e3f2fd;
                color: #007BFF;
                transform: scale(1.02);
            }
            .sidebar-item:active {
                background-color: #007BFF;
                color: white;
            }
            /* Style for icons */
            .sidebar-item span {
                font-size: 20px;
                color: #007BFF;
            }
        </style>
    """, unsafe_allow_html=True)
