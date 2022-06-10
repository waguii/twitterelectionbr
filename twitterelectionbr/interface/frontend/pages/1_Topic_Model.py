import streamlit as st
import streamlit.components.v1 as components
import os

Title_html = """
    <style>
        h3{
          font-size: 26px;
          color: #2E2E2E;
          text-align: center;
          font-style: oblique;
          font-weight: bold;
          width: 100%;

    </style> """

st.set_page_config(layout="wide")

script_dir = os.path.dirname(__file__)

# st.markdown("<h1 style='text-align: center;'>Topic Modelling</h1>", unsafe_allow_html=True)


rel_path = '../static/graficos/dilma_topic_overtime.html'
abs_file_path = os.path.join(script_dir, rel_path)

HtmlFile = open(abs_file_path, 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, height=400, width=1250)
st.markdown("<h3>Debates organized by TV channels is the main dominant topic in the final stage of election campaign </h3>", unsafe_allow_html=True)

rel_path = '../static/graficos/dilma_TopicDistance.html'
abs_file_path = os.path.join(script_dir, rel_path)

HtmlFile = open(abs_file_path, 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, height=500, width=1250)

st.markdown("<h3>Governmental social schemes like Bolsa Familia, the world cup and  the results of polling institutions \
            are the main topics discussed during the election campaign </h3>", unsafe_allow_html=True)


rel_path = '../static/graficos/dilma_hierarchicalCluster.html'
abs_file_path = os.path.join(script_dir, rel_path)

HtmlFile = open(abs_file_path, 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, height=500, width=1250)
