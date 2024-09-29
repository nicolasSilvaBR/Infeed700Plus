import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# Textos e códigos para as seções
Overview = '''\
The Infeed700 application is a sophisticated interactive platform developed by **ICMC Solutions** utilizing **Streamlit**. This project aims to transition from the existing SSRS reporting system to a new solution using Python Streamlit. The new system will enhance interactivity, visual quality, and ease of report development and maintenance. 

Designed to serve multiple clients, Infeed700 prioritizes user experience with its responsive interface and intuitive navigation. Users can effortlessly switch between different reporting modules, including "Intake", "Blending", and "Press", allowing for dynamic data analysis tailored to their specific needs.

### Key Features:
- **User-Friendly Interface**: The application’s layout is designed for ease of use, minimizing the learning curve for new users.
- **Data Visualization**: With integrated SSRS reports, users can visualize data effectively, leading to informed decision-making.
- **Customizable Reports**: The application supports various report types, enabling tailored data presentations for different operational needs.

The project will be executed in multiple phases, with defined responsibilities across various teams. The solution will be implemented on-premises, and existing stored procedures will be used to maintain continuity with the current system. 

Infeed700 is not only a tool for data visualization but also a comprehensive solution for business intelligence, providing valuable insights through advanced data analytics and reporting capabilities.
'''


readme_text = '''\
## Overview

The Infeed700 application is an interactive platform developed by **ICMC Solutions** using **Streamlit**. It provides embedded dashboards and SSRS (SQL Server Reporting Services) reports, allowing users to access and visualize data efficiently in an on-premises environment. This application is designed to serve multiple clients, offering a user-friendly and responsive interface.

## Installation Instructions

Follow these steps to set up the Infeed700 application on your local machine:

1. **Download Python**:
   - Visit the official Python website: [Download Python](https://www.python.org/downloads/)
   - Download the latest version of Python (make sure to choose the installer compatible with your operating system).
   - Run the installer and make sure to check the box that says **"Add Python to PATH"** during installation.

2. **Download and Extract the Application Files**:
   - Download the Infeed700 application files, which are provided as a `.zip` or `.rar` archive.
   - Extract the contents of the archive to a local directory of your choice.

3. **Navigate to the Application Directory**:
   - Open a command prompt window (you can do this by searching for "cmd" in the Windows search bar).
   - Use the `cd` command to change to the directory where you extracted the application files. For example:
     ```
     cd path\to\your\extracted\folder
     ```

4. **Run the Setup Batch File**:
   - In the command prompt, execute the `setup.bat` file by typing:
     ```
     setup.bat
     ```
   - This will install all the required dependencies and start the Streamlit application.

5. **Access the Application**:
   - After running the setup, the Streamlit application should automatically launch in your web browser. If it doesn't, you can manually open your browser and go to `http://localhost:8501`.

By following these steps, you will have the Infeed700 application set up and running on your local machine. If you encounter any issues, please refer to the troubleshooting section of this documentation or seek assistance from your IT support team.
'''

project_structure = '''\
Infeed700/
│
├── images/                     # Directory for images and icons
│   ├── home.svg                # SVG icon for the sidebar
│   └── (other images and icons)
│
├── LeftMenu/                   # Directory for left menu-related files
│   ├── leftMenu.py             # Contains the logic for the left menu
│   ├── expanderStyle.css        # Custom styles for the left menu
│
├── styles.py                   # Custom styles for the menu
│
├── main.py                     # Main entry point for the Streamlit application
│
├── requirements.txt             # List of dependencies for the application
│
├── setup.bat                    # Batch file for setting up the environment
│
└── .streamlit/
    └── secrets.toml            # Secrets for database connection
    └── config.toml             # Streamlit Configuration Settings [theme][server]
'''

