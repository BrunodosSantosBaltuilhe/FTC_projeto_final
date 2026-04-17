from haversine import haversine
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
import datetime as dt
import folium
import numpy as np

df = pd.read_csv(r'C:\Users\User\Documents\repos\ftc.python\zomato_corrigido_para_analise.csv')

def restaurantes_map(df):
    df_aux = df.loc[:, ['Latitude','Longitude','Restaurant Name','Address']].copy()
    # garante que latitude e longitude sejam numéricas
    df_aux['Latitude'] = pd.to_numeric(df_aux['Latitude'], errors='coerce')
    df_aux['Longitude'] = pd.to_numeric(df_aux['Longitude'], errors='coerce')
    df_aux = df_aux.dropna(subset=['Latitude', 'Longitude'])
    # centro inicial do mapa
    center_lat = df_aux['Latitude'].median()
    center_lon = df_aux['Longitude'].median()

    map_fig = folium.Map(location=[center_lat, center_lon], zoom_start=2)

    # um marcador para cada restaurante
    for _, restaurant_info in df_aux.iterrows():
        folium.Marker(
            location=[restaurant_info['Latitude'], restaurant_info['Longitude']],
            popup=f"""
                <b>{restaurant_info['Restaurant Name']}</b><br>
                {restaurant_info['Address']}
            """,
            tooltip=restaurant_info['Restaurant Name']
        ).add_to(map_fig)

    folium_static(map_fig, width=1024, height=600)

    return map_fig

st.set_page_config(
    page_title="Visão Negócio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Fome zero!")
st.title("O Melhor lugar para encontrar seu mais novo restaurante favorito!")

st.set_page_config(page_title="Projeto", layout="wide")
with st.container():
    st.header('Temos as seguintes marcas dentro da nossa plataforma:')
    col1,col2,col3,col4,col5 = st.columns(5, gap='Large')
    with col1:
        total_rest = df['Restaurant ID'].nunique()
        st.metric('Restaurantes Cadastrados', total_rest)
    with col2:
        paises_cad = df['Country Code'].nunique()
        st.metric('Países Cadastrados', paises_cad)
    with col3:
        cidade_cad = df['City'].nunique()
        st.metric('Cidades Cadastradas', cidade_cad)
    with col4:
        soma_votos = df['Votes'].sum()
        st.metric('Total de Avaliações', f"{soma_votos:,.0f}".replace(",", "."))
    with col5:
        cuisines_unicos = df['Cuisines'].nunique()
        st.metric('Total de Culinárias', cuisines_unicos)
with st.container():
     restaurantes_map(df)







