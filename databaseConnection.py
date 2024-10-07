import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

@st.cache_resource
def mydb() -> Engine:
    """
        Creates a connection to the SQL Server database using SQLAlchemy.

        Returns:
            engine: SQLAlchemy engine object for interactions with the database.
    """
    # Access connection details from Streamlit secrets configuration file
    db_config = st.secrets["mydb"]

    # Check if all required parameters are present
    required_keys = ["username", "password", "host", "port", "database"]
    missing_keys = [key for key in required_keys if key not in db_config]
    if missing_keys:
        raise ValueError(f"Missing configuration parameters: {', '.join(missing_keys)}")

    # Use the default ODBC driver
    driver = "ODBC Driver 17 for SQL Server"

    # Build the connection string for SQL Server
    connection_string = (
        f"mssql+pyodbc://{db_config['username']}:{db_config['password']}@"
        f"{db_config['host']}:{db_config['port']}/{db_config['database']}?driver={driver}"
    )
    
    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)
    
    return engine
