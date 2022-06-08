
import re
from twitterelectionbr.interface.api.consts import twiitter_regex_url, twiiter_regex_username
from twitterelectionbr.LeIA.leia import SentimentIntensityAnalyzer
import string
import unidecode
import itertools
from nltk.corpus import stopwords

def get_twiiter_user(input):

    if input is None:
        return None

    if m := re.match(twiiter_regex_username, input):
        return m.group(1)

    if m := re.match(twiitter_regex_url, input):
        return m.group(1)

    return None

def sentiment(data):
    analyzer = SentimentIntensityAnalyzer()
    temp=[]
    for row in data:
        tmp=analyzer.polarity_scores(row)
        temp.append(tmp)
    return temp


def clean_tweet(tweet):
    new_punc = list(string.punctuation)
    del new_punc[2]

    tweet = tweet.lower()
    tweet = re.sub(r"\d+", "", tweet)
    tweet = re.sub(r'\@[a-zA-Z0-9]*', ' ', tweet) # remove username start with @
    tweet = re.sub(r'https?:\/\/[a-zA-Z0-9@:%._\/+~#=?&;-]*', ' ', tweet) # remove link in the tweet
    tweet = re.sub(r'\$[a-zA-Z0-9]*', ' ', tweet) # remove the variable start with $
    for punctuation in new_punc: # remove panctuations
            tweet = tweet.replace(punctuation, '')
    tweet = ' '.join( [w for w in tweet.split() if len(w)>1] ) #remove one letter words
    tweet = ''.join(c[0] for c in itertools.groupby(tweet)) #remove duplicated letters
    tweet = unidecode.unidecode(tweet)  # normalizar as letras com acentos
    tweet = [word for word in tweet.split(' ') if word not in get_stopwords()] # remove stopwords

    return tweet

def get_stopwords():
    stop_words = stopwords.words('portuguese')
    stop_words.remove('não')
    addicional = [
                'd', 'ta', 'q', 'tah', 'tao', 'eh', 'vc', 'voce',
                'pq', 'quede', 'mto', 'mt', 'bj', 'bjs','vcs','bb','pra','ai',
                'b', 'sao', 'axo', 'mano', 'ae', 'neh', 'ai','la','ja','so',
                'porque', 'ne', 'no', 'iai', 'tbm', 'msm', 'jah', 'yahoo', 'yahoobr','rt']
    stop_words.extend(addicional)
    return stop_words
