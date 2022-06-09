import streamlit as st
import requests
from static.core_css import main_css
from components.bootstrap import profile_card
from core.consts import *
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

def clear_results():
    # Delete all the items in Session state
    for key in st.session_state.keys():
        del st.session_state[key]

def search():
    twiiter_username = st.session_state.username
    #with st.spinner("Carregando..."):
    headers = {"accept": "application/json"}

    params = {"twiitter_profile": twiiter_username}
    results = requests.get(f'{API_BASE_URL + API_ENDPOINT_ANALYSIS}',headers=headers,params=params).json()

    if 'error' not in results:
        st.session_state.results = results
    else:
        st.session_state.results_error = results
        #print(results)

def plot_nlp_ver_time(nlp, name):
    columns = nlp.keys()

    df = pd.DataFrame( columns=columns)
    df['date'] = nlp['date']
    df['created_at_r'] = nlp['created_at_r']
    df['created_at_r2'] = nlp['created_at_r2']
    df['compound'] = nlp['compound']
    df['sentiment'] = nlp['sentiment']
    df['direction'] = nlp['direction']

    df_to = df[df['direction'] == 'to']
    df_from = df[df['direction'] == 'from']

    fig_to = px.bar(df_to, x="date", y="compound")
    fig_from = px.bar(df_from, x="date", y="compound", labels=['1','2'])

    st.markdown(f"#### Tweets from {name}")
    st.plotly_chart(fig_to, use_container_width=True)

    st.markdown(f"#### Tweets from {name}")
    st.plotly_chart(fig_from, use_container_width=True)



def main():
    if 'results' not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: white;'>Anyone can be analysed?</h1>", unsafe_allow_html=True)
        st.text_input(key='username', label='', placeholder='Type a Twitter username to look up their stats.', on_change=search)
        if 'results_error' in st.session_state:
            st.error(st.session_state.results_error['error'])
    else:
        st.button('🔍 New search', on_click = clear_results)

        #grid
        col1, col2 = st.columns([2, 1])

        #variables
        profile = st.session_state.results['profile']
        profile_analysis = st.session_state.results['profile_analysis']
        tweets_analysis = st.session_state.results['tweets_analysis']
        raw_data = st.session_state.results['raw']
        detail = st.session_state.results['detail']

        with col1:
            #st.subheader(f"{profile['displayname']} - Analysis")
            plot_nlp_ver_time(tweets_analysis['nlp'], profile['displayname'])

        with col2:
            profile_card(profile)


main_css()
main()
