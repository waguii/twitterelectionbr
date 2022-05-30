import snscrape.modules.twitter as sntwitter
import pandas as pd
import numpy as np
from alive_progress import alive_bar
import time
from twitterelectionbr.utils import clear_downloaded_files
from twitterelectionbr.params import *

def download_tweets(query, init_date, end_date, limit, sample_size):

    total_tweets = []
    sample_count = 0

    search_term = query +" until:"+ end_date+ " since:" + init_date

    query_result_generator = sntwitter.TwitterSearchScraper(search_term).get_items()

    while len(total_tweets) < limit:
        sample_tweets = []
        #animated loading bar
        with alive_bar(sample_size, ctrl_c=False, title=f'Downloading tweets[{sample_count}]') as bar:
            for _ in range(0, sample_size):
                content = next(query_result_generator)

                user = [
                    content.user.username, content.user.displayname,
                    content.user.description, content.user.verified,
                    content.user.created, content.user.followersCount,
                    content.user.friendsCount, content.user.location,
                    content.user.protected, content.user.profileImageUrl
                ]

                tweet = [
                    content.url, content.date, content.content, content.id,
                    content.replyCount, content.retweetCount,
                    content.likeCount, content.quoteCount, content.lang
                ]

                sample_tweets.append(tweet + user)
                bar()
                #print(tweet.__dict__)

            total_tweets.extend(sample_tweets)
            sample_count += 1
            #saving DF
            df = pd.DataFrame(sample_tweets, columns=DF_COLUMNS)
            df.to_csv(f'{DOWNLOAD_PARTIAL_FOLDER}{query}-{sample_count}-partial-{time.time()}.csv', index=False)

    df = pd.DataFrame(total_tweets, columns=DF_COLUMNS)
    # df.to_csv(f'{DOWNLOAD_FOLDER}{query}-{time.time()}.csv', index=False)
    df.to_csv(f'{DOWNLOAD_FOLDER}{query}-{init_date}-{end_date}.csv', index=False)

if __name__ == '__main__':
    #Query config - INIT
    #elonmusk until:2022-02-01 since:2022-01-01
    query = "haddad"

    limit = 1000000
    sample_size = 100
    init_date = "2018-01-01" #"2014-01-01"
    end_date = "2018-10-28" #"2014-10-27"
    #Query config - END

    clear_downloaded_files()
    download_tweets(query, init_date, end_date, limit, sample_size)
