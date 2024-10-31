import streamlit as st
import pandas as pd

# Function to fetch and process the SQL query
def get_report_headers_and_reports_names(project,engine):
    sql_query = f"""
    
        declare @project varchar(15) = '{project}'

        if @project IS NULL OR @project = 'Infeed700'
        SELECT	
            [MenuItems].[HeaderId]
            ,[HeaderName]
            ,[ReportDisplayName]
            ,[ReportName]
            ,ItemDisplayOrder           
        FROM [Infeed700DAS].[Report].[MenuItems]
        JOIN [Infeed700DAS].[Report].[MenuHeader] ON [MenuHeader].HeaderId = [MenuItems].HeaderId
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
        FROM [EnecomsDAS].[Report].[MenuItems]
        JOIN [EnecomsDAS].[Report].[MenuHeader] ON [MenuHeader].HeaderId = [MenuItems].HeaderId
        WHERE [MenuItems].IsActive = 1 AND [MenuHeader].IsActive = 1
        ORDER BY  
            [MenuHeader].WebHeaderDisplayOrder,
            [ItemDisplayOrder],
            [ReportDisplayName]

    """
    # Read the SQL query into a DataFrame
    df = pd.read_sql_query(sql_query, engine)
    # Ensure the DataFrame is not empty
    if df.empty:
        st.error("No data found. Please check your database or query.")
    else:
        headers_name = df[['HeaderId', 'HeaderName']].drop_duplicates()
        reports_names = df[['HeaderName', 'HeaderId', 'ReportDisplayName', 'ReportName']].drop_duplicates()

    return headers_name,reports_names