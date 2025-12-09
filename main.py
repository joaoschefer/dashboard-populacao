import streamlit as st
import pandas as pd
import plotly.express as px

# carregar dataset
df = pd.read_csv("world_population.csv")
st.set_page_config(page_title="Dashboard População Mundial", layout="wide")
st.title("Dashboard de População Mundial")
st.write("Visualização interativa baseada no dataset de população mundial.")

# sidebar
st.sidebar.header("Filtros")

continentes = st.sidebar.multiselect(
    "Selecione os continentes:",
    options=df["Continent"].unique(),
    default=df["Continent"].unique()
)

df_filtrado = df[df["Continent"].isin(continentes)]

# métricas
col1, col2, col3 = st.columns(3)

col1.metric("Total de Países", df_filtrado.shape[0])
col2.metric("População Total (2023)", f"{df_filtrado["2022 Population"].sum():,}")
col3.metric("Maior População", f"{df_filtrado['2022 Population'].max():,}")

# gráfico 1
st.subheader("Top 10 Países Mais Populosos (2023)")
top10 = df_filtrado.nlargest(10, "2022 Population")

fig1 = px.bar(
    top10,
    x="Country/Territory",
    y="2022 Population",
    color="Continent",
    title="Top 10 Populações (2023)",
)
st.plotly_chart(fig1, use_container_width=True)

# grafico 2
st.subheader("Distribuição Populacional por Continente")

fig2 = px.pie(
    df_filtrado,
    names="Continent",
    values="2022 Population",
    title="Participação dos Continentes na População Mundial",
)
st.plotly_chart(fig2, use_container_width=True)

# grafico 3
st.subheader("Crescimento Populacional por País")

fig3 = px.scatter(
    df_filtrado,
    x="Growth Rate",
    y="2022 Population",
    size="2022 Population",
    color="Continent",
    hover_name="Country/Territory",
    title="Taxa de Crescimento vs População",
)
st.plotly_chart(fig3, use_container_width=True)

# tabela
st.subheader("Tabela Completa Filtrada")
st.dataframe(df_filtrado)