import streamlit as st
import streamlit.components.v1 as components
import os

script_dir = os.path.dirname(__file__) 

st.title("Topic Modelling")

rel_path = '../static/graficos/dilma_topic_overtime.html'
abs_file_path = os.path.join(script_dir, rel_path)

HtmlFile = open(abs_file_path, 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=500, width=1250)


rel_path = '../static/graficos/dilma_TopicDistance.html'
abs_file_path = os.path.join(script_dir, rel_path)

HtmlFile = open(abs_file_path, 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=500, width=1250)


rel_path = '../static/graficos/dilma_hierarchicalCluster.html'
abs_file_path = os.path.join(script_dir, rel_path)

HtmlFile = open(abs_file_path, 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=500, width=1250)