import streamlit as st

def leftMenu_custom_css():
    st.markdown("""
        <style>
            /* Modern style for the sidebar menu */
            
            /* Estilizando o contêiner principal do menu lateral */
            .sidebar-menu {
                display: flex; /* Usando flexbox para organizar o layout em coluna */
                flex-direction: column;
                padding: 20px; /* Espaçamento interno do menu */
                background-color: #ffffff; /* Cor de fundo branca */
                border-radius: 15px; /* Bordas arredondadas para suavizar o design */
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); /* Sombra para dar uma sensação de profundidade */
                border: 1px solid #f0f0f0; /* Borda clara ao redor do menu */
                margin-top: 20px; /* Distância superior para separar do topo */
            }

            /* Estilo para cada item do menu */
            .sidebar-item {
                padding: 14px 20px; /* Espaçamento interno para os itens do menu */
                text-align: left; /* Alinhamento do texto à esquerda */
                text-decoration: none; /* Removendo sublinhado dos links */
                color: #333; /* Cor do texto padrão (cinza escuro) */
                font-size: 18px; /* Tamanho da fonte */
                font-family: 'Helvetica Neue', sans-serif; /* Fonte utilizada */
                transition: all 0.3s ease; /* Transição suave ao interagir com o item */
                border-radius: 12px; /* Bordas arredondadas para os itens do menu */
                margin-bottom: 12px; /* Espaçamento entre os itens */
                display: flex; /* Flexbox para organizar o conteúdo dentro do item */
                align-items: center; /* Alinhamento vertical centralizado */
                justify-content: space-between; /* Espaço entre o texto e os ícones */
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); /* Sombra leve em cada item */
            }

            /* Efeito ao passar o mouse sobre o item do menu */
            .sidebar-item:hover {
                background-color: #e3f2fd; /* Cor de fundo ao passar o mouse (azul claro) */
                color: #007BFF; /* Cor do texto ao passar o mouse (azul escuro) */
                box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2); /* Sombra mais pronunciada para destaque */
                transform: translateY(-2px); /* Efeito de leve elevação ao passar o mouse */
            }

            /* Efeito ao clicar no item do menu */
            .sidebar-item:active {
                background-color: #007BFF; /* Fundo azul ao clicar */
                color: white; /* Texto branco ao clicar */
                transform: translateY(0); /* Remove a elevação para simular o "pressionar" */
            }

            /* Estilo para os ícones dentro dos itens do menu */
            .sidebar-item span {
                font-size: 20px; /* Tamanho dos ícones */
                color: #007BFF; /* Cor padrão dos ícones (azul) */
                transition: color 0.3s ease; /* Transição suave da cor ao interagir */
            }

            /* Mudar a cor dos ícones ao passar o mouse */
            .sidebar-item:hover span {
                color: #0056b3; /* Cor dos ícones ao passar o mouse (azul mais escuro) */
            }
        </style>
    """, unsafe_allow_html=True)
