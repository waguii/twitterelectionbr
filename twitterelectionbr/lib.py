import snscrape.modules.twitter as sntwitter
import pandas as pd
import numpy as np
from alive_progress import alive_bar
import time
from twitterelectionbr.utils import clear_downloaded_files
from twitterelectionbr.params import DOWNLOAD_FOLDER

def download_tweets(query, limit, sample_size):

    total_tweets = []
    sample_count = 0

    query_result_generator = sntwitter.TwitterSearchScraper(query).get_items()

    while len(total_tweets) < limit:
        sample_tweets = []
        #animated loading bar
        with alive_bar(sample_size, ctrl_c=False, title=f'Downloading tweets[{sample_count}]') as bar:
            for _ in range(0, sample_size):
                tweet = next(query_result_generator)
                sample_tweets.append([  tweet.date,
                                        tweet.user.username,
                                        tweet.content])
                bar()

            total_tweets.extend(sample_tweets)
            sample_count += 1
            #saving DF
            df = pd.DataFrame(sample_tweets, columns=['Date', 'User', 'Tweet'])
            df.to_csv(f'{DOWNLOAD_FOLDER}{sample_count}-partial-{time.time()}.csv')

    df = pd.DataFrame(total_tweets, columns=['Date', 'User', 'Tweet'])
    df.to_csv(f'{DOWNLOAD_FOLDER}total-{time.time()}.csv')

if __name__ == '__main__':
    #Query config - INIT
    #elonmusk until:2022-02-01 since:2022-01-01
    query = "(from:elonmusk) until:2022-05-01 since:2022-04-01"

    limit = 100
    sample_size = 10
    #Query config - END

    clear_downloaded_files()
    download_tweets(query, limit, sample_size)
