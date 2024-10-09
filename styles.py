import streamlit as st
# Focus on text-related properties and colors that are specific to the option menu. 
# Anything related to the container layout will be moved to the external CSS.
# menu_styles only focuses on text formatting, font sizes, and color styling.

sidebar = st.secrets["sidebar"]

menu_styles = {
    # Menu title styles (text-specific)
    "menu_title": {
        "font-size": "12px",  # Adjust the font size as needed
        "font-weight": "bold",  # Make the title bold
        "color": "#333333",  # Set the color of the title
    },
    
    # Icon styles when the item is selected
    "icon-selected": {
        "color": sidebar['icon_color'],  # Force the color change when selected
    },

    # Container styles (move layout-related properties to CSS)
    "container": {
        "padding": "0px!important",                     # Internal padding of the container (borders)
        "background-color": "#ffffff!important",                  # Menu background color
        "border": "0px solid #e0e0e0",                  # Light border around the menu
        "border-radius": "0px",                         # Rounded borders
        "box-shadow": "0 2px 8px rgba(150, 150, 147, 0.5)",   # Light shadow for depth
        "width": "370px",                               # Menu width
        "max-width": "100%",                            # Maximum width for responsiveness
        "font-family": "Segoe UI",                      # Font used in the menu
        #"font-size": "12px",                            # Adjusts font size for the entire container
        "margin": "0px auto",                           # Center the menu with top and bottom margin
        "transition": "all 0.3s ease-in-out",           # Smooth transition for any style changes
        "opacity": "1",                                 # Defines the container's opacity
        "backdrop-filter": "blur(5px)",                 # Background blur effect (modern and clean)        
        "overflow": "hidden",                           # Ensures that no content overflows outside the container       
        "flex-direction": "column",                     # Align items in a column (optional for vertical menus)
        "justify-content": "center",                    # Center items on the vertical axis (optional)       
        "transform": "scale(1)",                        # Prepared for transformation effects (zoom       
        
    },
    
    # Icon styles for unselected items
    "icon": {  
        "color": sidebar['icon_color'],     
        "font-size": "20px",  # Font size for icons
    },
   
    # Navigation links (menu items)
    "nav-link": {
        "font-size": "15px",  # Font size for links
        "color": "#73726F",   # Default color for links    
        "padding": "px 10px",# Internal spacing for links, space between each report name   
    },
    
    # Selected link (active state)
    "nav-link-selected": {
        "background-color": sidebar['selected_item_color'],  # Background color for selected item
        "color": "white",  # Text color for selected item
        "font-weight": "bold",  # Bold text for emphasis
    },
}