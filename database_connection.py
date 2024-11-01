import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
import toml
import os

@st.cache_resource
def mydb() -> Engine:
    """
    Creates a connection to the SQL Server database using SQLAlchemy.

    Returns:
        engine: SQLAlchemy engine object for interactions with the database.
    """
    # Retrieve the configuration file name from Streamlit secrets
    secrets_config = st.secrets.get("secrets_config", {"secrets_name": ".streamlit/secrets.toml"})
    secrets_name = secrets_config.get("secrets_name", ".streamlit/secrets.toml")

    # Ensure the file has the .toml extension and is in the .streamlit folder
    if not secrets_name.endswith(".toml"):
        secrets_name = f".streamlit/{secrets_name}.toml"
    else:
        secrets_name = f".streamlit/{secrets_name}"

    # Convert to absolute path and display for debugging
    absolute_path = os.path.abspath(secrets_name)
    #st.write(f"Absolute path for configuration file: {absolute_path}")

    # Check if the file exists
    if not os.path.isfile(absolute_path):
        st.error(f"The configuration file '{absolute_path}' was not found. Please check the path and file name.")
        return None

    # Load configuration from the TOML file
    try:
        # Load the entire configuration file and access the "mydb" section
        db_config = toml.load(absolute_path)["mydb"]
    except KeyError:
        st.error("The 'mydb' section was not found in the configuration file.")
        return None
    except Exception as e:
        st.error(f"Error loading the configuration file: {e}")
        return None

    # Check if all required parameters are present
    required_keys = ["username", "password", "host", "port", "database"]
    missing_keys = [key for key in required_keys if key not in db_config]
    if missing_keys:
        st.error(f"Missing configuration parameters: {', '.join(missing_keys)}")
        return None

    # Use the default ODBC driver
    driver = "ODBC Driver 17 for SQL Server"

    # Build the connection string for SQL Server
    connection_string = (
        f"mssql+pyodbc://{db_config['username']}:{db_config['password']}@"
        f"{db_config['host']}:{db_config['port']}/{db_config['database']}?driver={driver}"
    )

    # Create the SQLAlchemy engine
    try:
        engine = create_engine(connection_string)
        return engine
    except Exception as e:
        st.error(f"Error creating the connection engine: {e}")
        return None
