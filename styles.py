# Arquivo style.py
# The file is used to define the styles of the menu, including the container, links, icons, and selected state.
# The styles are defined in a dictionary, where each key represents a class or ID of an HTML element, and the value is a dictionary of styles to be applied to that element.

# The styles are divided into several sections:
# - container: styles for the container that encloses the menu
# - icon: styles for the icons displayed next to each menu item
# - nav-link: styles for the links (menu items)
# - nav-link-selected: styles for the selected state of the links (menu items)
# - icon-selected: styles for the icon when the item is selected


menu_styles = {
    # Estilos gerais do container que envolve o menu
    "container": {
        "padding": "0px!important",                     # Espaçamento interno do container (bordas)
        "background-color": "#ffffff",                  # Cor de fundo do menu
        "border": "0px solid #e0e0e0",                  # Borda leve ao redor do menu
        "border-radius": "0px",                         # Bordas arredondadas
        "box-shadow": "0 2px 8px rgba(150, 150, 147, 0.5)",   # Sombra leve para profundidade
        "width": "370px",                               # Largura do menu  
        "max-width": "100%",                            # Largura máxima para responsividade
        "font-family": "Segoe UI",                      # Fonte utilizada no menu
        "margin": "0px auto",                           # Centraliza o menu com margem superior e inferior
        "transition": "all 0.3s ease-in-out",           # Transição suave para qualquer mudança de estilo
        "opacity": "1",                              # Define a opacidade do container  
        "backdrop-filter": "blur(5px)",                 # Efeito de desfoque no fundo (moderno e clean)
        # "background-image": "url('path/to/image.jpg')",  # Exemplo para adicionar imagem de fundo
        # "background-size": "cover",                   # Faz a imagem de fundo cobrir todo o container
        "overflow": "hidden",                           # Garante que nenhum conteúdo transborde fora do container
        #"display": "flex",                              # Utiliza Flexbox para alinhamento interno
        "flex-direction": "column",                     # Alinha itens em coluna (opcional para menus verticais)   
        "justify-content": "center",                    # Centraliza itens no eixo vertical (opcional)
        #"align-items": "center",                       # Centraliza itens no eixo horizontal (opcional)
        "transform": "scale(1)",                        # Preparado para efeitos de transformação (zoom)       
        "hover": {  
            "transform": "scale(1.05)",                 # Efeito de zoom suave ao passar o mouse
            "box-shadow": "0 4px 12px rgba(150, 150, 147, 0.15)"  # Aumenta a sombra ao passar o mouse
        }
    },

     # Estilos do ícone quando o item está selecionado
    "icon-selected": {
        "color": "#ffffff!important",  # Force the color change when selected
    },
    
    # Estilos dos ícones exibidos ao lado de cada item de menu
    "icon": {
        "color": "#006018",                             # Cor padrão dos ícones
        "font-size": "20px",                            # Tamanho da fonte dos ícones
        "transition": "color 0.5s ease",                # Transição suave para mudança de cor ao selecionar                
    },
   
    # Estilos dos links de navegação (itens do menu)
    "nav-link": {
        "font-size": "15px",                            # Tamanho da fonte dos links
        "text-align": "left",                           # Alinhamento do texto
        "margin": "2px 0",                              # Espaçamento vertical entre os links
        "padding": "7px 10px",                          # Espaçamento interno dos links
        "border-radius": "8px",                         # Bordas arredondadas dos links
        "transition": "background-color 0.3s ease, color 0.3s ease", # Transição suave para mudanças de cor
        "cursor": "pointer",                            # Exibe o cursor de ponteiro ao passar sobre os links        
        #"display": "flex",                             # Utiliza Flexbox para alinhamento interno
        "align-items": "center",                        # Centraliza os itens no eixo horizontal
        "justify-content": "space-between",             # Espaçamento entre os itens
        "width": "100%",                                # Largura total dos links
        "max-width": "100%",                            # Largura máxima dos links
        #"text-decoration": "none",                     # Remove o sublinhado dos links
        "color": "black",                               # Cor padrão dos links
        "background-color": "transparent",              # Cor de fundo padrão dos links
        "border": "0px solid transparent",              # Borda padrão dos links
        "opacity": "1",                               # Opacidade padrão dos links
        # Hover
        "hover": {
            "background-color": "rgba(190, 217, 91, 0.1)",  # Cor de fundo ao passar o mouse (efeito hover)
            "color": "#0056b3",                             # Cor do texto ao passar o mouse   
        }
    },
    
    # Estilos aplicados ao link selecionado (ativo)
    "nav-link-selected": {
        "background-color": "#02401D",                  # Cor de fundo do item selecionado
        "color": "white",                               # Cor do texto do item selecionado
        "font-weight": "bold",                          # Deixa o texto em negrito para destaque
    },
    
    
}
