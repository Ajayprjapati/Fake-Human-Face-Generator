import streamlit as st
from tensorflow.keras.models import load_model
from matplotlib import pyplot as plt
from build_generator import Generator
from PIL import Image
import numpy as np
from PIL import Image

generator = Generator('saved_weights/generator_weights.h5')
# generator= None
st.header('Fake Human Face Generator')
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(30, 200, 49);font-size:20px;height:3em;width:30em;
}
</style>""", unsafe_allow_html=True)


image = Image.open('app/temp/temp.png')
st.image(image)
if st.button('Generate'):
    noise = np.random.normal(np.random.normal(0, 1, (1, 100)))
    img = (generator.predict(noise)[0] / 2) + 0.5
    img = np.clip(img, 0, 1)
    plt.imsave('app/temp/temp.png', img)


