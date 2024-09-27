import streamlit as st

headers = {"Intake": 1, "Blending": 2, "Press": 3}
reports = {"Intake": 1, "TipBreakdown": 1, "Blending": 2, "Press Summary": 3}

def LeftMenu():
    # Load CSS for custom styles
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    local_css("leftMenu/style.css")

    with st.sidebar:
        for header, valor in headers.items():
            with st.expander(header, expanded=False):
                for report, valor2 in reports.items():
                    if valor2 == valor:
                        # Button to set the report selection
                        if st.button(report):
                            st.session_state['selected_report'] = report

