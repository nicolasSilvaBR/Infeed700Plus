import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

def get_odbc_driver() -> str:
    """
    Determine the appropriate ODBC driver based on the SQL Server version.

    This function checks the SQL Server version and returns the corresponding 
    ODBC driver. If no version is specified or if it falls below a certain 
    threshold, a default driver is returned.

    Returns:
        str: The name of the ODBC driver to use.
    """
    # Retrieve the SQL Server version from Streamlit secrets.
    # If not found, default to "2019".
    sql_server_version = st.secrets["mydb"].get("sql_server_version", "2019")

    # Determine the ODBC driver based on the SQL Server version.
    if sql_server_version >= "2022":
        return "ODBC Driver 17 for SQL Server"  # Use the latest driver for SQL Server 2022
    elif sql_server_version >= "2012":
        return "ODBC Driver 13 for SQL Server"  # Use driver suitable for SQL Server 2012 and later
    else:
        return "ODBC Driver 17 for SQL Server"  # Default driver for older versions

@st.cache_resource
def mydb() -> Engine:
    """
    Create a database connection to SQL Server using SQLAlchemy.

    This function retrieves connection details from Streamlit secrets, 
    constructs the connection string, and creates an SQLAlchemy engine 
    object to facilitate interactions with the SQL Server database.

    Returns:
        engine: SQLAlchemy engine object for the database connection.
    """
    # Access the connection details from the Streamlit secrets configuration file.
    db_config = st.secrets["mydb"]

    # Check if all required configuration parameters are present in db_config.
    required_keys = ["username", "password", "host", "port", "database"]
    for key in required_keys:
        if key not in db_config:
            # Log an error if a required key is missing and exit the function.
            st.error(f"Missing required configuration key: {key}")
            return None  # Optionally handle the error according to your needs

    # Use the function to define the ODBC driver based on the SQL Server version.
    driver = get_odbc_driver()

    # Construct the connection string for SQL Server using SQLAlchemy.
    connection_string = (
        f"mssql+pyodbc://{db_config['username']}:{db_config['password']}@"
        f"{db_config['host']}:{db_config['port']}/{db_config['database']}?driver={driver}"
    )
    
    # Create the SQLAlchemy engine using the constructed connection string.
    engine = create_engine(connection_string)
    
    return engine  # Return the SQLAlchemy engine for further database operations.