dependency_support = '''\
- **Streamlit**: [Streamlit Documentation](https://docs.streamlit.io/)
- **Pandas**: [Pandas Documentation](https://pandas.pydata.org/)
- **NumPy**: [NumPy Documentation](https://numpy.org/)
- **SQLAlchemy**: [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- **PyODBC**: [PyODBC Documentation](https://github.com/mkleehammer/pyodbc/wiki)
- **Matplotlib**: [Matplotlib Documentation](https://matplotlib.org/)
- **Plotly**: [Plotly Documentation](https://plotly.com/)
- **Requests**: [Requests Documentation](https://docs.python-requests.org/)
- **Altair**: [Altair Documentation](https://altair-viz.github.io/)
- **Openpyxl**: [Openpyxl Documentation](https://openpyxl.readthedocs.io/en/stable/)
'''

secrets_toml = '''\
# .streamlit/secrets.toml

[mydb]
dialect = "mssql"  # Database dialect, in this case, MS SQL Server
driver = "ODBC Driver 17 for SQL Server"  # Specify the ODBC driver
username = "sa"  # The SQL Server username (replace with your actual credentials)
password = "1984Icm000"  # The password for the SQL Server
host = "127.0.0.1"  # IP address of the SQL Server, 127.0.0.1 for localhost
port = "1433"  # Default SQL Server port
database = "infeed700ECV"  # Name of the target database
instance = "MSSQLSERVER"  # Optional: Include the instance name if needed

# Example for adding another environment or service
[mydb_dev]
dialect = "mssql"
driver = "ODBC Driver 17 for SQL Server"
username = "dev_user"
password = "dev_password"
host = "192.168.1.100"  # Example for a development server IP
port = "1433"
database = "infeed700_DEV"
instance = "MSSQLSERVER_DEV"

# Another example for external APIs
[api_service]
api_key = "YOUR_API_KEY"
api_url = "https://api.example.com/"
'''
config_toml = '''\
# Streamlit Configuration Settings

[server]
port = 8501  # The port on which the Streamlit app will run

[theme]
primaryColor = "#F39C12"  # Primary color used in the app
backgroundColor = "#F0F0F5"  # Background color for the app
secondaryBackgroundColor = "#E0E0EF"  # Secondary background color
textColor = "#262730"  # Color of the text in the app
font = "Segoe UI"  # Font style used throughout the app
'''

requirements_txt = '''\
streamlit>=1.38.0
pandas>=2.1.0
numpy>=1.25.0
altair>=5.0.0
openpyxl>=3.1.0
sqlalchemy>=2.0.0
pyodbc>=4.0.0
matplotlib>=3.9.2
plotly>=5.24.1
requests==2.32.3  # Corrigido para usar '=='
requests_ntlm>=1.3.0
streamlit-option-menu>=0.3.13
'''

main_py_code = '''\
import streamlit as st
from leftMenu.leftMenu import LeftMenu
import requests
from requests_ntlm import HttpNtlmAuth

# Set the page layout for the Streamlit app
st.set_page_config(layout="wide")

# Display the left menu for navigation
LeftMenu()

# Initialize session state for the selected report if not already set
if 'selected_report' not in st.session_state:
    st.session_state['selected_report'] = "Intake"

reportRDLname = st.session_state['selected_report']

# Database credentials and configuration settings
ipAddress = "10.202.2.22"
port = "80"
database = "Infeed700"
ReportServerName = "ReportServer"
username = "icm\\ndasilva"
password = "1984Icm022*"

# Construct the URL for the SSRS report
ssrs_url = f"http://{ipAddress}:{port}/{ReportServerName}/Pages/ReportViewer.aspx?%2f{database}%2f{reportRDLname}&rs:Command=Render&MinDate=2024-08-01"

# Make the request to the SSRS report using NTLM authentication
try:
    response = requests.get(ssrs_url, auth=HttpNtlmAuth(username, password), timeout=10)

    # Check if the request was successful
    if response.status_code == 200:
        report_url = f"{ssrs_url}&rs:Embed=true&rc:Parameters=Collapsed"
        # Create an iframe to display the report
        iframe_code = f"""
        <iframe width="100%" height="100%" style="min-height: 150vh;" src="{report_url}" frameborder="0" allowfullscreen></iframe>
        """
        st.components.v1.html(iframe_code, height=900, scrolling=False)
    else:
        st.error(f"Error accessing the report: {response.status_code}")

# Handle specific connection errors and provide user guidance
except requests.exceptions.ConnectTimeout:
    error_message = """
    **Connection Timeout Error**

    Possible reasons for this issue:
    1. Verify that the provided IP address `10.202.2.22` is correct and reachable.
    2. Ensure that the port `80` is open and accessible on the target server.
    3. Double-check the database name `Infeed700` in your report URL.
    4. Go to the `.secrets.toml` file and verify that the credentials (username and password) are correctly configured.

    Please resolve these potential issues and try again.
    """
    st.error(error_message)

# Handle other request-related errors
except requests.exceptions.RequestException as e:
    st.error(f"Error accessing the report: {e}")
'''

