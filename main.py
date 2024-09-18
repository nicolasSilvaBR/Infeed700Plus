import streamlit as st
from leftMenu_custom_css import leftMenu_custom_css  # Custom CSS for the left menu
from reports.Intake.intake import intake_page  # Import the intake page function
from leftMenu import LeftMenu  # Import the left menu functionality

# Configure the page layout to "wide" (esta linha deve ser a primeira)
st.set_page_config(layout="wide")

# Apply custom left menu styles (if necessary)
leftMenu_custom_css()

# Display the left menu
LeftMenu()

# Call the intake page with predefined dates
intake_page('2024-08-01', '2024-09-17')
