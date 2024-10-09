import plotly.express as px
import streamlit as st
import pandas as pd

# Line Chart: Input and Output Over Time
# Objective: Visualize how the input and output of materials varied over time (Time In and Time Out).
# Chart: Line chart that shows the number of transactions on each day or by time range.

@st.cache_resource
def line_chart_nett_weight_by_day(dataSource_filtered):

    dataSource_filtered['Time In'] = pd.to_datetime(dataSource_filtered['Time In'])
    dataSource_filtered['Time In'] = dataSource_filtered['Time In'].dt.date
    net_weight_by_day = dataSource_filtered[['Time In','Nett Weight']]

    net_weight_by_day = net_weight_by_day.groupby('Time In')['Nett Weight'].sum()

    line = px.line(
        net_weight_by_day,
        x=net_weight_by_day.index,
        y='Nett Weight',
        title='Nett Weight by Day',
        labels={'Time In': 'Date', 'Nett Weight': 'Nett Weight (kg)'},
        color_discrete_sequence=['#0072B2'],  # Define a cor do gráfico    
        template='plotly_white' ,           # Define o template do gráfico    
        markers=True,                     # Define os marcadores do gráfico  
        text='Nett Weight',  # Adiciona os rótulos de dados                                                        
    )
    # Aumentar o tamanho dos rótulos dos dados e dos marcadores
    line.update_traces(
        textposition='bottom right',  # Posição dos rótulos
        textfont_size=14,  # Tamanho da fonte dos rótulos
        marker_size=6,    # Tamanho dos marcadores    
        line_width=2 ,      # Largura da linha
        
    )
    # Ajustar o layout do gráfico
    line.update_layout(
        xaxis_title_font={'size': 12},  # Tamanho da fonte do título do eixo X
        yaxis_title_font={'size': 12},  # Tamanho da fonte do título do eixo Y 
        title_font={'size': 14},        # Tamanho da fonte do título do gráfico
        width=600,                      # Largura do gráfico
        height=600                      # Altura do gráfico
    )
    # Display the chart
    st.plotly_chart(line, use_container_width=True)