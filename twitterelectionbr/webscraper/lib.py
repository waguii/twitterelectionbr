from twitterelectionbr.webscraper.utils import *
from twitterelectionbr.webscraper.params import *
import concurrent.futures
import os

#number of threads
THREAD_POOL_SIZE = 30

def get_tweet_task(query, date, limit):
    file_name = os.path.join(query, date + ".csv")
    absulute_path = os.path.join(DOWNLOAD_FOLDER, file_name)

    if os.path.exists(absulute_path):
        return []

    tweets = download_tweets_by_date(query, date, limit)
    return [parse_tweet(tweet) for tweet in tweets]

def get_tweets(query, init_date, end_date, limit):
    dates = date_range(init_date, end_date)

    with concurrent.futures.ThreadPoolExecutor(max_workers = THREAD_POOL_SIZE) as executor:
        future_to_date = {executor.submit(get_tweet_task, query, date, limit): date for date in dates}
        for future in concurrent.futures.as_completed(future_to_date):
            date = future_to_date[future]
            try:
                tweets = future.result()
            except Exception as exc:
                print(f'{query} exception {exc}')
            else:
                if len(tweets) != 0:
                    print(f'{len(tweets)} tweets encontrados para {query} em {date}')
                    #save the tweets
                    save_tweets_by_date(tweets, date, query)

    concatenate_datasets(query)

if __name__ == '__main__':
    #Query config - INIT
    query = "Ciro Gomes"
    limit = -1 #no limit
    init_date = "2018-03-01" #"2014-03-01"
    end_date = "2018-10-28" #"2014-10-27"
    #Query config - END

    #download and save the tweets
    get_tweets(query, init_date, end_date, limit)
