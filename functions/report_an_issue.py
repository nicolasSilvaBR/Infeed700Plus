import streamlit as st

def report_an_issue_button(minDate, StartHour, StartMinute, maxDate, EndHour, EndMinute):
    # Recuperar mensagem de erro armazenada
    error_msg = st.session_state.get('error_msg', 'No error message available')
    site_info = st.session_state.get('selected_site', 'Unknown Site')
    reportRDLname = st.session_state.get('selected_report', 'Unknown Report')

    # Criar botão de e-mail com as informações do erro
    st.markdown(
        f"""
        <a href="mailto:reports@icmcsl.ie?subject=Report Issue Details - {site_info}&body=To ICM Reports Team%0A%0A
        Error Msg: {error_msg}%0A
        Project: {st.session_state['selected-project']}%0A
        ReportRDL: {reportRDLname}%0A
        Date From: {minDate.strftime('%d/%m/%Y')}%0A
        Start Hour: {StartHour}%0A
        Start Minute: {StartMinute}%0A
        Date To: {maxDate.strftime('%d/%m/%Y')}%0A
        End Hour: {EndHour}%0A
        End Minute: {EndMinute}%0A%0A
        Describe the issue:
        "
        style="text-decoration:none; font-size:14px; color:white; background-color:#007bff; padding:8px 8px; border-radius:5px;">
        Report an Issue via Email
        </a>
        """,
        unsafe_allow_html=True
    )