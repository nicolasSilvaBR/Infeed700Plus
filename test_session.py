import streamlit as st
from streamlit_option_menu import option_menu

# Definir as opções de relatórios
options = ["Relatório 1", "Relatório 2", "Relatório 3"]

options2 = ["Relatório 4", "Relatório 5", "Relatório 6"]


# Inicializar o estado da sessão para garantir que haja um espaço para o valor selecionado
if 'report_option' not in st.session_state:
    st.session_state['report_option'] = None

# Criar o primeiro menu de opções
report_option1 = option_menu(
    menu_title="Menu 1",
    menu_icon="reception-4",
    options=options,
    icons=["table"] * len(options),
    default_index=0,  # Não predefinir uma opção
    key=f"option_menu_1",  # Chave única para o primeiro menu
    
)

# Criar o segundo menu de opções
report_option2 = option_menu(
    menu_title="Menu 2",
    menu_icon="reception-4",
    options=options2,
    icons=["table"] * len(options2),
    default_index=0,  # Não predefinir uma opção
    key=f"option_menu_2",  # Chave única para o segundo menu  
)



# Verificar qual menu foi usado para fazer a seleção e atualizar o session_state
if report_option1 != st.session_state['report_option']:
    st.session_state['report_option'] = report_option1
elif report_option2 != st.session_state['report_option']:
    st.session_state['report_option'] = report_option2

# Lógica para exibir o relatório selecionado
if st.session_state['report_option']:
    st.write(f"Você selecionou: {st.session_state['report_option']}")
else:
    st.write("Nenhum relatório selecionado.")
