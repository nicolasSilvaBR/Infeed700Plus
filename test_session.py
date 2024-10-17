import streamlit as st
from streamlit_option_menu import option_menu
from utilities import load_local_css, display_footer, get_header_dict, get_report_dict  # Import custom functions from utilities.py
from database_connection import mydb
from styles import menu_styles  # Import custom styles for the menu

# Initialize the database connection
engine = mydb()

# Function to clear specific session state key
def delete_key():
    if 'select_report_options' in st.session_state:
        st.session_state['select_report_options']        
    return

with st.sidebar:

    # Get headers and reports from the database
    headers = get_header_dict(engine)
    reports = get_report_dict(engine)

    # Create a list to store the names of the headers
    header_list = [headerName for headerKey, headerName in headers.items()]

    # Initialize session state for report options if not present
    if 'select_report_options' not in st.session_state:
        st.session_state['select_report_options'] = None

    # Selectbox to select the category (header)
    selected_header = st.selectbox(
        label="Choose a Category...",
        options=header_list,
        key="select_header_options",
        placeholder="Choose a Category...",
        on_change= delete_key,     
        index=None   
    )

    # Create a list to store the reports for the selected header
    report_list = []  # For displaying report options
    rdl_report_list = []  # For storing the SSRS report names

    # Populate report_list and rdl_report_list based on the selected header
    for headersKey, headerName in headers.items():
        if headersKey in reports and headerName == selected_header:
            for report in reports[headersKey]:
                report_list.append(report[0])
                rdl_report_list.append(report[1])

    # If there are report options, show the report option menu
    if report_list:
        reports_option = option_menu(
            menu_title=f"{selected_header} Reports",
            menu_icon="list",
            icons=["file-text"] * len(report_list),
            default_index=0,
            options=report_list,
            key="select_report_options"           
            
        )
        
        st.session_state['select_report_options']

        # Store the selected report (SSRS report name) in session state
        selected_report = rdl_report_list[report_list.index(reports_option)]
        st.session_state['selected_report'] = selected_report

    else:
        st.write("No reports available for this category.")
        st.session_state['selected_report'] = None

# Display the selected header and report
st.write(f"Selected Header: {selected_header}")

if st.session_state['selected_report']:
    st.write(f"Report Selected: {st.session_state['selected_report']}")
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