left_menu_code = '''\
import streamlit as st
from streamlit_option_menu import option_menu
from styles import menu_styles  # Import custom styles
from utilities import load_svg  # Import function to load SVGs
import os  # For file path manipulation

# Define headers and reports for the menu
headers = {1: "Intake", 2: "Blending", 3: "Press"}
reports = {
    1: [["Intakes", "Intake"], ["Intake Tips", "TipBreakdown"]],
    2: [["Blending / Batching", "Batch"], ["Blending / Run", "BatchByRunNumber"]]
}

def LeftMenu():
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    local_css("leftMenu/expanderStyle.css")   
    svg_file_path = os.path.join("images", "home.svg")

    with st.sidebar:
        with st.expander(label='', expanded=True):
            svg_icon = load_svg(svg_file_path)  

            selectedMenu = option_menu(
                menu_title="Infeed700",
                menu_icon="bar-chart-fill",
                options=["Dashboards", "SSRS Reports"],
                icons=["pie-chart-fill", "grid-3x3-gap-fill"],
                default_index=0,
                styles=menu_styles
            )

        if selectedMenu == "SSRS Reports":
            for headerskey, headerName in headers.items():
                if headerskey in reports:
                    with st.expander(headerName, expanded=False):
                        report_option = option_menu(
                            menu_title=None,
                            menu_icon="reception-4",
                            options=[report[0] for report in reports[headerskey]],
                            icons=["table"] * len(reports[headerskey]),
                            default_index=0,
                            key=headerName,
                            styles=menu_styles
                        )

                        for report in reports[headerskey]:
                            if report[0] == report_option:
                                st.session_state['selected_report'] = report[1]
'''

expander_style_css = '''\
/* Styling for the main container of the sidebar menu */
.sidebar-menu {
    display: flex;  
    flex-direction: column;  
    padding: 0px!important;  
    background-color: #ffffff;  
    border: 0px solid #e0e0e0;  
    border-radius: 8px;  
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);  
    width: 300px;  
    max-width: 100%;  
    margin: 0px auto;  
    transition: all 0.3s ease-in-out;  
    opacity: 0.95;  
    backdrop-filter: blur(5px);  
}
'''

