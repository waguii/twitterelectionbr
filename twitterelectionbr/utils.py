import os
import glob
from twitterelectionbr.params import DOWNLOAD_FOLDER

def clear_downloaded_files():
    for f in glob.glob(DOWNLOAD_FOLDER + '*'):
        os.remove(f)
