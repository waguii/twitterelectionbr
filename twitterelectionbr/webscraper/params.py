import os
from twitterelectionbr.webscraper.candidate import Candidate

#Consts
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(ROOT_DIR, "..", "..", "raw_data", "data")
BUCKET_NAME = "twiiter-effect-in-elections-bucket"

USER_COLUMNS = [
    "username", "displayname", "description", "verified", "created",
    "followers_count", "friends_count", "location", "protected", "profile_img"
]

TWEET_COLUMNS = [
    "url", "date", "content", "id", "reply_count", "retweet_count",
    "like_count", "quote_count", "lang"
]

DF_COLUMNS = TWEET_COLUMNS + USER_COLUMNS

FORMAT_DATETIME = "%Y-%m-%d %H:%M:%S"
FORMAT_DATE = "%Y-%m-%d"

CANDIDATES = {
    Candidate.CIRO_GOMES : ['Ciro Gomes', 'ciro'],
    Candidate.DILMA_ROUSSEFF : ['Dilma Rousseff', 'dilma'],
    Candidate.AECIO_NEVES : ['Aécio Neves', 'aécio'],
    Candidate.LUCIANA_GENRO : ['Luciana Genro'],
    Candidate.JAIR_BOLSONARO : ['Jair Bolsonaro', 'jair', 'bolsonaro', 'mito' 'biroliro'],
    Candidate.FERNANDO_HADDAD : ['Fernando Haddad', 'haddad'],
    Candidate.MARINA_SILVA : ['Marina Silva'],
    Candidate.GERALDO_ALCKMIN : ['Geraldo Alckmin', 'alckmin'],
    Candidate.JOAO_AMOEDO : ['João Amoedo', 'amoedo'],
    Candidate.CABO_DACIOLO : ['Cabo Daciolo', 'daciolo'],
    Candidate.HENRIQUE_MEIRELES : ['Henrique Meirelles'],
}
