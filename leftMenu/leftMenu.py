import streamlit as st  # Importing Streamlit for building the web application
import pandas as pd  # Importing pandas for data manipulation and analysis
from databaseConnection import mydb  # Importing the database connection module
import streamlit.components.v1 as components  # Importing Streamlit components for custom functionalities

# Establish a connection to the database using a custom function from the databaseConnection module
engine = mydb()

# Database credentials and configuration settings
ipAddress = "10.202.2.22"  # The IP address of the database server
port = "80"                 # The port number to connect to the database
database = "Infeed700"     # The name of the database to be accessed
ReportServerName = "ReportServer"  # The name of the report server
username = "icm\\ndasilva" # Username for database authentication
password = "1984Icm022*"   # Password for database authentication
reportRDLname = "Intake"   # The name of the report to be generated

# Dictionary to map report types to their corresponding header values
headers = {"Intake": 1, "Blending": 2, "Press": 3}
# Dictionary to map specific reports to their corresponding values
reports = {"Intake": 1, "IntakeTip": 1, "Blending": 2, "Press Summary": 3}

def LeftMenu():
    # Function to create a left sidebar menu for report navigation

    # Load a CSS file for custom styling of the Streamlit app
    def local_css(file_name):
        # Open and read the specified CSS file
        with open(file_name) as f:
            # Inject the CSS styles into the Streamlit app using markdown
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Call the local_css function to load styles from "style.css"
    local_css("leftMenu\style.css")

    # Create a sidebar for navigation
    with st.sidebar:
        # Iterate over the headers dictionary to create expandable sections in the sidebar
        for header, valor in headers.items():
            with st.expander(header, expanded=False):  # Create an expandable section for each header
                # Iterate over the reports dictionary to list reports under the corresponding header
                for report, valor2 in reports.items():
                    # Check if the report's value matches the current header's value
                    if valor2 == valor:
                        # Create a clickable link for the report using HTML within markdown
                        st.markdown(f"""
                            <a target="_self" class="sidebar-item" href="http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{report}&rs:Command=Render">{report} <span>›</span></a>
                        """, unsafe_allow_html=True)  # Render the report link, allowing HTML rendering
