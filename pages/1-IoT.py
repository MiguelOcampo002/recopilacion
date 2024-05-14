import pandas as pd
import streamlit as st
from PIL import Image


st.title('Temperatura y humedad, simulación irreal')
image = Image.open('OIP.jpeg')
st.image(image)
st.subheader("la comprensión de los datos pueden potenciar la toma de desiciones de una ciudad")
st.write ("Esta primera página te mostrará los calculos básicos de los datos ingresados por csv sacados a través de la medición de sensores de humedad y temperatura simulados como todo un proyecto de IoT, esto tiene la potencialidad de transformarse en un modelo de análisis automático para tomas de desiciones reactivas y proactivas a según el interés del desarrollador")

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
   df1=pd.read_csv(uploaded_file)
   st.write(df1)
   st.subheader('Estadísticos básicos de los sensores')
   st.dataframe(df1["humedad ESP32"].describe())
else:
 st.warning('Necesitas cargar un archivo csv excel.')
