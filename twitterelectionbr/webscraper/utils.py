import os
import glob
from twitterelectionbr.webscraper.params import *
import shutil
import pandas as pd
import snscrape.modules.twitter as sntwitter
from datetime import datetime, timedelta
from alive_progress import alive_bar

# def clear_downloaded_files():
    # for f in glob.glob(DOWNLOAD_FOLDER + '*'):
    #     if os.path.isfile(f):
    #         os.remove(f)
    # for f in glob.glob(DOWNLOAD_PARTIAL_FOLDER + '*'):
    #     if os.path.isfile(f):
    #         os.remove(f)

def remove_breaklines(message):
    return message.replace("\n", " ").replace('\r', '')

def save_tweets_by_date(tweets, date, query):

    if len(tweets) == 0:
        return

    query_folder = DOWNLOAD_FOLDER + query

    # Check whether the specified path exists or not
    isExist = os.path.exists(query_folder)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(query_folder)

    df = pd.DataFrame(tweets, columns=DF_COLUMNS)
    df.to_csv(f'{query_folder}/{date}.csv', index=False)

def save_tweets(tweets, query):
    query_folder = DOWNLOAD_FOLDER + query

    # Check whether the specified path exists or not
    isExist = os.path.exists(query_folder)

    if not isExist:
        # Create a new directory because it does not existaa
        os.makedirs(query_folder)

    df = pd.DataFrame(tweets, columns=DF_COLUMNS)
    df.to_csv(f'{query_folder}/total_tweets.csv', index=False)


def download_tweets_by_date(query, date, limit):
    tweets = []
    stop_criteria = True if limit == -1 else len(tweets) < limit

    d_date = datetime.strptime(date, '%Y-%m-%d').date() + timedelta(days=1) #date +1 day
    util_date = d_date.strftime("%Y-%m-%d")

    search_term = query +" lang:pt until:"+ util_date + " since:" + date
    #print(search_term)
    #download tweets
    query_result_generator = sntwitter.TwitterSearchScraper(search_term).get_items()
    #with alive_bar(ctrl_c=False, title=f'Downloading tweets[{query} - {date}]') as bar:
    while stop_criteria:
        try:
            tweets.append(next(query_result_generator))
        except StopIteration:
            break
    # print(len(tweets))
    return tweets

def parse_tweet(content):
    user = [
        content.user.username, content.user.displayname,
        remove_breaklines(content.user.description),
        content.user.verified,
        content.user.created.strftime(FORMAT_DATETIME),
        content.user.followersCount,
        content.user.friendsCount, remove_breaklines(content.user.location),
        content.user.protected, content.user.profileImageUrl
    ]

    tweet = [
        content.url, content.date.strftime(FORMAT_DATETIME),
        remove_breaklines(content.content), content.id,
        content.replyCount, content.retweetCount,
        content.likeCount, content.quoteCount, content.lang
    ]

    return tweet + user

def date_range(start, end):

    dstart = datetime.strptime(start, '%Y-%m-%d').date()
    dend = datetime.strptime(end, '%Y-%m-%d').date()

    delta = dend - dstart  # as timedelta
    days = [(dstart + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(delta.days + 1)]
    return days

# def download_tweets(query, init_date, end_date, limit):

#     date_tweets = []
#     total_tweets = []
#     last_date = end_date
#     stop_criteria = True if limit == -1 else len(total_tweets) < limit

#     search_term = query +" lang:pt until:"+ end_date+ " since:" + init_date

#     query_result_generator = sntwitter.TwitterSearchScraper(search_term).get_items()

#     #with alive_bar(ctrl_c=False, title=f'Downloading tweets[{query} - {last_date}]') as bar:
#     while stop_criteria:
#         try:
#             content = next(query_result_generator)

#             current_date = content.date.strftime(FORMAT_DATE)

#             user = [
#                 content.user.username, content.user.displayname,
#                 remove_breaklines(content.user.description),
#                 content.user.verified,
#                 content.user.created.strftime(FORMAT_DATETIME),
#                 content.user.followersCount,
#                 content.user.friendsCount, content.user.location,
#                 content.user.protected, content.user.profileImageUrl
#             ]

#             tweet = [
#                 content.url, content.date.strftime(FORMAT_DATETIME),
#                 remove_breaklines(content.content), content.id,
#                 content.replyCount, content.retweetCount,
#                 content.likeCount, content.quoteCount, content.lang
#             ]

#             if current_date != last_date:
#                 print(f'partial {current_date}')
#                 save_tweets_by_date(date_tweets, last_date, query)
#                 total_tweets.extend(date_tweets)
#                 date_tweets = []
#                 last_date = current_date
#                 #bar() #print another animated bar
#             else:
#                 date_tweets.append(tweet + user)

#         except StopIteration:
#             save_tweets_by_date(date_tweets, last_date, query)
#             total_tweets.extend(date_tweets)
#             break

#     print(len(total_tweets))
#     save_tweets(total_tweets,query)
