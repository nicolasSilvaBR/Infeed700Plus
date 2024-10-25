import streamlit as st

# Read the content of the releases.md file
with open('releases.md', 'r') as file:
    releases_text = file.read()
    
    
    
st.markdown(releases_text)