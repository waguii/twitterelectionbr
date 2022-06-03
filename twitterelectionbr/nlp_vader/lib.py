#imports
import gc
import os
import pandas as pd
from twitterelectionbr.LeIA.leia import SentimentIntensityAnalyzer

def sentiment(analyzer, data):
    temp=[]
    for row in data:
        tmp=analyzer.polarity_scores(row)
        temp.append(tmp)
    return temp

def nlp_vader(path, column):
    files = []
    datasets = []

    analyzer = SentimentIntensityAnalyzer()

    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(dirname, filename))

    print(files)

    for file in files:

        dataset  = pd.read_csv(file)
        print(f'Dataset {file} carregado...')

        query = dataset['query'][0]
        filename = query + "_vader.csv"

        print(f'Realizando analise de sentimento em {query}...')

        dataset['VADAR'] = sentiment(analyzer, dataset[column])
        dataset['compound']  = dataset['VADAR'].apply(lambda score_dict: score_dict['compound'])
        dataset['sentiment']  = dataset['compound'].apply(lambda x: 'pos' if x > 0.05 else ('neg' if x < -0.05 else 'neu'))

        print(f'Dataset {query} analisado.')
        print(dataset['sentiment'].value_counts())

        dataset.to_csv(os.path.join(path, filename))

        print(f'Dataset {query} salvo.')

        del [[dataset]]
        gc.collect()


if __name__ == '__main__':
    nlp_vader('raw_data/data_remote/', 'content')
