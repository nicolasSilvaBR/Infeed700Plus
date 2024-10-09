# File style.py
# The file is used to define the styles of the menu, including the container, links, icons, and selected state.
# The styles are defined in a dictionary, where each key represents a class or ID of an HTML element, and the value is a dictionary of styles to be applied to that element.

# The styles are divided into several sections:
# - container: styles for the container that encloses the menu
# - icon: styles for the icons displayed next to each menu item
# - nav-link: styles for the links (menu items)
# - nav-link-selected: styles for the selected state of the links (menu items)
# - icon-selected: styles for the icon when the item is selected

menu_styles = {
    # General styles for the container that wraps the menu
    # Icon styles when the item is selected
    "icon-selected": {
        "color": "#ffffff!important",  # Force the color change when selected
    },

    "container": {
        "padding": "0px!important",                     # Internal padding of the container (borders)
        "background-color": "#ffffff",                  # Menu background color
        "border": "0px solid #e0e0e0",                  # Light border around the menu
        "border-radius": "0px",                         # Rounded borders
        "box-shadow": "0 2px 8px rgba(150, 150, 147, 0.5)",   # Light shadow for depth
        "width": "370px",                               # Menu width
        "max-width": "100%",                            # Maximum width for responsiveness
        "font-family": "Segoe UI",                      # Font used in the menu
        "font-size": "12px",                            # Adjusts font size for the entire container
        "margin": "0px auto",                           # Center the menu with top and bottom margin
        "transition": "all 0.3s ease-in-out",           # Smooth transition for any style changes
        "opacity": "1",                                 # Defines the container's opacity
        "backdrop-filter": "blur(5px)",                 # Background blur effect (modern and clean)
        # "background-image": "url('path/to/image.jpg')",  # Example for adding background image
        # "background-size": "cover",                   # Make the background image cover the whole container
        "overflow": "hidden",                           # Ensures that no content overflows outside the container
        #"display": "flex",                              # Use Flexbox for internal alignment
        "flex-direction": "column",                     # Align items in a column (optional for vertical menus)
        "justify-content": "center",                    # Center items on the vertical axis (optional)
        #"align-items": "center",                       # Center items on the horizontal axis (optional)
        "transform": "scale(1)",                        # Prepared for transformation effects (zoom)
        "hover": {  
            "transform": "scale(1.05)",                 # Smooth zoom effect on hover
            "box-shadow": "0 4px 12px rgba(150, 150, 147, 0.15)"  # Increase shadow on hover
        }
    },
    
    # Styles for the icons displayed next to each menu item
    "icon": {
        "color": "#006018",                             # Default color for icons
        "font-size": "20px",                            # Font size for icons
        "transition": "color 0.5s ease",                # Smooth transition for color change when selected
    },
   
    # Styles for the navigation links (menu items)
    "nav-link": {
        "font-size": "15px",                            # Font size for links
        "text-align": "left",                           # Text alignment
        "margin": "2px 0",                              # Vertical spacing between links
        "padding": "2px 10px",                          # Internal spacing for links, space between each report name
        "border-radius": "6px",                         # Rounded borders for links
        "transition": "background-color 0.3s ease, color 0.3s ease", # Smooth transition for color changes
        "cursor": "pointer",                            # Display pointer cursor when hovering over links
        #"display": "line",                              # Use Flexbox for internal alignment
        "align-items": "center",                        # Center items on the horizontal axis
        "justify-content": "space-between",             # Space between items
        "width": "100%",                                # Full width for links
        "max-width": "100%",                            # Maximum width for links        
        "color": "#73726F",                             # Default color for links
        "background-color": "transparent",              # Default background color for links
        "border": "0px solid transparent",              # Default border for links
        "opacity": "1",                                 # Default opacity for links        
        "hover": {
            "background-color": "rgba(190, 217, 91, 0.1)",  # Background color on hover effect
            "color": "#0056b3",                             # Text color on hover
        }
    },
    
    # Styles applied to the selected (active) link
    "nav-link-selected": {
        "background-color": "#00401f",                  # Background color for selected item
        "color": "white",                               # Text color for selected item
        "font-weight": "bold",                          # Bold text for emphasis
        "border": "0px solid #00401f",                  # Border for selected item
        "opacity": "1",                                 # Full opacity for selected item
        "hover": {
            "background-color": "#0056b3",              # Background color on hover effect
            "color": "white",                           # Text color on hover effect
        }
    },
}
