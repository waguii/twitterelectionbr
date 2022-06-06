import sys
import gc
import os
import pandas as pd
import numpy as np
from twitterelectionbr.cnn.model_1.predict_gender import predict_gender_simple_img
import imutils
from urllib.error import HTTPError
import concurrent.futures

#number of threads
THREAD_POOL_SIZE = 15

pd.options.mode.chained_assignment = None  # default='warn'

def analyse_img_url(url):
    #print('URL ' + url)
    try:
        img = imutils.url_to_image(url)
        return predict_gender_simple_img(img)
    except HTTPError as err:
        #print(err.code)
        pass
    return {}

def analyse_imgs_batch(dataset):
    dataset['cnn'] = dataset.apply(lambda row : analyse_img_url(row['profile_img']), axis=1)
    return dataset

def gender_classification(dataset_unique, filename):

    counter = 0
    split_number = int(dataset_unique.shape[0] * 0.1) #10%
    split_number = 1 if split_number < 1 else split_number

    dataset_unique_list = np.array_split(dataset_unique, split_number)
    dataset_unique_result = pd.DataFrame()

    with concurrent.futures.ThreadPoolExecutor(max_workers = THREAD_POOL_SIZE) as executor:
        future_to_dataset = {executor.submit(analyse_imgs_batch, dataset_unique): dataset_unique for dataset_unique in dataset_unique_list}
        for future in concurrent.futures.as_completed(future_to_dataset):
            dataset_unique = future_to_dataset[future]
            try:
                dataset = future.result()
            except Exception as exc:
                print(f'dataset exception {exc}')
            else:
                counter += 1
                print(f'{filename} [{counter}/{len(dataset_unique_list)}]')
                dataset_unique_result = pd.concat([dataset_unique_result, dataset], axis=0)

    return dataset_unique_result


def transform_dataset(file):

    filename = os.path.splitext(os.path.basename(file))[0]
    dataset = pd.read_csv(file)

    middle = int(dataset.shape[0] / 2)

    dfs = np.split(dataset, [middle], axis=0)

    print(f'size: {len(dfs)} ')

    dataset = dfs[0]

    #dataset = dataset.iloc[:, :middle]

    print(f'Realizando analise de genero em {file}...')

    dataset_unique = dataset.drop_duplicates(subset=['username'])

    dataset_unique = gender_classification(dataset_unique, filename)
    dataset_unique['gender']  = dataset_unique['cnn'].apply(lambda score_dict: score_dict.get('gender', np.nan))
    dataset_unique['gender_confidence_score']  = dataset_unique['cnn'].apply(lambda score_dict: score_dict.get('gender_confidence_score', np.nan))

    merged = pd.merge(dataset, dataset_unique, how='inner',
                      left_on=['username'],right_on=['username'],
                      suffixes=('', '_delme'))

    # Discard the columns that acquired a suffix
    merged = merged[[c for c in merged.columns if not c.endswith('_delme')]]

    del [[dataset]]
    # gc.collect()

    return merged

def save_dataset(dataset, path, filename):

    filename = os.path.basename(filename)

    # remove extension
    filename = os.path.splitext(filename)[0]

    dataset.to_csv(os.path.join(path, filename + "_cnn.csv"))
    print(f'Dataset({filename}) salvo.')

def transform_datasets(path, output_path):

    files = []

    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(dirname, filename))

    print(f'Arquivos encontrados: {files}')

    with concurrent.futures.ThreadPoolExecutor(max_workers = 1) as executor:
        future_to_file = {executor.submit(transform_dataset, file): file for file in files}
        for future in concurrent.futures.as_completed(future_to_file):
            file = future_to_file[future]
            try:
                dataset = future.result()
            except Exception as exc:
                print(f'{file} exception {exc}')
            else:
                print(f'{file} analisado')
                #save the tweets
                save_dataset(dataset, output_path, file)


if __name__ == '__main__':
    transform_datasets('raw_data/data/totals/', 'raw_data/data_cnn/cnn_results/')
