from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from twitterelectionbr.interface.api.utils import get_twiiter_user
from twitterelectionbr.interface.api.service.twiitter_service import analysis_twiitter_user
import nltk

#download stop words
nltk.download('stopwords')

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

    return analysis_twiitter_user(twiitter_username)
    #result = analyse_img_url('https://pbs.twimg.com/profile_images/1414439092373254147/JdS8yLGI_400x400.jpg')
