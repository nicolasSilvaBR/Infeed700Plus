import streamlit as st
from streamlit_option_menu import option_menu
from utilities import get_header_dict, get_report_dict  # Import custom functions from utilities.py
from database_connection import mydb
import styles

# Initialize the database connection with error handling
try:
    engine = mydb()
except Exception as e:
    st.error("Error connecting to the database. Please try again later.")
    st.stop()  # Stop execution if the database connection fails

# Function to clear specific session state keys when a category is changed
def update_report_selection():
    st.session_state['selected_report'] = None
    st.session_state['select_report_options'] = None

# Function to create and display the option menu based on the selected header
def option_menu_function(report_list):
    # Display the option menu inside the sidebar without using manual_select
    reports_option = option_menu(
        menu_title=None,
        menu_icon="list",
        icons=["box-arrow-in-right"] * len(report_list),
        default_index=0,
        options=report_list,
        key="select_report_options",
        styles={
                "container": styles.menu_styles["container"], # styles.py sets the container style
                "icon": styles.menu_styles["icon"],
                "nav-link": styles.menu_styles["nav-link"],
                "nav-link-selected": styles.menu_styles["nav-link-selected"],
                "icon-selected": styles.menu_styles["icon-selected"], 
        }
    )
    return reports_option

# Initialize session state variables if not already present
st.session_state.setdefault('select_header_options', None)
st.session_state.setdefault('selected_report', None)
st.session_state.setdefault('select_report_options', None)
st.session_state['is_python_enabled'] = None

# Sidebar: Select a category (header) and display the report options
with st.sidebar:
    # Attempt to fetch headers and reports with error handling
    try:
        headers = get_header_dict(engine)  # Should return a dictionary
        reports = get_report_dict(engine)  # Should return a dictionary
    except Exception as e:
        st.error("Error fetching data from the database. Please try again later.")
        st.stop()

    # Check if headers and reports are empty
    if not headers or not reports:
        st.error("No data available. Please check your database configuration.")
        st.stop()

    # Create a list of header names
    header_list = list(headers.values())

    # Selectbox to select the category (header)
    selected_header = st.selectbox(
        label="Choose a Category...",
        options=header_list,
        key="select_header_options",
        placeholder="Choose a Category...",
        index=0,    
        on_change=update_report_selection    
    )

    # Lists to store report names and corresponding SSRS file names for the selected header
    report_list = []
    rdl_report_list = []
    is_python_enabled = []

    # Populate report_list and rdl_report_list based on the selected header
    if selected_header:
        for headersKey, headerName in headers.items():
            if headerName == selected_header and headersKey in reports:
                # Ensure 'reports' is accessed correctly using the headersKey
                for report in reports[headersKey]:
                    report_list.append(report[0])
                    rdl_report_list.append(report[1])
                    is_python_enabled.append(report[2])

    # If there are report options, show the report option menu
    if report_list:
        reports_option = option_menu_function(report_list)
        # Update the session state based on the selected option
        if reports_option in report_list:
            st.session_state['selected_report'] = rdl_report_list[report_list.index(reports_option)]
            st.session_state['is_python_enabled'] = is_python_enabled[report_list.index(reports_option)]
    else:
        st.write("No reports available for this category.")
        st.session_state['selected_report'] = None

# Display the selected header and report
st.write(f"Selected Header: {selected_header}")

# Display the selected report or a message if no report is selected
if st.session_state.get('selected_report'):
    st.write(f"Report Selected: {st.session_state['selected_report']}")
    st.write(f"Is Python enabled: {st.session_state['is_python_enabled']}")
else:
    st.write("No report selected.")








          


# headers_option = option_menu(
#     menu_title="Category",
#     options=options,  # Ensure headerName is a list or iterable
#     menu_icon="cast",  # Optional: icon for the menu
#     default_index=0  # Optional: change to None if no default selection is needed
#     )

# Definir as opções de relatórios
# options = ["Relatório 1", "Relatório 2", "Relatório 3"]
# options2 = ["Relatório 4", "Relatório 5", "Relatório 6"]


# # Inicializar o estado da sessão para garantir que haja um espaço para o valor selecionado
# if 'report_option' not in st.session_state:
#     st.session_state['report_option'] = None

# with st.sidebar:

#     # Criar o primeiro menu de opções
#     report_option1 = option_menu(
#         menu_title="Intake",
#         menu_icon="reception-4",
#         options=options,
#         icons=["table"] * len(options),
#         default_index=0,  # Não predefinir uma opção
#         key=f"option_menu_1",  # Chave única para o primeiro menu

#     )

#     # Criar o segundo menu de opções
#     report_option2 = option_menu(
#         menu_title="Bleding",
#         menu_icon="reception-4",
#         options=options2,
#         icons=["table"] * len(options2),
#         default_index=0,  # Não predefinir uma opção
#         key=f"option_menu_2",  # Chave única para o segundo menu
#     )


#     # Verificar qual menu foi usado para fazer a seleção e atualizar o session_state
#     if report_option1 != st.session_state['report_option']:
#         st.session_state['report_option'] = report_option1
#     elif report_option2 != st.session_state['report_option']:
#         st.session_state['report_option'] = report_option2

#     # Lógica para exibir o relatório selecionado
#     if st.session_state['report_option']:
#         st.write(f"Você selecionou: {st.session_state['report_option']}")
#     else:
#         st.write("Nenhum relatório selecionado.")
