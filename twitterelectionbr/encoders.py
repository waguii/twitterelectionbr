from sklearn.pipeline import make_pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import  make_column_transformer
import nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class CleaningEncoder(BaseEstimator, TransformerMixin):
    '''
    Receives raw text data from the tweets and returns clean data:
    Actions:
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

        #settinbg lower case
        X_ = X_.str.lower()

        #removing handles
        X_ = X_.apply(lambda x: ' '.join( [w for w in x.split() if not w.startswith('@')] ))

        #removing punctuation from each tweet
        for punctuation in string.punctuation:
            X_ = X_.str.replace(punctuation, '')

        #removing numbers
        X_ = X_.str.replace('\d+', '')

        #tokenizing
        X_ = X_.apply(word_tokenize)

        #removing stopwords

        stop_words = stopwords.words('portuguese')
        stop_words.remove('não')
        addicional = [
            'ta', 'q', 'nao', 'tah', 'tao', 'eh', 'vc', 'voce',
            'pq', 'quedê', 'mane', 'mto', 'mt', 'bj', 'bjs',
            'b', 'sao', 'axo', 'mano', 'ae', 'neh' ]
        stop_words.extend(addicional)

        X_ = X_.apply(lambda x: [word for word in x if word not in (stop_words)])



        return X_
