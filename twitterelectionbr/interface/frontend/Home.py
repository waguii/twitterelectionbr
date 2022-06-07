import streamlit as st
from static.core_css import main_css

# NOTE: This must be the first command in your app, and must be set only once
st.set_page_config(layout="wide")

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>Twiitter Sentiment Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: white;'>Le Wagon Brazil - Batch #869 </h5>", unsafe_allow_html=True)
    st.write('Collect tweets using the twitter api (snsscrape) for keywords and hashtags with publish date close(first day of year util last day of election) to the election period and then try to create a dataset containing the tweets content and author details.')

main_css()
main()
