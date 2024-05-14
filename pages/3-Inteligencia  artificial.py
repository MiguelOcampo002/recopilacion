import streamlit as st
import cv2
import numpy as np
#from PIL import Image
from PIL import Image as Image, ImageOps as ImagOps
from keras.models import load_model

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

st.title("Reconocimiento de Imágenes")
st.subheader("Aquí podras hacer el reconocimiento de una imagen sobre tu estado de animo, siendo este capaz de reconocer si tu cara significa que estas bien o estas mal")
st.write("La inteligenci artificial a través del reconocimiento de impagenes tiene la potencialidad de aplicabilidad en la ciudad para optimizar infraestructura de movilidad, salud, lucha contra el cambio climático y demás tópicos, que permiten una toma de desiciones eficaz y en corto tiempo gracias a la movilización de datos y análisis de los mismos realizados por la IA")

img_file_buffer = st.camera_input("Toma una Foto")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
   #To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][0]>0.5:
      st.header('Mike bad, con Probabilidad: '+str( prediction[0][0]) )
    if prediction[0][1]>0.5:
      st.header('Mike good, con Probabilidad: '+str( prediction[0][1]))
    #if prediction[0][2]>0.5:
    # st.header('Derecha, con Probabilidad: '+str( prediction[0][2]))
