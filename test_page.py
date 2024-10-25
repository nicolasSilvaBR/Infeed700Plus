import streamlit as st
from functions.utilities import get_datetime_input


minDate,maxDate,StartHour,EndHour,StartMinute,EndMinute = get_datetime_input()

# import streamlit as st
# from datetime import datetime, timedelta
# import pandas as pd

# # Callbacks
# st.markdown("#### Select your time range")

# def add_timedelta():
#     initial = st.session_state['start_date']
    
#     if st.session_state['radio_range'] == "Today":
#         today = datetime.now()
#         st.session_state['start_date'] = today
#         st.session_state['end_date'] = today
#     elif st.session_state['radio_range'] == "1 day":
#         st.session_state['end_date'] = initial + timedelta(days=1)
        
#     elif st.session_state['radio_range'] == "7 days":
#         st.session_state['end_date'] = initial + timedelta(days=7)

#     elif st.session_state['radio_range'] == "30 days":
#         st.session_state['end_date'] = initial + timedelta(days=30)
    
#     elif st.session_state['radio_range'] == "Quarter":
#         quarter = (initial.month - 1) // 3 + 1
#         st.session_state['end_date'] = datetime(initial.year, quarter * 3, 1) + timedelta(days=-1)
    
#     elif st.session_state['radio_range'] == "Year":
#         st.session_state['end_date'] = datetime(initial.year, 12, 31)
    
#     elif st.session_state['radio_range'] == "Year to Date":
#         st.session_state['start_date'] = datetime(initial.year, 1, 1)
#         st.session_state['end_date'] = datetime.now()
    
#     else:
#         pass

# def subtract_timedelta():
#     final = st.session_state['end_date']
    
#     if st.session_state['radio_range'] == "Today":
#         today = datetime.now()
#         st.session_state['start_date'] = today
#         st.session_state['end_date'] = today
    
#     elif st.session_state['radio_range'] == "1 day":
#         st.session_state['start_date'] = final - timedelta(days=1)

#     elif st.session_state['radio_range'] == "7 days":
#         st.session_state['start_date'] = final - timedelta(days=7)

#     elif st.session_state['radio_range'] == "30 days":
#         st.session_state['start_date'] = final - timedelta(days=30)
    
#     elif st.session_state['radio_range'] == "Quarter":
#         quarter = (final.month - 1) // 3 + 1
#         st.session_state['start_date'] = datetime(final.year, (quarter - 1) * 3 + 1, 1)
    
#     elif st.session_state['radio_range'] == "Year":
#         st.session_state['start_date'] = datetime(final.year, 1, 1)
    
#     elif st.session_state['radio_range'] == "Year to Date":
#         st.session_state['start_date'] = datetime(final.year, 1, 1)
#         st.session_state['end_date'] = datetime.now()
    
#     else:
#         pass

# # Adiciona as novas opções ao seletor de intervalo
# st.radio(
#     "Select a range", 
#     ["Today", "custom","1 day","7 days", "30 days", "Quarter", "Year", "Year to Date"], 
#     horizontal=True, 
#     key="radio_range", 
#     on_change=add_timedelta,
#     help=""" 
#         When selecting the range choose either the Start or End date then the date will be calculate base in the selected range.
#         Ex. Selected 30 Days     
#     """
# )

# col1, col2, col3 = st.columns(3)

# # Inputs de data para data de início e fim
# col1.date_input("Start date", key="start_date", on_change=add_timedelta)
# col2.date_input("End date", key="end_date", on_change=subtract_timedelta)

