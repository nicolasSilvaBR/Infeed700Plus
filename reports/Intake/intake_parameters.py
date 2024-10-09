import streamlit as st

def intake_parameters():
    '''
    This function is used to display the input parameters for the intake report.    
    '''
    st.session_state.run_report = True

    with st.container():
        col1, col2 = st.columns([10, 1])

        with col1:
            with st.expander("Input Parameters", expanded=False):
                input_col1, input_col2, input_col3 = st.columns(3)
                
                with input_col1:
                    suppliercode = st.text_input('Supplier Code', value='NULL', key='input_suppliercode')
                    supplier = st.text_input('Supplier', value='NULL', key='input_supplier')
                    hauliercode = st.text_input('Haulier Code', value='NULL', key='input_hauliercode')
                    haulier = st.text_input('Haulier', value='NULL', key='input_haulier')

                with input_col2:
                    intakestatustypes = st.text_input('Intake Status Types', value='1,2,3', key='input_intakestatustypes')
                    rminclude = st.text_input('RM Include', value='-1', key='input_rminclude')
                    keytypes = st.text_input('Key Types', value='1,31,41,51', key='input_keytypes')

                with input_col3:
                    calloff = st.text_input('Call Off', value='NULL', key='input_calloff')
                    siteid = st.number_input('Site ID', value=0, key='input_siteid')

        with col2:
            if st.button('Run Report', key='run_report_button'):
                st.session_state.run_report = True

        return (suppliercode, supplier, hauliercode, haulier, intakestatustypes, rminclude, keytypes, calloff, siteid)
