# Arquivo style.py

menu_styles = {
    # Estilos gerais do container que envolve o menu
    "container": {
        "padding": "0px!important",  # Espaçamento interno do container (bordas)
        "background-color": "#ffffff",  # Cor de fundo do menu
        "border": "0px solid #e0e0e0",  # Borda leve ao redor do menu
        "border-radius": "0px",  # Bordas arredondadas
        "box-shadow": "0 2px 8px rgba(0, 0, 0, 0.1)",  # Sombra leve para profundidade
        "width": "350px",  # Largura do menu
        "max-width": "100%",  # Largura máxima para responsividade
        "font-family": "Segoe UI",  # Fonte utilizada no menu
        "margin": "0px auto",  # Centraliza o menu com margem superior e inferior
        "transition": "all 0.3s ease-in-out",  # Transição suave para qualquer mudança de estilo
        "opacity": "0.95",  # Define a opacidade do container
        "backdrop-filter": "blur(5px)",  # Efeito de desfoque no fundo (moderno e clean)
        # "background-image": "url('path/to/image.jpg')",  # Exemplo para adicionar imagem de fundo
        # "background-size": "cover",  # Faz a imagem de fundo cobrir todo o container
        "overflow": "hidden",  # Garante que nenhum conteúdo transborde fora do container
        "display": "flex",  # Utiliza Flexbox para alinhamento interno
        # "flex-direction": "column",  # Alinha itens em coluna (opcional para menus verticais)
        # "justify-content": "center",  # Centraliza itens no eixo vertical (opcional)
        # "align-items": "center",  # Centraliza itens no eixo horizontal (opcional)
        # "transform": "scale(1)",  # Preparado para efeitos de transformação (zoom)
        # "hover": {  
        #     "transform": "scale(1.05)",  # Efeito de zoom suave ao passar o mouse
        #     "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.15)"  # Aumenta a sombra ao passar o mouse
        # }
    },
    
    # Estilos dos ícones exibidos ao lado de cada item de menu
    "icon": {
        "color": "#818274",  # Cor padrão dos ícones
        "font-size": "20px",  # Tamanho do ícone
        "transition": "color 0.3s ease",  # Transição suave para mudança de cor ao selecionar
    },
    
    # Estilos dos links de navegação (itens do menu)
    "nav-link": {
        "font-size": "18px",  # Tamanho da fonte dos links
        "text-align": "left",  # Alinhamento do texto
        "margin": "10px 0",  # Espaçamento vertical entre os links
        "padding": "10px 15px",  # Espaçamento interno dos links
        "border-radius": "5px",  # Bordas arredondadas dos links
        "transition": "background-color 0.3s ease, color 0.3s ease",  # Transição suave para mudanças de cor
        "cursor": "pointer",  # Exibe o cursor de ponteiro ao passar sobre os links
        "font-weight": "normal",  # Peso da fonte (normal para itens não selecionados)
    },
    
    # Estilos aplicados ao link selecionado (ativo)
    "nav-link-selected": {
        "background-color": "#10454F",  # Cor de fundo do item selecionado
        "color": "white",  # Cor do texto do item selecionado
        "font-weight": "bold",  # Deixa o texto em negrito para destaque
    },
    
    # Estilos ao passar o mouse sobre um link (hover)
    "nav-link:hover": {
        "background-color": "rgba(190, 217, 91, 0.1)",  # Cor de fundo ao passar o mouse (efeito hover)
        "color": "#0056b3",  # Cor do texto ao passar o mouse
    },
    
    # Estilos do ícone quando o item está selecionado
    "icon-selected": {
        "color": "white",  # Cor do ícone do item selecionado (fica branco)
    }
}
