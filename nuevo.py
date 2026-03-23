# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:51:59 2026

@author: LENOVO
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import os
import warnings
warnings.filterwarnings("ignore")

df= pd.read_csv("C:/Users/LENOVO/Downloads/practica dashboard/World Energy Consumption.csv")

st.set_page_config(page_title="Dashboard consumos Charlx", layout="wide")

st.title("Dashboard Charly") 


#este es para crear un boton (barra), para seleccionar pais
st.sidebar.header("Seleccione un pais") #crea una barra
seleccionar_pais = st.sidebar.multiselect("seleccione un pais",df["country"].unique(),default=df["country"].unique())
#el multiselec nos permite seleccionar varios botones

#este nos permitira seleccionar el año, ele selec nos permitira seleccionar solo UN AÑO
seleccione_año = st.sidebar.selectbox("selccione un año",df["year"].unique())

#este nos permite seleccionar la variable de su comportamiento
seleccione_columnas = st.sidebar.selectbox("seleccione una variable", df.columns[3:])

#mostraremos el dashboard
df= df[df["country"].isin(seleccionar_pais)& (df["year"]>= seleccione_año)]
if st.checkbox("vea parte del dataframe"):
    with st.expander("describe el dataframe"):
        st.subheader("descripcion del dataframe")
        st.write(df)
    with st.expander("valores estadisticos"):
        st.subheader("mostrar valores estadisticos")
        st.write(df.describe())
#esto crea pestañas para mostrar nuestro dataframe

st.subheader("comportamiento de la variable seleccionado")
fig_line = px.line(df, x="year", y= seleccione_columnas, color = "country", hover_name="country", title= f"comportamiento de {seleccione_columnas}")
st.plotly_chart(fig_line)