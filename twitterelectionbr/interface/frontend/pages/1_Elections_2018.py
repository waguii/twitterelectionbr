import streamlit as st
import numpy as np
from components.bootstrap import card
from static.core_css import main_css
from PIL import Image
import os

Title_html = """
    <style>
        h3{
          font-size: 26px;
          color: #2E2E2E;
          text-align: center;
          font-style: oblique;
          font-weight: bold;

    </style> """

st.set_page_config(layout="wide")

def main():

    st.markdown("<h1 style='text-align: center;'>2018 Elections Analysis</h1>", unsafe_allow_html=True)
    st.markdown(Title_html, unsafe_allow_html=True)
    #WRITE THE CODE BELOW
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 style='text-align: center; color: #FD2B49;'>Fernando Haddad</h1>", unsafe_allow_html=True)
        rel_path = '../static/haddad_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of tweets about Haddad divided by sentiment', use_column_width='auto')
        st.markdown("<h3>There were more negative tweets about Haddad than positive</h3>", unsafe_allow_html=True)

        rel_path = '../static/haddad_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption="Daily tweets about Haddad", use_column_width='auto')
        st.markdown("<h3>People only really started to talk about Haddad around the time he replaced Lula as the candidate for the PT party</h3>", unsafe_allow_html=True)

        rel_path = '../static/haddad_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        st.markdown("<h3>Great majority of users only mention Haddad once</h3>", unsafe_allow_html=True)

        rel_path = '../static/haddad_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users who mentioned Haddad the most', use_column_width='auto')
        st.markdown("<h3>Haddad tweeted about himself more than any other user</h3>", unsafe_allow_html=True)

        rel_path = '../static/haddad_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of likes divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>Positive and negative tweets about Haddad received an equal amount of likes</h3>", unsafe_allow_html=True)

        rel_path = '../static/haddad_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of replies divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>People react more to positive tweets about Haddad</h3>", unsafe_allow_html=True)

        rel_path = '../static/haddad_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of retweeted posts divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>Positive tweets about Haddad have a higher circulation than the positives</h3>", unsafe_allow_html=True)

        rel_path = '../static/haddad_gender.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Users talking about Haddad divided by gender (using picture recognition)', use_column_width='auto')
        st.markdown("<h3>The percentage of male users talking about Haddad is abundantly higher than female</h3>", unsafe_allow_html=True)

        rel_path = '../static/haddad_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiment throughout the year up to the election', use_column_width='auto')
        st.markdown("<h3>There was a mixed general feeling about Haddad throughout the year</h3>", unsafe_allow_html=True)

        rel_path = '../static/haddad_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Negative word cloud about Haddad', use_column_width='auto')
        st.markdown("<h3>Most of the people talking negative things about Haddad do so because of his affiliations with PT party and Lula</h3>", unsafe_allow_html=True)

        rel_path = '../static/haddad_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Positive Word cloud about Haddad', use_column_width='auto')
        st.markdown("<h3>Most of the people talking positive things about Haddad do so because of his affiliations with PT party and Lula</h3>", unsafe_allow_html=True)


    with col2:
        st.markdown("<h1 style='text-align: center; color: #279A55;'>Jair Bolsonaro</h1>", unsafe_allow_html=True)
        rel_path = '../static/bolsonaro_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of tweets about Bolsonar/o divided by sentiment', use_column_width='auto')
        st.markdown("<h3>In general, most of the tweets about Bolsonaro throughout the year are positive</h3>", unsafe_allow_html=True)

        rel_path = '../static/bolsonaro_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Daily tweets about Bolsonaro', use_column_width='auto')
        st.markdown("<h3>People started talking about Bolsonaro earlier in the year</h3>", unsafe_allow_html=True)

        rel_path = '../static/bolsonaro_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        st.markdown("<h3>Great majority of users only mention Bolsonaro once</h3>", unsafe_allow_html=True)

        rel_path = '../static/bolsonaro_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users who mentioned Bolsonaro the most', use_column_width='auto')
        st.markdown("<h3>Bolsonaro is mentioned mostly by personnal accounts</h3>", unsafe_allow_html=True)

        rel_path = '../static/bolsonaro_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of likes divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>Negative tweets about Bolsonaro received more likes than the positives</h3>", unsafe_allow_html=True)

        rel_path = '../static/bolsonaro_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of replies divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>People react more to negative tweets about Bolsonaro</h3>", unsafe_allow_html=True)

        rel_path = '../static/bolsonaro_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of retweeted posts divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>Negative tweets about Bolsonaro have a higher circulation than the positives</h3>", unsafe_allow_html=True)

        rel_path = '../static/bolsonaro_gender.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Users talking about Bolsonaro divided by gender (using picture recognition)', use_column_width='auto')
        st.markdown("<h3>The percentage of male users talking about Bolsonaro is abundantly higher than female</h3>", unsafe_allow_html=True)

        rel_path = '../static/bolsonaro_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiment throughout the year up to the election', use_column_width='auto')
        st.markdown("<h3>Tweets about Bolsonaro are mostly positive and stable throughout the whole year</h3>", unsafe_allow_html=True)

        rel_path = '../static/bolsonaro_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Negative word cloud about Bolsonaro', use_column_width='auto')
        st.markdown("<h3>Tweets with negative sentiment about Bolsonaro are rarely explicit</h3>", unsafe_allow_html=True)

        rel_path = '../static/bolsonaro_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Positive word cloud about Bolsonaro', use_column_width='auto')
        st.markdown("<h3>The majority of positive comments about Bolsonaro are about his military and religious background</h3>", unsafe_allow_html=True)

main_css()
main()