styles_py = '''\
menu_styles = {
    "container": {
        "padding": "0px!important",
        "background-color": "#ffffff",
        "border": "0px solid #e0e0e0",
        "border-radius": "0px",
        "box-shadow": "0 2px 8px rgba(0, 0, 0, 0.1)",
        "width": "350px",
        "max-width": "100%",
        "font-family": "Segoe UI",
        "margin": "0px auto",
        "transition": "all 0.3s ease-in-out",
        "opacity": "0.95",
        "backdrop-filter": "blur(5px)",
        "overflow": "hidden",
        "display": "flex",
        "flex-direction": "column",
        "justify-content": "center",
        "transform": "scale(1)",
        "hover": {  
            "transform": "scale(5.05)",
            "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.15)"
        }
    },
    
    "icon": {
        "color": "#818274",
        "font-size": "20px",
        "transition": "color 0.3s ease",
        "hover": {
            "color": "#f39c12",
            "transform": "scale(1.2)",
        }
    },
    
    "nav-link": {
        "font-size": "12px",
        "text-align": "left",
        "margin": "10px 0",
        "padding": "10px 15px",
        "border-radius": "5px",
        "transition": "background-color 0.3s ease, color 0.3s ease",
        "cursor": "pointer",
        "font-weight": "normal",
        "hover": {
            "color": "#f39c12",
            "transform": "scale(1.2)",
        }
    },
    
    "nav-link-selected": {
        "background-color": "#10454F",
        "color": "white",
        "font-weight": "bold",
    },
    
    "nav-link:hover": {
        "background-color": "rgba(190, 217, 91, 0.1)",
        "color": "#0056b3",
    },
    
    "icon-selected": {
        "color": "white",
    }
}
'''
setup_bat_code = '''\
@echo off

:: Save the current directory
set ORIGINAL_DIR=%CD%

:: Change to the directory where the script is located
cd /d %~dp0

:: Check if Python is installed
python --version >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed or not found in the PATH.
    echo Please install Python from https://www.python.org.
    pause
    exit /b 1
) else (
    echo Python is already installed.
)

:: Install the dependencies globally
echo Installing dependencies globally...
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo Failed to install dependencies. Please check the requirements.txt file.
    pause
    exit /b 1
)

:: Ensure the directory contains main.py
if not exist "main.py" (
    echo main.py does not exist in the current directory.
    pause
    exit /b 1
)

:: Run Streamlit application
echo Starting Streamlit application...
start "" cmd /k "streamlit run main.py"

:: Return to the original directory
cd /d %ORIGINAL_DIR%

pause
'''


# Configuração do menu lateral usando `streamlit_option_menu` no sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Documentation",  # Título do menu
        options=["Overview", 
                 "README.md", 
                 "Project Structure", 
                 "Dependency Support", 
                 "Requirements.txt", 
                 "Setup.bat",
                 "Secrets.toml",
                 "Config.toml",
                 "Main.py", 
                 "LeftMenu.py", 
                 "Expander Style CSS",                   
                 ],  # Incluindo Setup.bat
        icons=["book", 
               "file-text", 
               "folder", 
               "link", 
               "filetype-txt", 
               "windows", 
               "filetype-py",
               "filetype-py",
               "filetype-py", 
               "filetype-py", 
               "filetype-css"],  # Ícones
        menu_icon="list",  # Ícone do menu
        default_index=0,  # Índice padrão selecionado
    )

# Exibe o conteúdo correspondente com base na seleção
if selected == "Overview":
    st.title("Overview")
    st.markdown(Overview)

elif selected == "README.md":
    st.title("README.md")
    st.markdown(readme_text)

elif selected == "Project Structure":
    st.title("Project Structure")
    st.code(project_structure, language='plaintext')

elif selected == "Dependency Support":
    st.title("Dependency Support")
    st.markdown(dependency_support)

elif selected == "Main.py":
    st.title("main.py")
    st.code(main_py_code, language='python')

elif selected == "LeftMenu.py":
    st.title("leftMenu/leftMenu.py")
    st.code(left_menu_code, language='python')

elif selected == "Expander Style CSS":
    st.title("leftMenu/expanderStyle.css")
    st.code(expander_style_css, language='css')

elif selected == "Secrets.toml":
    st.title(".streamlit/secrets.toml")
    st.code(secrets_toml, language='toml')

elif selected == "Config.toml":
    st.title(".streamlit/Config.toml")
    st.code(config_toml, language='toml')

elif selected == "Requirements.txt":
    st.title("requirements.txt")
    st.code(requirements_txt, language='plaintext')

elif selected == "Styles.py":
    st.title("styles.py")
    st.code(styles_py, language='python')

elif selected == "Setup.bat":
    st.title("setup.bat")
    st.code(setup_bat_code, language='batch')
