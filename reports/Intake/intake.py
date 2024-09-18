import streamlit as st
import pandas as pd
import plotly.express as px
from databaseConnection import mydb
from leftMenu_custom_css import leftMenu_custom_css
import json
import os


# Estabelecer a conexão com o banco de dados
engine = mydb()


# Ler o arquivo de mapeamento de colunas JSON
def load_columns_mapping():
    json_file_path = 'reports/intake/intake_columns.json'  # Nome do arquivo JSON
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            return json.load(f)
    else:
        st.error(f"Mapping file '{json_file_path}' not found.")
        return {}

def intake_page(mindate, maxdate):
    # Layout com colunas para os campos de entrada e o botão de execução
    with st.container():
        col1, col2 = st.columns([10, 1])  # Ajustar a largura das colunas

        with col1:
            # Seção de parâmetros de entrada
            with st.expander("Input Parameters", expanded=False):
                # Sub-colunas para campos de entrada
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
            # Botão para gerar o relatório
            if st.button('Run Report', key='run_report_button'):
                st.session_state.run_report = True

    # Verificar se o relatório deve ser executado
    if 'run_report' not in st.session_state:
        st.session_state.run_report = False

    if st.session_state.run_report:
        try:
            # Exibir um spinner enquanto a consulta SQL é executada
            with st.spinner('Running Report...'):
                # Formatar parâmetros para o SQL
                suppliercode = f"'{suppliercode}'" if suppliercode != 'NULL' else 'NULL'
                hauliercode = f"'{hauliercode}'" if hauliercode != 'NULL' else 'NULL'
                haulier = f"'{haulier}'" if haulier != 'NULL' else 'NULL'
                supplier = f"'{supplier}'" if supplier != 'NULL' else 'NULL'
                calloff = f"'{calloff}'" if calloff != 'NULL' else 'NULL'
                keytypes = f"'{keytypes}'" if keytypes != 'NULL' else 'NULL'

                # Chamada da stored procedure com os parâmetros
                storedProcedure = f"""
                    EXEC [Report].[SSRS_IntakeReport]
                    @mindate = '{mindate}',
                    @maxdate = '{maxdate}',
                    @suppliercode = {suppliercode},
                    @hauliercode = {hauliercode},
                    @intakestatustypes = '{intakestatustypes}',
                    @rminclude = '{rminclude}',
                    @haulier = {haulier},
                    @supplier = {supplier},
                    @calloff = {calloff},
                    @siteid = {siteid},
                    @keytypes = {keytypes}
                """

                # Executar a stored procedure e carregar os dados
                dataSource = pd.read_sql(storedProcedure, engine).sort_values('timein')
                dataSource['date'] = dataSource['timein'].dt.date

                # Mostrar os resultados em um dataframe
                st.subheader('Intake Report Dashboard')

                if dataSource.empty:
                    st.write("No data available to display.")
                else:
                    # Carregar o arquivo de mapeamento de colunas JSON
                    columns_to_display = load_columns_mapping()

                    if columns_to_display:
                        # Filtrar e renomear colunas
                        existing_columns = [col for col in columns_to_display.keys() if col in dataSource.columns]
                        dataSource_filtered = dataSource[existing_columns]
                        dataSource_filtered.rename(columns=columns_to_display, inplace=True)

                        st.dataframe(data=dataSource_filtered.sort_values('Time In'), hide_index=True)

                        # Agrupar dados e gerar gráficos
                        grouped_data = dataSource_filtered.groupby('RM Name').agg({'Nett Weight': 'sum'}).reset_index()

                        # Gráfico de barras para Peso Líquido por Código de Matéria-Prima
                        fig_rmName = px.bar(
                            grouped_data.sort_values("Nett Weight"),
                            x='Nett Weight',
                            y='RM Name',
                            orientation='h',
                            title="Net Weight Intake by Raw Material Code",
                            labels={'Nett Weight': 'Net Weight', 'RM Name': 'Raw Material Name'},
                            color_discrete_sequence=['#475b7d'],
                        )
                        fig_rmName.update_layout(height=400, width=600)

                        # Gráfico de linha para Peso Líquido por Número de Baia
                        fig_bayNumber = px.line(
                            dataSource_filtered,
                            x="Time In",
                            y="Nett Weight",
                            title="Net Weight by Bay Number"
                        )
                        fig_bayNumber.update_layout(height=400, width=600)

                        # Exibir os gráficos em duas colunas
                        chartColumn1, chartColumn2 = st.columns(2)
                        with chartColumn1:
                            st.plotly_chart(fig_rmName, use_container_width=True)
                        with chartColumn2:
                            st.plotly_chart(fig_bayNumber, use_container_width=True)

                    else:
                        st.write("No column mapping found. Please check the mapping file.")

                # Resetar o estado do botão para evitar reexecuções contínuas
                st.session_state.run_report = False

        except Exception as e:
            st.error(f"An error occurred: {e}")
