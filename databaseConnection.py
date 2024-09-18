import streamlit as st
from sqlalchemy import create_engine

@st.cache_resource
def mydb():
    # Access the connection details from .toml file
    db_config = st.secrets["mydb"]

    # Connect to SQL Server using SQLAlchemy
    connection_string = (
        f"mssql+pyodbc://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}?driver={db_config['driver']}"
    )
    engine = create_engine(connection_string)
    return engine