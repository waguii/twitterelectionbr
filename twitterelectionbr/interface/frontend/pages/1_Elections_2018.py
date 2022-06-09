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
    st.markdown(Title_html, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color:#2E2E2E ;'>Twiitter Sentiment Analysis</h1>", unsafe_allow_html=True)
    #WRITE THE CODE BELOW
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h1 style='text-align: center; color: #FD2B49;'>Fernando Haddad</h1>", unsafe_allow_html=True)
        rel_path = '../static/haddad_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Numbers of tweet written for Haddad by the types of sentiments', use_column_width='auto')
        st.markdown("<h3>Haddad received more negative tweet than positive </h3>", unsafe_allow_html=True)
        
        rel_path = '../static/haddad_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption="Daily numbers of tweet written for Haddad", use_column_width='auto')
        st.markdown("<h3>Haddad become active only in the last month </h3>", unsafe_allow_html=True)
        
        rel_path = '../static/haddad_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        st.markdown("<h3>Candidates are commented only once by most of users during election year</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/haddad_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users tweeted most for Haddad', use_column_width='auto')
        st.markdown("<h3>Haddad tweeted about himself more than any other </h3>", unsafe_allow_html=True)
        
        rel_path = '../static/haddad_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total likes given to sentiments', use_column_width='auto')
        st.markdown("<h3>Positive and negative Tweets about Haddad received balanced likes from users</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/haddad_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of reply given to sentiments', use_column_width='auto')
        st.markdown("<h3>Positive tweets about Haddad are discussed more than the negative ones </h3>", unsafe_allow_html=True)
        
        rel_path = '../static/haddad_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of retweet by sentiments', use_column_width='auto')
        st.markdown("<h3>Positive tweets about Haddad are retweeted more than the negative ones </h3>", unsafe_allow_html=True)
        
        rel_path = '../static/haddad_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiments over the period', use_column_width='auto')
        st.markdown("<h3>Along the election year, users have had indecisive sentiments about Haddad</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/haddad_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of negative tweets for Haddad', use_column_width='auto')
        st.markdown("<h3>Haddad is under the shadow of Lula </h3>", unsafe_allow_html=True)
        
        rel_path = '../static/haddad_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of positivo tweets for Haddad', use_column_width='auto')
        st.markdown("<h3>Users have had difficulty to compliment Haddad  </h3>", unsafe_allow_html=True)


    with col2:
        st.markdown("<h1 style='text-align: center; color: #279A55;'>Jair Bolsonaro</h1>", unsafe_allow_html=True)
        rel_path = '../static/bolsonaro_tweetTotalbySentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Numbers of tweet written for Bolsonaro by the types of sentiments', use_column_width='auto')
        st.markdown("<h3>Bolsonaro is commented positively in most of tweets </h3>", unsafe_allow_html=True)
        
        rel_path = '../static/bolsonaro_numberDailyTweet.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Daily numbers of tweet written for Bolsonaro', use_column_width='auto')
        st.markdown("<h3>Bolsonaro become active earlier than Haddad </h3>", unsafe_allow_html=True)
        
        rel_path = '../static/bolsonaro_avgTweetsbyUser.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average number of tweets by user', use_column_width='auto')
        st.markdown("<h3>Candidates are commented only once by most of users during election year</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/bolsonaro_userTweetedMost.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Top 20 Users tweeted most for Bolsonaro', use_column_width='auto')
        st.markdown("<h3>Bolsonaro is commented by mostly personal accounts</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/bolsonaro_likesForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total likes given to sentiments', use_column_width='auto')
        st.markdown("<h3>Negative tweets about Bolsonaro received likes more than the positives ones</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/bolsonaro_replyForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of reply given to sentiments', use_column_width='auto')
        st.markdown("<h3>Negative tweets about Bolsonaro are discussed more than the positives ones</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/bolsonaro_retweetForSentiments.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Total number of retweet by sentiments', use_column_width='auto')
        st.markdown("<h3>Negative tweets about Bolsonaro are retweeted more than the positives ones</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/bolsonaro_sentimentsOvertime.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Average sentiments over the period', use_column_width='auto')
        st.markdown("<h3>Along the election year, tweets about Bolsonaro are mostly positive and stable </h3>", unsafe_allow_html=True)
        
        rel_path = '../static/bolsonaro_wordCloudNegativo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of negative tweets for Bolsonaro', use_column_width='auto')
        st.markdown("<h3>Critics about Bolsonaro are not necessarily negative</h3>", unsafe_allow_html=True)
        
        rel_path = '../static/bolsonaro_wordCloudPositivo.png'
        abs_file_path = os.path.join(script_dir, rel_path)
        image = Image.open(abs_file_path)
        st.image(image, caption='Word cloud of positivo tweets for Bolsonaro', use_column_width='auto')
        st.markdown("<h3>Positive tweets about Bolsonaro have religious and militar sentiments </h3>", unsafe_allow_html=True)

main()
