import streamlit as st
import random
from PIL import Image, ImageOps
import numpy as np

import warnings
warnings.filterwarnings("ignore")


st.title("Runway Designer Identification")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.sidebar:
        st.title("Runway Designer")
        st.subheader("Accurate detection of the designer of clothes in the image. This helps an user to easily identify the runway designer.")