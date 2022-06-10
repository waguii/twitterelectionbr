import streamlit as st
import numpy as np
from components.bootstrap import card
from static.core_css import main_css
from PIL import Image
import os
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

def main():

    #st.title("Candidates activity on Twitter during campaign")
    st.markdown("<h1 style='text-align: center;'>Candidates activity on Twitter during campaign</h1>", unsafe_allow_html=True)

    components.iframe('https://app.powerbi.com/view?r=eyJrIjoiODc3N2RhNDctM2NkOS00YTEyLThkMjQtOTdkMTcyYjU0MjkzIiwidCI6IjU3YjJhZDI2LWM4YTgtNDNlOC1iMTk4LWM4NzU4YzU1MDQyOSJ9',
                    height = 650)

main_css()
main()
