import streamlit as st

#titulo del content
st.title("App con sidebar")

sidebar = st.sidebar

sidebar.title("Esta es la barra lateral.")

sidebar.write("Datos del sidebar")

st.header("Información sobre el Conjunto de datos")
st.header("Descripción de los datos")
st.write("Datos del content")

