import os
from twitterelectionbr.webscraper.params import *
import pandas as pd
import snscrape.modules.twitter as sntwitter
from datetime import datetime, timedelta
import glob
from google.cloud import storage
from datetime import date

# def clear_downloaded_files():
    # for f in glob.glob(DOWNLOAD_FOLDER + '*'):
    #     if os.path.isfile(f):
    #         os.remove(f)
    # for f in glob.glob(DOWNLOAD_PARTIAL_FOLDER + '*'):
    #     if os.path.isfile(f):
    #         os.remove(f)

def remove_breaklines(message):
    return message.replace("\n", " ").replace('\r', '')

def save_tweets_by_date(tweets, date, query, candidate, remote=False):

    if len(tweets) == 0:
        return

    dyear = datetime.strptime(date, '%Y-%m-%d').date().year

    df = pd.DataFrame(tweets, columns=DF_COLUMNS)

    now = datetime.now() # current date and time
    df['query'] = query
    df['crawled_date'] = now.strftime("%Y-%m-%d")

    if remote:
        file_path = "/".join(("data", str(dyear), candidate.name, query, date + ".csv"))

        if not file_exists_gcp(BUCKET_NAME, file_path):
            upload_to_gcp(df, BUCKET_NAME, file_path)

    else:
        query_folder = os.path.join(DOWNLOAD_FOLDER,str(dyear),candidate.name,query)
        # Check whether the specified path exists or not
        isExist = os.path.exists(query_folder)

        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(query_folder)

        df.to_csv(f'{query_folder}/{date}.csv', index=False)


def concatenate_date_datasets(date, query, candidate, remote=False, overwrite=False):

    dyear = datetime.strptime(date, '%Y-%m-%d').date().year

    if remote:
        folder_path = "/".join(("data", str(dyear), candidate.name, query))
        file_path = "/".join((folder_path,  "total_csv.csv"))

        if not file_exists_gcp(BUCKET_NAME, file_path):
            compose_csv_files_gcp(BUCKET_NAME, folder_path, file_path)
    else:
        query_folder = os.path.join(DOWNLOAD_FOLDER,str(dyear),candidate.name,query)
        files = os.path.join(query_folder, "*.csv")
        file_destination = os.path.join(query_folder, "total_tweets.csv")

        if overwrite:
            #remove the old totalfile
            ## If file exists, delete it ##
            if os.path.isfile(file_destination):
                os.remove(file_destination)
        # list of merged files returned
        files = glob.glob(files)
        # joining files with concat and read_csv
        df = pd.concat(map(pd.read_csv, files), ignore_index=True)
        df.to_csv(file_destination, index=False)

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

def download_lastest_tweets_by_profile(profile, limit = 100):
    tweets = []
    #stop_criteria = True if limit == -1 else len(tweets) < limit

    today = date.today().strftime("%Y-%m-%d")
    d_date = (date.today() - timedelta(days=14)).strftime("%Y-%m-%d") #date +14 days

    search_term = profile +" until:"+ today + " since:" + d_date
    #print(search_term)
    #download tweets
    query_result_generator = sntwitter.TwitterSearchScraper(search_term).get_items()
    #with alive_bar(ctrl_c=False, title=f'Downloading tweets[{query} - {date}]') as bar:
    while len(tweets) < limit:
        try:
            tweets.append(next(query_result_generator))
        except StopIteration:
            break
    # print(len(tweets))
    return tweets

def profile_info(username):

    userScraper = sntwitter.TwitterUserScraper(username)

    return userScraper._get_entity()

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


def upload_to_gcp(df, dest_bucket_name, dest_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(dest_bucket_name)
    blob = bucket.blob(dest_file_name)
    blob.upload_from_string(df.to_csv(), 'text/csv')
    print(f'DataFrame uploaded to bucket {dest_bucket_name}, file name: {dest_file_name}')

def file_exists_gcp(bucket_name, file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    return storage.Blob(bucket=bucket, name=file_name).exists(storage_client)

def compose_csv_files_gcp(bucket_name, path, file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    sources = list(bucket.list_blobs(prefix=path))

    destination = bucket.blob(file_name)
    destination.content_type = "text/csv"
    destination.compose(sources)

    print(f'DataFrames concatenated of folder: {path}')
