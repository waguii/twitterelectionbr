import sys
import gc
import os
import pandas as pd
import numpy as np
from twitterelectionbr.cnn.model_1.predict_gender import predict_gender_simple_img
import imutils
from urllib.error import HTTPError

def analyse_img_url(url):
    #print('URL ' + url)
    try:
        img = imutils.url_to_image(url)
        return predict_gender_simple_img(img)
    except HTTPError as err:
        print(err.code)
    return {}


def transform_dataset(dataset):

    dataset_unique = dataset.drop_duplicates(subset=['username'])

    dataset_unique['cnn'] = [analyse_img_url(row) for row in dataset_unique['profile_img']]
    dataset_unique['gender']  = dataset_unique['cnn'].apply(lambda score_dict: score_dict.get('gender', np.nan))
    dataset_unique['gender_confidence_score']  = dataset_unique['cnn'].apply(lambda score_dict: score_dict.get('gender_confidence_score', np.nan))

    merged = pd.merge(dataset, dataset_unique, how='inner',
                      left_on=['username'],right_on=['username'],
                      suffixes=('', '_delme'))

    # Discard the columns that acquired a suffix
    merged = merged[[c for c in merged.columns if not c.endswith('_delme')]]

    return merged

def save_dataset(dataset, path, filename):

    #remove extension
    filename = os.path.splitext(filename)[0]

    dataset.to_csv(os.path.join(path, filename + "_cnn.csv"))
    print(f'Dataset({filename}) salvo.')

def transform_datasets(path, output_path):

    files = []

    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(dirname, filename))

    print(f'Arquivos encontrados: {files}')

    for file in files:

        dataset = pd.read_csv(file)

        print(f'Realizando analise de genero em {file}...')

        dataset = transform_dataset(dataset)

        save_dataset(dataset, output_path, filename)

        del [[dataset]]
        gc.collect()

if __name__ == '__main__':
    transform_datasets('raw_data/data/totals/', 'raw_data/data_cnn/cnn_results/')
