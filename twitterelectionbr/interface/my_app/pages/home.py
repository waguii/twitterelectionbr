import streamlit as st
import numpy as np
#from streamlit_card import card
from components.bootstrap import card


# NOTE: This must be the first command in your app, and must be set only once
st.set_page_config(layout="wide")

def css():
    st.markdown(f'''
        <style>
        section[data-testid="stSidebar"] ..css-17ziqus {{width: 14rem;}}
        </style>
    ''',unsafe_allow_html=True)

def main():

    st.markdown("<h1 style='text-align: center; color: white;'>Twiiter Sentiment Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: white;'>Le Wagon 2 Weeks Project - Batch #869 </h5>", unsafe_allow_html=True)

    with st.container():
        st.markdown('## Eleições 2014')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(card(title="Dilma Rousseff", text="PT", image="https://i.imgur.com/l56y2og.jpeg"), unsafe_allow_html=True)
        with col2:
            col2.image("https://i.imgur.com/Y1YI54f.png", width=200)
        # with col3:
            # card(title="Aécio Neves", text="PSDB", image="https://i.imgur.com/SWIzwcx.jpeg")

    with st.container():
        st.markdown('## Eleições 2018')
        col1, col2 = st.columns(2)
        with col1:
            card(title="Fernando Haddad", text="PT", image="https://i.imgur.com/B1TjWfH.jpeg")
        with col2:
            card(title="Jair Bolsonaro", text="PSL", image="https://i.imgur.com/89jXcO6.jpeg")

        st.write("This is inside the container")

    with st.container():
        st.markdown('## Eleições 2022')
        col1, col2 = st.columns(2)
        with col1:
            card(title="Luiz Inácio Lula da Silva", text="PT", image="https://i.imgur.com/MT3O4fy.jpeg")
        with col2:
            card(title="Jair Bolsonaro", text="PL", image="https://i.imgur.com/89jXcO6.jpeg")



css()
main()
