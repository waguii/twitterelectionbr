from pyrsistent import s
import streamlit as st
from static.core_css import main_css

def custom_css():
    st.markdown("""<style>
                .css-1fcdlhc{
                    margin-inline: 8rem;
                }
                </style>""", unsafe_allow_html=True)

# NOTE: This must be the first command in your app, and must be set only once
st.set_page_config(layout="wide")

def main():
    st.markdown("""<div class="container">
                    <div class="row justify-content-md-center">
                        <h1>Just Tweet It</h1>
                    </div>
                   </div>""", unsafe_allow_html=True)
    st.markdown("""<div class="container">
                    <div class="row justify-content-md-center">
                        <h5>Le Wagon Brazil - <b>Batch #869</b></h5>
                    </div>
                   </div>""", unsafe_allow_html=True)

    st.markdown("""
                <div class="container">
                    <div class="row justify-content-md-center">
                        <div class="col-md-10">
                            Just Tweet It is a sentiment analysis tool designed as final project for the Le Wagon Data Science bootcamp.
                            Its ultimate purpose is to perform a thorough analysis of the general popular sentiment around an individual,
                            product, company or even a specific term, while also getting usefull information, like number of followers,
                            tweets, replies etc. For this showcase, we chose to apply it to the political scenario
                            around the 2014 and 2018 presidential elections in Brazil, analysing what was the public's opinion
                            about the two main candidates in each year, but it can be used for inumerous situtaions.
                            You choose the word and Just Tweet It does the work!
                        </div>
                    </div>
                </div>""",unsafe_allow_html=True)

    st.markdown("""
                <div class="container mt-5">
                    <div class="row justify-content-md-center">
                        <h3 style='text-align: left;'>How does it work?</h3>
                    </div>
                </div>""", unsafe_allow_html=True)


    # st.markdown("""<div class="container">
    #                 <div class="row justify-content-md-center">""", unsafe_allow_html=True)



    expander = st.expander('Collecting data')

    expander.write("""
                   Just Tweet It uses the Twitter api to collect all tweets
                   published using the chosen keyword (snsscrape), inside a alterable period
                   of time and creates a dataset containing the tweet itself and, among other
                   information, who tweeted it, how many likes
                   and replies it got and the number of followers the user who tweeted has at the moment of the search.""")

    expander1 = st.expander('Getting the sentiment')

    expander1.write("""
                    With the ready dataset, Just Tweet It does a sentiment analysis for the tweets,
                    classifying each into 3 categories: positive, negative and neutral, based on
                    keywords utilized by the users.
                    """)

    expander3= st.expander('Engineering features')

    expander3.write('''
                    This is the part where Just Tweet It generate some data based on
                    information from the users: from the location provided, it pin points
                    the geographical coordenades of the user; from the profile picture,
                    it classifies each user into two categories, male and female, based on
                    photo recognition and statistical probability. This is very useful to
                    get a demographic sense of the public you are reaching.
                    ''')

    expander2 = st.expander('Generating report')

    expander2.write('''
                    After all the previous steps, Just Tweet It sets out to
                    generate several useful and easy-to-read graphics. With them,
                    the user get information like: do people react better to positive
                    or negative tweets? How does the popularity of their brand throughout
                    the time period selected? Based on time the time-based graphs,
                    which events had a positive effect on their brand?

                    ''')

    expander3 = st.expander('Quick personnal analysis feature')

    expander3.write('''
                    Within just a few seconds, you can get a quick personnal analysis
                    of a specific user and get the average sentiment of tweets from
                    and to that user, most commom words used by them etc.
                    ''')



main_css()
custom_css()
main()
