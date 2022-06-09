import imutils
from twitterelectionbr.cnn.model_1.predict_gender import predict_gender_simple_img
from twitterelectionbr.geolocation.lib import find_location_simple
from twitterelectionbr.webscraper.utils import *
from twitterelectionbr.webscraper.params import *
from twitterelectionbr.interface.api.utils import *
from urllib.error import HTTPError
import pandas as pd

def analyse_img_url(url):
    url = str(url)
    try:
        img = imutils.url_to_image(url)
        return predict_gender_simple_img(img)
    except HTTPError as err:
        #print(err.code)
        pass
    return {}

def get_nlp_vader_df(df_user_tweets):

    df_user_tweets['VADAR'] = sentiment(df_user_tweets['content'])
    df_user_tweets['compound']  = df_user_tweets['VADAR'].apply(lambda score_dict: score_dict['compound'])
    df_user_tweets['sentiment'] = df_user_tweets['compound'].apply(lambda x: 'pos' if x > 0.05 else ('neg' if x < -0.05 else 'neu'))

    #convert to datetime columns
    df_user_tweets['date']=pd.to_datetime(df_user_tweets['date'])

    df_user_tweets['created_at_r']=df_user_tweets['date'].dt.strftime('%Y-%m-%d %H')
    df_user_tweets['created_at_r2']=df_user_tweets['date'].dt.strftime('%m-%d')

    return df_user_tweets[['date', 'created_at_r', 'created_at_r2', 'compound', 'sentiment', 'direction']].to_dict('list')

def data_analysis(df_user_tweets):
    pass

def get_tweets_nlp(df_user_tweets):
    #do nlp using vader
    vader_result = get_nlp_vader_df(df_user_tweets)
    return vader_result

def get_user_tweets_df(username):
    #download tweets
    tweets_to = download_lastest_tweets_to_profile(username)
    tweets_from = download_lastest_tweets_from_profile(username)
    #print quantity of tweets crawled
    #print(f'{len(tweets)} encontrados para {username}')
    #transform to dataframe
    df_to = pd.DataFrame(tweets_to, columns=DF_COLUMNS)
    df_from = pd.DataFrame(tweets_from, columns=DF_COLUMNS)

    df_to['direction'] = 'to'
    df_from['direction'] = 'from'

    return pd.concat([df_to, df_from], ignore_index=True)

def get_tweets_words(df_user_tweets):
    result = df_user_tweets.content.apply(clean_tweet)
    return [word for sentence in result for word in sentence]

def get_location(location):
    result = find_location_simple(location)

    if result is None:
        return None

    return result.raw

def get_tweets_detail(df_user_tweets):
    size = df_user_tweets.shape[0]

    sentiment_counts = df_user_tweets.sentiment.value_counts().to_dict()

    reply_count = int(df_user_tweets.replyCount.sum())
    retweet_count = int(df_user_tweets.retweetCount.sum())
    like_count = int(df_user_tweets.likeCount.sum())

    return {
        'size': size,
        'sentiment_counts' : sentiment_counts,
        'reply_count' : reply_count,
        'retweet_count' : retweet_count,
        'like_count' : like_count
    }

def dataframe_to_json(dataframe):
    return dataframe.to_json()

def analysis_twiitter_user(username):

    profile = profile_info(username)

    if profile is None:
        return {'error' : "Twiiter profile not found"}

    cnn_result = analyse_img_url(profile.profileImageUrl)

    geo_result = get_location(profile.location)

    user_tweets_df = get_user_tweets_df(username)

    user_tweets_df_json = dataframe_to_json(user_tweets_df)

    nlp_result = get_tweets_nlp(user_tweets_df)

    words_result = get_tweets_words(user_tweets_df)

    detail_result = get_tweets_detail(user_tweets_df)

    return {
        'detail' : detail_result,
        'profile' : profile,
        'profile_analysis' : {
            'cnn' : cnn_result,
            'geo': geo_result
        },
        'tweets_analysis' : {
            'nlp' : nlp_result,
            'words': words_result
        },
        'raw': user_tweets_df_json
    }
