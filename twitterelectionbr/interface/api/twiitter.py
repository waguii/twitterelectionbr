from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from twitterelectionbr.interface.api.utils import get_twiiter_user
from twitterelectionbr.interface.api.service.twiitter_service import analysis_twiitter_user
import nltk
from pathlib import Path
import os
import numpy as np

ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DL_FOLDER = os.path.join(ROOT_FOLDER, "..","..", "data")
LOCATIONS_DIC_FILE = os.path.join(DL_FOLDER, "locations.npy")

#download stop words
nltk.download('stopwords')

print(LOCATIONS_DIC_FILE)

#load locations dict
path = Path(LOCATIONS_DIC_FILE)

locations_dic = {'brasil' : [ -10.3333333, -53.2 ]}

if path.is_file():
    locations_dic = np.load(LOCATIONS_DIC_FILE,allow_pickle='TRUE').item()
    #to lowercase
    locations_dic = {k.lower():v for k,v in locations_dic.items()}

#images url cache
images_cache = {}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/analysis")
def data(twiitter_profile):

    twiitter_username = get_twiiter_user(twiitter_profile)

    if twiitter_username is None:
        return {'error' : "Twiiter profile invalid"}

    return analysis_twiitter_user(twiitter_username, locations_dic, LOCATIONS_DIC_FILE, images_cache)
    #result = analyse_img_url('https://pbs.twimg.com/profile_images/1414439092373254147/JdS8yLGI_400x400.jpg')
