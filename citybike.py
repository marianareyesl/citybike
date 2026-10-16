import pandas as pd
import streamlit as st

st.title('Bicicletas en New York')

DATA_URL = 'https://raw.githubusercontent.com/marianareyesl/citybike/refs/heads/main/citibike-tripdata.csv'

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'start_lat': 'lat', 'start_lng': 'lon'}, inplace=True)
    data['started_at'] = pd.to_datetime(data['started_at'])
    return data

data = load_data(1000)

st.sidebar.write('Barra:')

mostrar_datos = st.sidebar.checkbox('Mostrar datos')
mostrar_grafica = st.sidebar.checkbox('Mostrar gráfica')
hour_to_filter = st.sidebar.slider('hora', 0, 23, 12)

if mostrar_datos:
    st.dataframe(data)

if mostrar_grafica:
    st.bar_chart(data['started_at'].dt.hour.value_counts().sort_index())

filtered_data = data[data['started_at'].dt.hour == hour_to_filter]

st.map(filtered_data)

st.write ("Mariana Reyes")
