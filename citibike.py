import pandas as pd
import streamlit as st
import numpy as np


st.title('Cicle Rides en NYC')

DATE_COLUMN = 'started_at'
DATA_URL=('citibike-tripdata.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows ,index_col=0, encoding='latin-1')
    return data

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Lilliam Romero Reyes - zs20006765@estudiantes.uv.mx')
data = load_data(500)
st.header("Raw data")

st.sidebar.image("images.jfif")

sidebar = st.sidebar
agree = sidebar.checkbox("Show raw data")
if agree:
    st.dataframe(data)

if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('Numero de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)

hour_to_filter = sidebar.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)