import streamlit as st
from database_connection import mydb
import pandas as pd


# Function to load local CSS file
def load_local_css(file_name):
    """Load local CSS for custom styles.
    Args:
        file_name (str): Name of the CSS file to load.       
    
    """
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file '{file_name}' not found.")



# Function to display the footer
def display_footer():
    """Display footer with custom CSS at the bottom of the sidebar."""
    st.markdown(
        """
        <style>
            /* Style for the footer to position it at the bottom of the sidebar */
            .sidebar-content {
                display: flex;
                flex-direction: column;
                height: 100%;
            }
            .footer {
                margin-top: auto;
                padding: 20px 0;
                text-align: center;
                font-size: 12px;
                color: #555;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="footer">
            <p>
                <a href="http://10.202.2.22:8503/" target="_blank">Data Lab</a> | 
                <a href="Http://10.202.2.22:8504/" target="_blank">Support</a> | 
                <a href="https://icmcsl.com/contact/" target="_blank">Contact Us</a> |
                <a href="https://forms.gle/jm3wTqskS1LD2D328" target="_blank">Feedback</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


 # Function to get the header dictionary
def get_header_dict(engine):
    
    sql_query = """
        SELECT
            [HeaderId]
            ,[HeaderDisplayName]    
        FROM [Report].[MenuHeader]
        WHERE IsActive = 1
            AND HeaderId <> 9
        ORDER by [WebHeaderDisplayOrder]  
        """

    df = pd.read_sql_query(sql_query, engine)
    header_dict = df.set_index('HeaderId')['HeaderDisplayName'].to_dict()

    return header_dict
        

 # Function to get the report dictionary
def get_report_dict(engine):

    sql_query = """
        SELECT	
            [HeaderId]
            ,[ReportDisplayName]
            ,[ReportName]
            ,ItemDisplayOrder
        FROM [Report].[MenuItems]
        WHERE IsActive = 1
        ORDER BY  [HeaderId],[ReportDisplayName],[ItemDisplayOrder]
        """

    df = pd.read_sql_query(sql_query, engine)   
    reports_dict = df.groupby('HeaderId')[['ReportDisplayName', 'ReportName']].apply(lambda x: x.values.tolist()).to_dict()

    return reports_dict