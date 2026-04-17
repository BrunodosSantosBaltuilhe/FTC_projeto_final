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

# #1. Qual o nome do restaurante que possui a maior quantidade de avaliações?


# maior_qtda_aval = df['Votes'].groupby(df['Restaurant Name']).sum()
# maior_qtda_aval.sort_values(ascending=False).head(1)

# #2. Qual o nome do restaurante com a maior nota média?


# maior_nota_media = df['Aggregate rating'].groupby(df['Restaurant Name']).mean()
# maior_nota_media.sort_values(ascending=False).head(1)

# #3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?


# maior_preço_prato_para_dois = df['Average Cost for two'].groupby(df['Restaurant Name']).max()
# maior_preço_prato_para_dois.sort_values(ascending=False).head(1)

# #4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?


# culinaria_brasileira = df['Cuisines'] == 'Brazilian'
# menor_media_brasileira = df.loc[culinaria_brasileira,['Restaurant Name', 'Aggregate rating']].groupby('Restaurant Name').agg({'Aggregate rating':'mean'})
# menor_media_brasileira.sort_values(by='Aggregate rating',ascending=True).head()

# #5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?


# culinaria_brasileira = df['Cuisines'] == 'Brazilian'
# restaurante_brasileiro = df['Country Name'] == 'Brazil'
# maior_media_brasileira = df.loc[culinaria_brasileira & restaurante_brasileiro,['Restaurant Name', 'Aggregate rating']].groupby('Restaurant Name').agg({'Aggregate rating':'mean'})
# maior_media_brasileira.sort_values(by='Aggregate rating',ascending=False).head(1)

# #6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?


# media_aval_online = df.loc[:,['Has Online delivery','Votes']].groupby('Has Online delivery').agg({'Votes':'mean'})
# media_aval_online.sort_values(by='Votes',ascending=False)

# #7. Os restaurantes que fazem reservas são também, na média, os restaurantes quepossuem o maior valor médio de um prato para duas pessoas?


# restaurantes_reservas = df.loc[:, ['Has Table booking', 'Average Cost for two']].groupby('Has Table booking').agg({'Average Cost for two':'mean'})
# restaurantes_reservas.sort_values(by='Average Cost for two', ascending=False)

# #8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?


# american_country_att = df['Country Name'] == 'United States of America'

# american_cuisines_japan = df['Cuisines'] == 'Japanese'
# american_cuisines_bbq = df['Cuisines'] == 'BBQ'

# american_cost_per_japanese= (df.loc[american_country_att  & american_cuisines_japan, ['Cuisines','Average Cost for two']].groupby('Cuisines').agg({'Average Cost for two':'mean'}))
# american_cost_per_bbq= (df.loc[american_country_att  & american_cuisines_bbq, ['Cuisines', 'Average Cost for two']].groupby('Cuisines').agg({'Average Cost for two':'mean'}))

# american_cost_per_japanese, american_cost_per_bbq

import streamlit as st

st.set_page_config(
    page_title="Restaurantes",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🍽️ Restaurantes")

with st.sidebar:
    st.title('Filtros')
    st.markdown("""---""")
    st.write('Escolha os Países que deseja visualizar as Informações')
    paises_selecionados = st.multiselect(
        label='Países',
        options=sorted(df['Country Name'].unique()),
        default=sorted(df['Country Name'].unique()),
        label_visibility='collapsed'
)
    st.markdown("""---""")
    qtda_restaurantes = st.slider(
        'Quantos restaurantes quer selecionar',
        min_value=1,
        max_value=20,
        value=10
    )
    st.markdown("""---""")
    st.write('Escolha os tipos de culinária que deseja filtrar')
    tipos_culinaria = st.multiselect(
        label='Tipo Culinário',
        options=sorted(df['Cuisines'].unique()),
        default=sorted(df['Cuisines'].unique()),
        label_visibility='collapsed'
    )
df_aux= df[df['Country Name'].isin(paises_selecionados) & df['Cuisines'].isin(tipos_culinaria)]
with st.container():
    st.header('Top Resaturantes no mundo')
    top_10 = df_aux.sort_values(by='Aggregate rating', ascending=False).head(qtda_restaurantes).loc[:, ['Restaurant ID','Restaurant Name',
                                                                            'Country Name','City','Cuisines',
                                                                            'Average Cost for two','Aggregate rating','Votes']]
    st.dataframe(top_10, use_container_width=True)
with st.container():
    top_10_cuisines = (df_aux.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
                                                                 .reset_index().head(qtda_restaurantes))
    fig = px.bar(top_10_cuisines, x='Cuisines', y='Aggregate rating',
                 title='Top tipos de Culinária',
                 labels={
                     'Cuisines':'Tipos de Culinária',
                     'Aggregate rating':'Média'
                 },
                 text='Aggregate rating'
                )
    st.plotly_chart(fig, use_container_width=True)