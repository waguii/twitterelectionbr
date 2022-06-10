import streamlit as st
from static.core_css import main_css

# NOTE: This must be the first command in your app, and must be set only once
st.set_page_config(layout="wide")

def main():
    st.markdown("<h1 style='text-align: center;'>Twiitter Sentiment Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Le Wagon Brazil - Batch #869 </h5>", unsafe_allow_html=True)
    st.markdown("""
                <div class="container">
                    <div class="row justify-content-md-center">
                        <div class="col-md-10">
                            Collect tweets using the twitter api (snsscrape) for keywords and hashtags with publish date close(first day of year util last day of election) to the election period and then try to create a dataset containing the tweets content and author details.
                        </div>
                    </div>
                </div>""",unsafe_allow_html=True)

    st.markdown("""
                <div class="container mt-5">
                    <div class="row justify-content-md-center">
                        <div class="col-md-5">
                            <h5 style='text-align: center;'> Proposal </h5>
                            <ul class="list-group">
                                <li class="list-group-item">Do sentiment analysis about the content posted on twitter</li>
                                <li class="list-group-item">Make gender classification based on twiiter profile picture</li>
                                <li class="list-group-item">Check if political events affect the sentiment of people on twitter during the election</li>
                                <li class="list-group-item">Check if there is a correlation between the sentiment exposed in twiiter posts and the results of the elections</li>
                                <li class="list-group-item">Identify the possible factors that arise in twitter and have an impact on the candidate's campaign process</li>
                            </ul>
                        </div>
                        <div class="col-md-5">
                            <h5 style='text-align: center;'> What did we learn? </h5>
                            <ul class="list-group">
                                <li class="list-group-item">The project can be extended to other sectors. Ex.: Music, Fashion and etc...</li>
                                <li class="list-group-item">The project can be applied to other social networks. Eg: Facebook, Instagram, etc.</li>
                                <li class="list-group-item">The Project can be applied in companies and institutions exposed on social networks</li>
                            </ul>
                        </div>
                    </div>
                </div>""",unsafe_allow_html=True)

main_css()
main()
