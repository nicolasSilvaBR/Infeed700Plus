import streamlit as st

headers = {1:"Intake", 2:"Blending", 3:"Press"}
reports = {1:[["Intakes","Intake"],["Intake Tips","TipBreakdown"]],
           2:[["Blending / Batching","Batch"],["Blending / Run","BatchByRunNumber"]]
        }


def LeftMenu():
    # Load CSS for custom styles
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    local_css("leftMenu/style.css")

    with st.sidebar:
        for key, header in headers.items():
            with st.expander(header, expanded=False):               
                for key2, report in reports.items():
                    if key2 == key:
                        for reportitem in report:                  
                            if st.button(reportitem[0],key=reportitem[1]):
                                st.session_state['selected_report'] = reportitem[1]

