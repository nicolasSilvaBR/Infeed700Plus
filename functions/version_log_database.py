import streamlit as st
import pandas as pd
from functions.secrets_config import get_secrets_config

db_config = get_secrets_config()
infeed_database_name = db_config["database"]

# Function to fetch and process the SQL query
def get_database_version_log_tfs_update(engine):
    sql_query = f"""  
        SELECT top 1 AppliedDT as AppliedDate
        FROM {infeed_database_name}.[dbo].[VersionLog] order by VersionId desc  
    """
    # Read the SQL query into a DataFrame
    df = pd.read_sql_query(sql_query, engine)
    # Ensure the DataFrame is not empty
    if df.empty:
        st.error("No data found. Please check your database or query.")
    else:
        database_version_log = df[['HeaderId']].drop_duplicates()        

    return database_version_log