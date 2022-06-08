from geopy.geocoders import Nominatim
from pathlib import Path
import pandas as pd
import os
import glob
import numpy as np

#Consts
LOCATIONS_DIC_FILE = '/content/drive/MyDrive/twiitter_elections_data/utils/locations.npy'

def get_files(directory, extension = 'csv'):
    return [i for i in glob.glob(directory + '*.{}'.format(extension))]

def find_location_simple(location):
    geolocator = Nominatim(user_agent = "my project app")
    try:
        return geolocator.geocode(location)
    except:
        return None


def find_location(location, geolocator, locations_dic):

    location = location.lower()

    if location in locations_dic:
        return locations_dic.get(location)[0], locations_dic.get(location)[1]

    try:
        local  = geolocator.geocode(location).point
        latitude = local[0]
        longitude = local[1]
    except:
        latitude = locations_dic.get('brasil')[0]
        longitude = locations_dic.get('brasil')[1]

    locations_dic[location] = [latitude, longitude]

    np.save(LOCATIONS_DIC_FILE, locations_dic)
    print(f'Location {location} [{latitude},{longitude}]')
    return latitude, longitude

def parse_dataset(dados, locations_dic):
    geolocator = Nominatim(user_agent = "my project app")
    results = dados.location.apply(lambda x: find_location(x, geolocator, locations_dic))
    return pd.DataFrame(results.to_list())

def transform_csv(file, output_path):
  #extract filename
  filename = os.path.splitext(os.path.basename(file))[0]
  #read file
  data = pd.read_csv(file)
  #load locations dict
  path = Path(LOCATIONS_DIC_FILE)
  #initialize locations_dic
  locations_dic = {'brasil' : [ -10.3333333, -53.2 ]}

  if path.is_file():
    locations_dic = np.load(LOCATIONS_DIC_FILE,allow_pickle='TRUE').item()
    #to lowercase
    locations_dic = {k.lower():v for k,v in locations_dic.items()}

  #remove nan
  data.location.fillna('Brasil', inplace=True)
  #parse dataset
  data_loc = parse_dataset(data, locations_dic)
  #rename new columns :x
  data_loc.rename(columns={0: "lat", 1: "long"}, inplace = True)
  #join new columns to original dataset
  data = data.join(data_loc)
  #save the new dataset
  data.to_csv(output_path + filename + '.csv')

if __name__ == '__main__':
    for file in get_files('/content/drive/MyDrive/twiitter_elections_data/pure/'):
        transform_csv(file,'/content/drive/MyDrive/twiitter_elections_data/geolocation/')
