import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Lab", page_icon=":bar_chart:", layout="wide")
# Título da página
st.subheader("Upload CSV, Visualize Data, and Select Columns to Display")

# Função para carregar e exibir os dados
def load_and_display_data(uploaded_file):
    # Carrega o arquivo CSV em um DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Exibe as colunas disponíveis
    st.write("### Columns in the CSV file:")
    all_columns = df.columns.tolist()
    selected_columns = st.multiselect("Select columns to display:", all_columns, default=all_columns)
    
    # Exibe as colunas selecionadas
    st.write("### Data from the CSV file (selected columns):")
    st.dataframe(df[selected_columns])
    
    return df, selected_columns

# Componente para upload de arquivo CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Verifica se um arquivo foi carregado
if uploaded_file is not None:
    # Carrega os dados e permite escolher as colunas para exibir
    load_and_display_data(uploaded_file)
else:
    st.write("Please upload a CSV file to view its content.")

