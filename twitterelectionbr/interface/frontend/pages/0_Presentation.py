import streamlit as st
import numpy as np
from components.bootstrap import card
from static.core_css import main_css
from PIL import Image
import os
import streamlit.components.v1 as components

def main():
    st.set_page_config(layout="wide")
    st.title("Candidates activity on Twitter during campaign")


    components.iframe('https://app.powerbi.com/view?r=eyJrIjoiMTYyYTViNTgtZTBhNC00YmFmLTljZTYtM2M4YTkwOTFkNTI2IiwidCI6IjU3YjJhZDI2LWM4YTgtNDNlOC1iMTk4LWM4NzU4YzU1MDQyOSJ9',
                    height = 600)
main()
