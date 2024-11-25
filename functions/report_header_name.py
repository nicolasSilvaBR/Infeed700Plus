import streamlit as st
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from functions.secrets_config import get_secrets_config

# Load database configurations from secrets
db_config = get_secrets_config()
infeed_database_name = db_config["database"]
enecoms_database_name = db_config["enecoms_database"]

# Function to fetch and process the SQL query
def get_report_headers_and_reports_names(project, engine):
    # Determine the database name based on the project
    database_name = infeed_database_name if project == 'Infeed700' else enecoms_database_name

    # SQL query to retrieve data
    sql_query = f"""
        declare @project varchar(15) = '{project}'

        if @project IS NULL OR @project = 'Infeed700'
        SELECT	
            [MenuItems].[HeaderId]
            ,[HeaderName]
            ,[ReportDisplayName]
            ,[ReportName]
            ,ItemDisplayOrder           
        FROM {infeed_database_name}.[Report].[MenuItems]
        JOIN {infeed_database_name}.[Report].[MenuHeader] ON [MenuHeader].HeaderId = [MenuItems].HeaderId
        WHERE [MenuItems].IsActive = 1 AND [MenuHeader].IsActive = 1
        ORDER BY  
            [MenuHeader].WebHeaderDisplayOrder,
            [ItemDisplayOrder],
            [ReportDisplayName]

        if @project = 'Enecoms'
        SELECT	
            [MenuItems].[HeaderId]
            ,[HeaderName]
            ,[ReportDisplayName]
            ,[ReportName]
            ,ItemDisplayOrder      
        FROM {enecoms_database_name}.[Report].[MenuItems]
        JOIN {enecoms_database_name}.[Report].[MenuHeader] ON [MenuHeader].HeaderId = [MenuItems].HeaderId
        WHERE [MenuItems].IsActive = 1 AND [MenuHeader].IsActive = 1
        ORDER BY  
            [MenuHeader].WebHeaderDisplayOrder,
            [ItemDisplayOrder],
            [ReportDisplayName]
    """

    try:
        # Execute the SQL query and load the result into a DataFrame
        df = pd.read_sql_query(sql_query, engine)

        # Check if the DataFrame is empty
        if df.empty:
            # Display an error message if no data is found
            st.error(
                f"No data found for the project '{project}' in the database '{database_name}'. "
                "Please make sure the database name is correct and exists in the source."
            )
            return None, None

        # Process the data if the query returns results
        headers_name = df[['HeaderId', 'HeaderName']].drop_duplicates()  # Extract unique headers
        reports_names = df[['HeaderName', 'HeaderId', 'ReportDisplayName', 'ReportName']].drop_duplicates()  # Extract unique reports

        return headers_name, reports_names

    except SQLAlchemyError as e:
        # Handle SQL execution errors
        st.error(
            f"An error occurred while querying the database '{database_name}': {str(e)}. "
            "Please make sure the database name is correct and exists in the source."
        )
        return None, None

    except Exception as e:
        # Handle any other unexpected errors
        st.error(
            f"An unexpected error occurred while processing the project '{project}': {str(e)}. "
            "Please make sure the database name is correct and exists in the source."
        )
        return None, None
