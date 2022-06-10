import streamlit as st

def bootstrap():
    st.markdown("""<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">""", unsafe_allow_html=True)

def fontawesome():
    st.markdown("""<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" crossorigin="anonymous">""", unsafe_allow_html=True)

def sidebar():
    st.markdown(f'''
        <style>
            section[data-testid="stSidebar"] .css-1siy2j7 {{width: 14rem;}}
            section.main .egzxvld2 {{padding: 0rem 1rem 10rem;}}
        </style>
    ''',unsafe_allow_html=True)

def main_css():
    fontawesome()
    bootstrap()
    sidebar()
