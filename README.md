# Fome Zero

Dashboard interativo desenvolvido em **Python** com **Streamlit** para análise de dados de restaurantes da base do Zomato.

## Sobre o projeto

O projeto tem como objetivo explorar informações sobre restaurantes, países, cidades, avaliações, culinárias e localização geográfica, apresentando os dados de forma visual e interativa.

A aplicação foi estruturada em diferentes visões analíticas, permitindo ao usuário navegar entre páginas específicas e aplicar filtros para explorar os dados.

## Funcionalidades

### Página inicial
- Exibição de indicadores gerais da base:
  - restaurantes cadastrados
  - países cadastrados
  - cidades cadastradas
  - total de avaliações
  - total de culinárias
- Mapa interativo com a localização dos restaurantes

### Visão por países
- Filtro por país
- Controle da quantidade de restaurantes exibidos
- Gráficos com:
  - quantidade de restaurantes por país
  - quantidade de cidades por país
  - média de avaliações por país
  - avaliação média por país

### Visão por cidades
- Filtro por cidade
- Gráficos com:
  - top 7 cidades com mais restaurantes bem avaliados
  - top 7 cidades com mais restaurantes mal avaliados
  - top 10 cidades com mais tipos de culinária diferentes

### Visão por restaurantes
- Filtro por país
- Filtro por tipo de culinária
- Controle da quantidade de restaurantes exibidos
- Tabela com os principais restaurantes
- Gráfico com os tipos de culinária mais bem avaliados

## Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- Plotly Express
- Plotly Graph Objects
- Folium
- Streamlit Folium
- NumPy

## Estrutura do projeto

```bash
.
├── Página_Inicial.py
├── 🌍_Países.py
├── 🏙️_Cidades.py
├── 🍽️_Restaurantes.py
└── zomato_corrigido_para_analise.csv
