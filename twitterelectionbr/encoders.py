from sklearn.pipeline import make_pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import  make_column_transformer
import nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import re

class CleaningEncoder(BaseEstimator, TransformerMixin):
    '''
    Receives raw text data from the tweets and returns clean, ready to process data:
    turns all into lower case;
    removes punctuation;
    removes stopwords;
    removes numbers;
    removes users' handles

    '''
    def __init__(self):
        pass


    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        #assert isinstance(X, pd.DataFrame)
        X_ = X.copy()

        #removin NaN values
        X_ = X_.fillna('nenhuma descrição')

        #removing links
        X_ = X_.apply(lambda x: re.sub(r"http\S+", "", x))
        X_ = X_.apply(lambda x: re.sub(r"www.\S+", "", x))

        #removing punctuation from each tweet
        new_punc = list(string.punctuation)
        del new_punc[2]
        del new_punc[-11]
        for punctuation in new_punc:
            X_ = X_.str.replace(punctuation, '')

        #removing numbers
        X_ = X_.str.replace('\d+', '')

        #tokenizing - removes handles, applies lowercase, keeps #, shortens letter repetitions to three
        #ex: kkkkk, kkkkkk, kkkkkkkkk = kkk
        tkn = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
        X_ = X_.apply(lambda x: tkn.tokenize(x))

        #removing stopwords
        stop_words = stopwords.words('portuguese')
        stop_words.remove('não')
        addicional = [
            'ta', 'q', 'nao', 'tah', 'tao', 'eh', 'vc', 'voce',
            'pq', 'quedê', 'mane', 'mto', 'mt', 'bj', 'bjs',
            'b', 'sao', 'axo', 'mano', 'ae', 'neh', 'aí',
            'kkk', 'porque', 'né', 'no']
        stop_words.extend(addicional)

        X_ = X_.apply(lambda x: [word for word in x if word not in (stop_words)])

        return X_

class TimeEncoder(BaseEstimator, TransformerMixin):
    '''
    Transforms the date column from string to datetime object
    '''

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_ = X_.apply(lambda x: pd.to_datetime(x))
        X_ = pd.DataFrame(X_)
        X_['data'] = X_['date'].dt.date
        X_['hora'] = X_['date'].dt.time
        X_.drop(columns = 'date', inplace=True)
        return X
