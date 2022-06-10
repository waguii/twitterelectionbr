from os import uname
import streamlit as st
import requests
from static.core_css import main_css
from components.bootstrap import profile_card, count_card
from core.consts import *
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

st.set_page_config(layout="wide")

def custom_css():
    st.markdown("""<style>
.card-counter{
    margin: 5px;
    padding: 20px 10px;
    background-color: #fff;
    height: 100px;
    border-radius: 5px;
  }

  .card-counter.primary{
    background-color: #007bff;
    color: #FFF;
  }

  .card-counter.danger{
    background-color: #ef5350;
    color: #FFF;
  }

  .card-counter.success{
    background-color: #66bb6a;
    color: #FFF;
  }

  .card-counter.info{
    background-color: #26c6da;
    color: #FFF;
  }

  .card-counter i{
    font-size: 5em;
    opacity: 0.2;

  }

  .card-counter .count-numbers{
    position: absolute;
    right: 35px;
    top: 20px;
    font-size: 32px;
    display: block;
  }

  .card-counter .count-name{
    position: absolute;
    right: 35px;
    top: 65px;
    font-style: italic;
    text-transform: capitalize;
    opacity: 0.5;
    display: block;
    font-size: 18px;
  }</style>""", unsafe_allow_html=True)

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

    fig_to = px.histogram(df_to, x="date", y="compound", color="sentiment", height=400, barmode='group', histfunc='avg')
    fig_from = px.histogram(df_from, x="date", y="compound", color="sentiment", height=400, histfunc='avg')

    fig_to.update_xaxes(rangeslider_visible=True)
    fig_from.update_xaxes(rangeslider_visible=True)

    st.markdown(f"#### Sentiment from {name} tweets")
    st.plotly_chart(fig_to, use_container_width=True)

    st.markdown(f"#### Sentiment of tweets to {name}")
    st.plotly_chart(fig_from, use_container_width=True)

def plot_heat_map(raw):

    # df = pd.read_json(raw)

    # fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
    #                     center=dict(lat=0, lon=180), zoom=0,
    #                     mapbox_style="stamen-terrain")
    # fig.show()
    pass

def plot_most_common_words(words):

    #remove empty words
    words = [x for x in words if x]
    most_common_words = Counter(words).most_common(10)

    #create a new dadtaframe with only two columns
    df = pd.DataFrame(most_common_words, columns = ['Word', 'Count'])

    #fig = px.bar(df, x='Count', y='Word', orientation='h')

    st.markdown(f"#### Most common words")

    fig = px.bar(df, x='Count', y='Word', color = 'Word', orientation='h')
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

    #st.plotly_chart(fig, use_container_width=True)

def plot_word_cloud(words):

    #remove empty words
    words = [x for x in words if x]
    word_counter = Counter(words)

    wordcloud = WordCloud(background_color='white', width = 1000, height = 500).generate_from_frequencies(word_counter)


    fig = plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")

    st.markdown(f"#### Wordcloud")
    st.pyplot(fig,use_container_width=True)

def plot_geo_map(df_json):
    pass
    # df = pd.read_json(df_json)

    # try:
    #     geolocator = Nominatim(user_agent = "my project app")
    #     local  = geolocator.geocode(location).point
    #     latitude = local[0]
    #     longitude = local[1]
    # except:
    #     latitude = locations_dic.get('brasil')[0]
    #     longitude = locations_dic.get('brasil')[1]

def main():
    if 'results' not in st.session_state:
        st.markdown("<h1 style='text-align: center;'>Candidate analysis</h1>", unsafe_allow_html=True)
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
        # raw_data = st.session_state.results['raw']
        detail = st.session_state.results['detail']

        with col1:
            plot_most_common_words(tweets_analysis['words'])

            plot_word_cloud(tweets_analysis['words'])

        with col2:
            profile_card(profile)

            nlp_total = detail['sentiment_counts']['pos'] + \
                        detail['sentiment_counts']['neg'] + \
                        detail['sentiment_counts']['neu']

            percentage_pos = round(detail['sentiment_counts']['pos'] / nlp_total * 100)
            percentage_neg = round(detail['sentiment_counts']['neg'] / nlp_total * 100)
            percentage_neu = round(detail['sentiment_counts']['neu'] / nlp_total * 100)

            count_card(percentage_neu, 'neutral', 'info')
            count_card(percentage_pos, 'positive', 'success')
            count_card(percentage_neg, 'negative', 'danger')


        plot_nlp_ver_time(tweets_analysis['nlp'], profile['displayname'])

main_css()
custom_css()
main()
