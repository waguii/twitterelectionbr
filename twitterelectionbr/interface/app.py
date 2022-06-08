import streamlit as st
import datetime
import requests

#from streamlit.components.v1 import html
import streamlit.components.v1 as components

with st.form(key='my_form'):
	text_input = st.text_input(label='Enter a username of twitter')
	submit_button = st.form_submit_button(label='Submit')

if submit_button:
    response = requests.get(f'http://localhost:8000/data?username={text_input}')
    st.write(response.text)




st.title("Javascript example")
HtmlFile = open("htmls/topic_overtime.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height=500, width=1250)

