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

# #1. Qual o nome da cidade que possui mais restaurantes registrados?


# mais_restaurantes_cidade = df['Restaurant ID'].groupby(df['City']).count()
# mais_restaurantes_cidade.sort_values(ascending=False).head(1)

# #2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?

# restaurantes_nota_media_acima_de_4 = df['Aggregate rating'] >= 4
# cidade_restuarante_maior_4 = df[restaurantes_nota_media_acima_de_4].groupby(df['City'])['Restaurant ID'].count()
# cidade_restuarante_maior_4.sort_values(ascending=False).head(1)

# #3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?

# nota_abaixo_dois_e_meio = df['Aggregate rating'] <= 2.5
# cidade_restaurante_abaixo_dois_e_meio = df[nota_abaixo_dois_e_meio].groupby(df['City'])['Restaurant ID'].count()
# cidade_restaurante_abaixo_dois_e_meio.sort_values(ascending=False).head(1)


# #4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?

# maior_valor_medio_para_dois = df['Average Cost for two'].groupby(df['City']).mean()
# maior_valor_medio_para_dois.sort_values(ascending=False).head(1)

# #5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?


# cidade_maior_qtda_culinaria = df['Cuisines'].groupby(df['City']).nunique()
# cidade_maior_qtda_culinaria.sort_values(ascending=False).head(1)

# #6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?


# reservas_yes = df['Has Table booking'] == 1
# cidade_mais_restaurantes_com_reserva = df[reservas_yes].groupby(df['City'])['Restaurant ID'].nunique()
# cidade_mais_restaurantes_com_reserva.sort_values(ascending=False).head(1)

# #7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?


# entregas_yes = df['Is delivering now'] == 'Yes'
# cidade_mais_restuarantes_com_entregas = df[entregas_yes].groupby(df['City'])['Restaurant ID'].count()
# cidade_mais_restaurantes_com_reserva.sort_values(ascending=False).head(1)

# #8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?


# entregas_yes = df['Has Online delivery'] == 'Yes'
# cidade_mais_restuarantes_com_entregas = df[entregas_yes].groupby(df['City'])['Restaurant ID'].count()
# cidade_mais_restaurantes_com_reserva.sort_values(ascending=False).head(1)

st.set_page_config(
    page_title="Cidades",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏙️ Cidades")

st.sidebar.markdown("""---""")
st.sidebar.title('Filtros')

country_options = st.sidebar.multiselect(
     ('Escolha os Paises que Deseja visualizar as Informações'),
    options=sorted(df['City'].dropna().unique()),
    default=sorted(df['City'].dropna().unique())
)

filtro_cidades = df['City'].isin(country_options)
df_cidades = df.loc[filtro_cidades,:]


with st.container():
    se7e_cidade_com_melhores_medias = (df_cidades[df_cidades['Aggregate rating'] > 4.5]
                                       .groupby(['City','Country Name'])['Restaurant ID'].nunique()
                                       .sort_values(ascending=False).head(7)
                                       .reset_index()
)
    fig = px.bar(se7e_cidade_com_melhores_medias, x='City', y='Restaurant ID',
                 title='Top 7 Cidades com mais restaurantes bem avaliados',
                 color='Country Name',
                 labels={
                     'City':'Cidades',
                     'Restaurant ID':'Quantidade de restaurantes'
                 },
                 text='Restaurant ID'
                )
    st.plotly_chart(fig, use_container_width=True)
with st.container():
    top_7_cidades_piores = (df_cidades[df_cidades['Aggregate rating'] < 2.5]
                            .groupby(['City', 'Country Name'])['Restaurant ID']
                            .nunique().reset_index()
                            .sort_values('Restaurant ID', ascending=False).head(7)
)                           
    fig = px.bar(top_7_cidades_piores, x='City', y='Restaurant ID',
                 title='Top 7 Cidades com mais restaurantes mal avaliados',
                 color='Country Name',
                 labels={
                     'City':'Cidades',
                     'Restaurant ID':'Quantidade de restaurantes'
                 },
                 text='Restaurant ID'
                )
    st.plotly_chart(fig, use_container_width=True)
with st.container():
    top_10_cidades_mais_tipos_de_cuisines = (df_cidades.groupby(['City','Country Name'])['Cuisines']
                                             .nunique().sort_values(ascending=False)
                                             .head(10).reset_index())
    fig = px.bar(top_10_cidades_mais_tipos_de_cuisines, x='City', y='Cuisines',
                 title='Top 10 cidades com mais tipos de culinária diferentes',
                 color='Country Name',
                 labels={
                     'City':'Cidades',
                     'Cuisines':'Quantidade de tipos culinários'
                 },
                 text='Cuisines'
                )
    st.plotly_chart(fig, use_container_width=True)