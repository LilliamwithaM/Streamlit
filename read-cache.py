import pandas as pd
import streamlit as st


st.title("Streamlit con atributo cache")

DATA_URL = "dataset.csv"

@st.cache

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data__load_state = st.text("Loading data...")
data = load_data(13)
data__load_state.text("Done! (using st.cache)")

st.dataframe(data)