import streamlit as st
from datetime import datetime, timedelta

def get_datetime_input():
    
    try:
        def add_timedelta():
            initial = st.session_state['start_date']
            
            if st.session_state['radio_range'] == "Today":
                today = datetime.now()
                st.session_state['start_date'] = today
                st.session_state['end_date'] = today
            elif st.session_state['radio_range'] == "1 day":
                st.session_state['end_date'] = initial + timedelta(days=1)
                
            elif st.session_state['radio_range'] == "7 days":
                st.session_state['end_date'] = initial + timedelta(days=7)

            elif st.session_state['radio_range'] == "30 days":
                st.session_state['end_date'] = initial + timedelta(days=30)
            
            if st.session_state['radio_range'] == "Quarter":
                # Usa pandas para obter o último dia do trimestre baseado na data 'initial'
                quarter_end = pd.Period(initial.strftime('%Y-%m-%d'), freq='Q').end_time
                st.session_state['end_date'] = quarter_end
            
            elif st.session_state['radio_range'] == "Year":
                st.session_state['end_date'] = datetime(initial.year, 12, 31)
            
            elif st.session_state['radio_range'] == "Year to Date":
                st.session_state['start_date'] = datetime(initial.year, 1, 1)
                st.session_state['end_date'] = datetime.now()
            
            else:
                pass

        def subtract_timedelta():
            final = st.session_state['end_date']
            
            if st.session_state['radio_range'] == "Today":
                today = datetime.now()
                st.session_state['start_date'] = today
                st.session_state['end_date'] = today
            
            elif st.session_state['radio_range'] == "1 day":
                st.session_state['start_date'] = final - timedelta(days=1)

            elif st.session_state['radio_range'] == "7 days":
                st.session_state['start_date'] = final - timedelta(days=7)

            elif st.session_state['radio_range'] == "30 days":
                st.session_state['start_date'] = final - timedelta(days=30)
            
            if st.session_state['radio_range'] == "Quarter":
                # Usa pandas para obter o primeiro dia do trimestre baseado na data 'final'
                quarter_start = pd.Period(final.strftime('%Y-%m-%d'), freq='Q').start_time
                st.session_state['start_date'] = quarter_start
            
            elif st.session_state['radio_range'] == "Year":
                st.session_state['start_date'] = datetime(final.year, 1, 1)
            
            elif st.session_state['radio_range'] == "Year to Date":
                st.session_state['start_date'] = datetime(final.year, 1, 1)
                st.session_state['end_date'] = datetime.now()
            
            else:
                pass    
        
        # Columns to show in the datetime parameters
        col_radio,col_min,col_max,col_text,space_col1 = st.columns([2,2,2,3,13])  
            
        with col_radio:
            st.radio(
                "Select a range", 
                ["Custom","Today","1 day","7 days", "30 days", "Quarter", "Year", "Year to Date"], 
                horizontal=False, 
                key="radio_range", 
                on_change=add_timedelta,
                help=""" 
                    When selecting the range, choose either the Start or End date, and the other date will be automatically calculated based on the selected range.
                    For example, if you select "30 Days," and choose a Start Date, the End Date will be set to 30 days later.     
                """
            )
            
        with col_min:            
            minDate = st.date_input("Start date", key="start_date", on_change=add_timedelta,format="DD/MM/YYYY")
            StartHour = st.selectbox(label='Start Hour',options=list(range(24)),index=0)
            StartMinute = st.selectbox(label='Start Minute',options=list(range(60)),index=0)
            
        with col_max:
            if "Quarter" not in st.session_state['radio_range']:
                maxDate = st.date_input("End date", key="end_date", on_change=subtract_timedelta,format="DD/MM/YYYY")
            else:
                maxDate = st.date_input("End date", key="end_date", on_change=subtract_timedelta,format="DD/MM/YYYY",disabled=True)
            EndHour = st.selectbox(label='End Hour',options=list(range(24)),index=23)
            EndMinute = st.selectbox(label='End Minute',options=list(range(60)),index=59)  
        
        
        return minDate,maxDate,StartHour,EndHour,StartMinute,EndMinute
    
    except Exception as e:
        # Tratamento para erros genéricos (qualquer outro tipo de exceção)
        st.write(f"Check the get_datetime_input() : {e} Columns to show in the datetime parameters")