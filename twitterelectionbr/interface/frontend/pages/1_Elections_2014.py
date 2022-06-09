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


def main():
    st.set_page_config(layout="wide")
    st.markdown("<h1 style='text-align: center; color:#2E2E2E ;'>Twiitter Sentiment Analysis</h1>", unsafe_allow_html=True)
    #WRITE THE CODE BELOW
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 style='text-align: center; color: #FD2B49;'>Dilma Rousseff</h1>", unsafe_allow_html=True)
        rel_path = '../static/dilma_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Numbers of tweet written for Dilma by the types of sentiments', use_column_width='auto')
        st.markdown("<h3>Dilma received more negative tweets but the number of positive tweets is still higher than Aécio's</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/dilma_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Daily numbers of tweet written for Dilma', use_column_width='auto')
        st.markdown("<h3>Dilma is active in Tweeter along the year of elections</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/dilma_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        st.markdown("<h3>Candidates are commented only once by most of users during election year</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/dilma_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users tweeted most for Dilma', use_column_width='auto')
        st.markdown("<h3>Dilma is commented mostly by institutional accounts</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/dilma_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total likes given to sentiments', use_column_width='auto')
        st.markdown("<h3>Positive and negative tweets about Dilma received equal amounts of likes</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/dilma_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of reply given to sentiments', use_column_width='auto')
        st.markdown("<h3>Positive and Negative tweets about Dilma creates almost equal amount of discussions </h3>", unsafe_allow_html=True)
        
        rel_path = '../static/dilma_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of retweet by sentiments', use_column_width='auto')
        st.markdown("<h3>Positive tweets about Dilma are circulated more than the negative one's</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/dilma_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiments over the period', use_column_width='auto')
        st.markdown("<h3>Average sentiments about Dilma is usually negative but differs less along the year</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/dilma_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of negative tweets for Dilma', use_column_width='auto')
        st.markdown("<h3>The world cup and the Petrobras scandal dominate the negative tweets about Dilma</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/dilma_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of positivo tweets for Dilma', use_column_width='auto')
        st.markdown("<h3>Positive tweets about Dilma points out the legacy of PT</h3>", unsafe_allow_html=True)


    with col2:
        st.markdown("<h1 style='text-align: center; color: #279A55;'>Aécio Neves</h1>", unsafe_allow_html=True)
        rel_path = '../static/aecio_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Numbers of tweet written for Aécio by the types of sentiments', use_column_width='auto')
        st.markdown("<h3>The number of tweets about Aécio is less than the Dilma's but positive and negative tweets are balanced</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/aecio_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Daily numbers of tweet written for Aécio', use_column_width='auto')
        st.markdown("<h3>Tweeters about Aécio jumps up just before the elections </h3>", unsafe_allow_html=True)

        
        rel_path = '../static/aecio_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        st.markdown("<h3>Candidates are commented only once by most of users during election year</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/aecio_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users tweeted most for Aécio', use_column_width='auto')
        st.markdown("<h3>Aécio is commented mostly by personal accounts</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/aecio_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total likes given to sentiments', use_column_width='auto')
        st.markdown("<h3>Negative tweets about Aécio received likes more than the positives one's</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/aecio_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of reply given to sentiments', use_column_width='auto')
        st.markdown("<h3>Negative tweets about Aécio are discussed more than the positives one's</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/aecio_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of retweet by sentiments', use_column_width='auto')
        st.markdown("<h3>Negative tweets about Aécio are circulated more than the positives one's</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/aecio_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiments over the period', use_column_width='auto')
        st.markdown("<h3>Average sentiments about Aécio is not stable and differs much along the year</h3>", unsafe_allow_html=True)
        
        
        rel_path = '../static/aecio_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of negative tweets for Aécio', use_column_width='auto')
        st.markdown("<h3>Discussion between political parties dominates the negative tweets about Aécio</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/aecio_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of positivo tweets for Aécio', use_column_width='auto')
        st.markdown("<h3>Positive tweets about Aécio looks for the support of Marina in the second round</h3>", unsafe_allow_html=True)

main()
