import streamlit as st

def leftMenu_custom_css():
    st.markdown("""
        <style>
            /* Modern style for the sidebar menu */
            .sidebar-menu {
                display: flex;
                flex-direction: column;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 15px;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
                border: 1px solid #f0f0f0;
                margin-top: 20px;
            }
            .sidebar-item {
                padding: 14px 20px;
                text-align: left;
                text-decoration: none;
                color: #333;
                font-size: 18px;
                font-family: 'Helvetica Neue', sans-serif;
                transition: all 0.3s ease;
                border-radius: 12px;
                margin-bottom: 12px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            }
            .sidebar-item:hover {
                background-color: #e3f2fd;
                color: #007BFF;
                box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
                transform: translateY(-2px);
            }
            .sidebar-item:active {
                background-color: #007BFF;
                color: white;
                transform: translateY(0);
            }
            /* Style for icons */
            .sidebar-item span {
                font-size: 20px;
                color: #007BFF;
                transition: color 0.3s ease;
            }
            .sidebar-item:hover span {
                color: #0056b3;
            }
        </style>
    """, unsafe_allow_html=True)
