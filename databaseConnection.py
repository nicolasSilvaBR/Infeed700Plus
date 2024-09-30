import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

@st.cache_resource
def mydb() -> Engine:
    """
    Cria uma conexão com o banco de dados SQL Server usando SQLAlchemy.

    Retorna:
        engine: Objeto de engine SQLAlchemy para interações com o banco de dados.
    """
    # Acessar os detalhes de conexão a partir do arquivo de configuração secrets do Streamlit
    db_config = st.secrets["mydb"]

    # Verificar se todos os parâmetros necessários estão presentes
    required_keys = ["username", "password", "host", "port", "database"]
    missing_keys = [key for key in required_keys if key not in db_config]
    if missing_keys:
        raise ValueError(f"Faltando parâmetros de configuração: {', '.join(missing_keys)}")

    # Usar o driver ODBC padrão
    driver = "ODBC Driver 17 for SQL Server"

    # Construir a string de conexão para o SQL Server
    connection_string = (
        f"mssql+pyodbc://{db_config['username']}:{db_config['password']}@"
        f"{db_config['host']}:{db_config['port']}/{db_config['database']}?driver={driver}"
    )
    
    # Criar o engine do SQLAlchemy
    engine = create_engine(connection_string)
    
    return engine
