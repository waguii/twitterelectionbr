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

    st.markdown("<h1 style='text-align: center;'>2014 Elections Analysis</h1>", unsafe_allow_html=True)
    #WRITE THE CODE BELOW
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 style='text-align: center; color: #FD2B49;'>Dilma Rousseff</h1>", unsafe_allow_html=True)
        rel_path = '../static/dilma_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of tweets about Dilma divided by sentiment', use_column_width='auto')
        st.markdown("<h3>Dilma received more negative tweets but the number of positive tweets is still higher than Aécio's</h3>", unsafe_allow_html=True)

        rel_path = '../static/dilma_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Daily tweets about Dilma', use_column_width='auto')
        st.markdown("<h3>Peaks of tweets about Dilma around the World Cup and increase near the elections </h3>", unsafe_allow_html=True)

        rel_path = '../static/dilma_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        st.markdown("<h3>Great majority of users only mention Dilma once</h3>", unsafe_allow_html=True)

        rel_path = '../static/dilma_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users who mentioned Dilma the most', use_column_width='auto')
        st.markdown("<h3>Dilma is mostly mentioned by institutional accounts</h3>", unsafe_allow_html=True)

        rel_path = '../static/dilma_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of likes divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>Positive and negative tweets about Dilma received an equal amount of likes</h3>", unsafe_allow_html=True)

        rel_path = '../static/dilma_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of replies divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>Positive and negative tweets about Dilma are equally discussed</h3>", unsafe_allow_html=True)

        rel_path = '../static/dilma_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of retweeted posts divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>Positive tweets about Dilma have a higher circulation than the negatives</h3>", unsafe_allow_html=True)

        rel_path = '../static/dilma_gender.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Users by machine-identified gender', use_column_width='auto')
        st.markdown("<h3>The percentage of male users talking about Dilma is greater than female</h3>", unsafe_allow_html=True)

        rel_path = '../static/dilma_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiment throughout the year up to the election', use_column_width='auto')
        st.markdown("<h3>The average sentiment about Dilma is negative, but with lower variance, and with a positive peak in the end</h3>", unsafe_allow_html=True)

        rel_path = '../static/dilma_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Negative word cloud about Dilma', use_column_width='auto')
        st.markdown("<h3>The World Cup and the Petrobras scandal dominate the negative tweets about Dilma</h3>", unsafe_allow_html=True)

        rel_path = '../static/dilma_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Positive word cloud about Dilma', use_column_width='auto')
        st.markdown("<h3>Positive tweets about Dilma points out the legacy of PT</h3>", unsafe_allow_html=True)


    with col2:
        st.markdown("<h1 style='text-align: center; color: #279A55;'>Aécio Neves</h1>", unsafe_allow_html=True)
        rel_path = '../static/aecio_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of tweets about Aécio divided by sentiment', use_column_width='auto')
        st.markdown("<h3>Less people mentioned Aécio, but there is a balance between positive and negative tweets</h3>", unsafe_allow_html=True)

        rel_path = '../static/aecio_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Daily tweets about Aécio', use_column_width='auto')
        st.markdown("<h3>People started mentioning Aécio more towards the end of the campaign.</h3>", unsafe_allow_html=True)


        rel_path = '../static/aecio_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        st.markdown("<h3>Great majority of users only mention Aécio once</h3>", unsafe_allow_html=True)

        rel_path = '../static/aecio_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users who mentioned Aécio the most', use_column_width='auto')
        st.markdown("<h3>Aécio is mostly mentioned by personnal accounts</h3>", unsafe_allow_html=True)

        rel_path = '../static/aecio_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of likes divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>Negative tweets about Aécio received more likes than the positives</h3>", unsafe_allow_html=True)

        rel_path = '../static/aecio_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of replies divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>People react more to negative tweets about Aécio</h3>", unsafe_allow_html=True)

        rel_path = '../static/aecio_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Amount of retweeted posts divided by general sentiment', use_column_width='auto')
        st.markdown("<h3>Negative tweets about Dilma have a higher circulation than the positives</h3>", unsafe_allow_html=True)

        rel_path = '../static/aecio_gender.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Users by machine-identified gender', use_column_width='auto')
        st.markdown("<h3>The percentage of male users talking about Aécio is greater than female</h3>", unsafe_allow_html=True)

        rel_path = '../static/aecio_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiment throughout the year up to the election', use_column_width='auto')
        st.markdown("<h3>The sentiment about Aécio has more variance, representing more extrem opinions, with a negative peak in the end</h3>", unsafe_allow_html=True)


        rel_path = '../static/aecio_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Negative word cloud about Aécio', use_column_width='auto')
        st.markdown("<h3>Discussion between political parties dominates the negative tweets about Aécio</h3>", unsafe_allow_html=True)

        rel_path = '../static/aecio_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Positive word cloud about Aécio', use_column_width='auto')
        st.markdown("<h3>The support of ex-candidate Marina stands out in the positive tweets</h3>", unsafe_allow_html=True)

main_css()
main()
