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

# #1. Qual o nome do país que possui mais cidades registradas?

# mais_cidade = df['City'].groupby(df['Country Name']).nunique()
# mais_cidade.sort_values(ascending=False).head(1)

# #2. Qual o nome do país que possui mais restaurantes registrados?

# df1 = df.copy()
# df1['Restaurant ID'] = df1['Restaurant ID'].astype(str).str.strip()
# mais_restaurantes_reg = df1['Restaurant ID'].groupby(df1['Country Name']).nunique()
# mais_restaurantes_reg.sort_values(ascending=False).head(1)

# #3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?

# nivel_4 = df['Country Name'][df['Price range'] == 4].value_counts()
# nivel_4.head(1)

# #4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?

# tipos_culinaria_distintos = df['Cuisines'].groupby(df['Country Name']).nunique()
# tipos_culinaria_distintos.sort_values(ascending=False).head(1)

# #5. Qual o nome do país que possui a maior quantidade de avaliações feitas?

# aval_feitas = df['Votes'].groupby(df['Country Name']).sum()
# aval_feitas.sort_values(ascending=False)

# #6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?

# df_Entrega_online = df['Has Online delivery'] == 'Yes'
# df_Entrega_online.groupby(df['Country Name']).sum().sort_values(ascending=False).head(1)


# #7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?


# qtda_rest_reservas = df['Has Table booking'].groupby(df['Country Name']).sum()
# qtda_rest_reservas.sort_values(ascending=False).head(1)

# #8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?


# media_qtda_aval = df['Votes'].groupby(df['Country Name']).mean()
# media_qtda_aval.sort_values(ascending=False).head(1)

# #9. Qual o nome do país que possui, na média, a maior nota média registrada?

# media_nota = df['Aggregate rating'].groupby(df['Country Name']).mean()
# media_nota.sort_values(ascending=False).head(1)

# #10. Qual o nome do país que possui, na média, a menor nota média registrada?

# menor_media = df['Aggregate rating'].groupby(df['Country Name']).mean()
# menor_media.sort_values(ascending=True).head(1)


# #11. Qual a média de preço de um prato para dois por país?

# media_prato_para_dois = df['Average Cost for two'].groupby(df['Country Name']).mean()
# media_prato_para_dois.sort_values(ascending=False)

st.set_page_config(
    page_title="Países",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Países")

st.sidebar.markdown("""---""")
with st.sidebar:
    st.sidebar.title('Filtros')
    
    country_options = st.sidebar.multiselect(
         ('Escolha os Paises que Deseja visualizar as Informações'),
        options=sorted(df['Country Name'].dropna().unique()),
        default=sorted(df['Country Name'].dropna().unique())
    )

    st.markdown("""---""")
    qtda_restaurantes = st.slider(
        'Quantos restaurantes quer selecionar',
        min_value=1,
        max_value=15,
        value=10
    )
    
filtro_paises = df['Country Name'].isin(country_options)
df_paises = df.loc[filtro_paises,:]
with st.container():
    col1,col2,col3 = st.columns(3)
    with col1:
        st.markdown('Total de Países Cadastrados')
        total_paises = df['Country Name'].nunique()
        st.header(total_paises)
    with col2:
        st.markdown('Total de Restaurantes Cadastrados')
        total_restaurantes = df['Restaurant ID'].nunique()
        st.header(total_restaurantes)
    with col3:
        st.markdown('Média Restaurantes por País')
        media_rest_pais = round(total_restaurantes / total_paises)
        st.header(media_rest_pais)
with st.container():
    restaurantes_per_paises = (df_paises.groupby('Country Name')['Restaurant ID'].nunique()
                               .sort_values(ascending=False).reset_index().head(qtda_restaurantes))
    fig = px.bar(restaurantes_per_paises, x='Country Name', y='Restaurant ID', 
                 title ='Quantidade de restaurantes cadastrados em cada país',
                 labels={
                     'Country Name':'Países',
                     'Restaurant ID' : 'Quantidade de restuarantes'
                 },
                 text='Restaurant ID',
                 color='Country Name'
    )
    st.plotly_chart(fig, use_container_width=True)
with st.container():
    cidades_per_pais = (df_paises.groupby('Country Name')['City'].nunique()
                        .sort_values(ascending=False).reset_index().head(qtda_restaurantes))
    fig = px.bar(cidades_per_pais, x='Country Name', y='City', 
                 title='Quantidade de cidades registradas em cada país',
                 labels={
                     'Country Name':'Países',
                     'City':'Quantidade de cidades registradas em cada país'
                 },
                text='City',
                color='Country Name'
    )
    st.plotly_chart(fig, use_container_width=True)
with st.container():
    col1,col2 = st.columns(2)
    with col1:
        medias_aval_per_pais = (df_paises.groupby("Country Name")['Votes'].mean().round(2)
                                .sort_values(ascending=False).reset_index().head(qtda_restaurantes))
        fig = px.bar(medias_aval_per_pais, x='Country Name', y='Votes', 
                     title='Médias de avaliações feitas por país',
                     labels={
                         'Country Name':'Países',
                         'Votes':'Quantidade de avaliações'
                     },
                     text='Votes',
                     color='Country Name'
                    )
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        aval_medio_per_pais = (df_paises.groupby('Country Name')['Aggregate rating'].mean().round(2)
                               .sort_values(ascending=False).reset_index().head(qtda_restaurantes))
        fig= px.bar(aval_medio_per_pais, x='Country Name', y='Aggregate rating', 
                    title ='Avaliação Média por país',
                    labels={
                        'Country Name':'Países',
                        'Aggregate rating':'Avaliação Média'
                    },
                    text='Aggregate rating',
                    color='Country Name'
                   )
        st.plotly_chart(fig, use_container_width=True)
        