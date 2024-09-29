import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# Read the content of the README.md file
with open('README.md', 'r') as file:
    readme_text = file.read()

# Read the content of the .streamlit/secrets.toml file
with open('.streamlit/secrets.toml', 'r') as file:
    secrets_toml = file.read()

# Read the content of the requirements.txt file
with open('requirements.txt', 'r') as file:
    requirements_txt = file.read()

# Read the content of the main.py file
with open('main.py', 'r') as file:
    main_py_code = file.read()

# Read the content of the leftMenu/leftMenu.py file
with open('leftMenu/leftMenu.py', 'r') as file:
    left_menu_code = file.read()

# Read the content of the leftMenu/expanderStyle.css file
with open('leftMenu/expanderStyle.css', 'r') as file:
    expander_style_css = file.read()

# Read the content of the styles.py file
with open('styles.py', 'r') as file:
    styles_py = file.read()

# Read the content of the setup.bat file
with open('setup.bat', 'r') as file:
    setup_bat_code = file.read()

# Read the contents of config.toml into the streamlit_config variable
with open('.streamlit/config.toml', 'r') as file:  # Ensure the path is correct
    streamlit_config = file.read()

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
                 "Expander Style CSS"],  # Incluindo Setup.bat
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
    st.title(".streamlit/config.toml")
    st.code(streamlit_config, language='toml')

elif selected == "Requirements.txt":
    st.title("requirements.txt")
    st.code(requirements_txt, language='plaintext')

elif selected == "Styles.py":
    st.title("styles.py")
    st.code(styles_py, language='python')

elif selected == "Setup.bat":
    st.title("setup.bat")
    st.code(setup_bat_code, language='batch')