import streamlit as st
from streamlit_option_menu import option_menu
from styles import menu_styles  # Importando os estilos do arquivo style.py

# Definição dos headers e relatórios
headers = {1: "Intake", 2: "Blending", 3: "Press"}
reports = {
    1: [["Intakes", "Intake"], ["Intake Tips", "TipBreakdown"]],
    2: [["Blending / Batching", "Batch"], ["Blending / Run", "BatchByRunNumber"]]
}

def LeftMenu():
    with st.sidebar:
        # Menu de opções principal
        selectedMenu = option_menu(
            menu_title="Infeed700",
            menu_icon="reception-4",
            options=["Dashboards", "SSRS Reports"],
            icons=["pie-chart-fill", "grid-3x3-gap-fill"],
            default_index=0,
            styles=menu_styles  # Aplicando os estilos importados
        )

        # Criando a opção para o menu de SSRS Reports
        if selectedMenu == "SSRS Reports":
            for headerskey, headerName in headers.items():
                with st.expander(headerName, expanded=False):
                    report_option = option_menu(
                        menu_title=None,
                        menu_icon="reception-4",
                        options=[report[0] for report in reports[headerskey]],
                        icons=["table"] * len(reports[headerskey]),
                        default_index=0,
                        key=headerName,
                        styles=menu_styles  # Aplicando os estilos
                    )

                    for report in reports[headerskey]:
                        if report[0] == report_option:
                            st.session_state['selected_report'] = report[1]

# Chama a função para exibir o menu
LeftMenu()
