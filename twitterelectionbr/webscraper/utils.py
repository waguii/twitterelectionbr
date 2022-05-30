import os
import glob
from twitterelectionbr.params import DOWNLOAD_FOLDER, DOWNLOAD_PARTIAL_FOLDER
import shutil

def clear_downloaded_files():
    # for f in glob.glob(DOWNLOAD_FOLDER + '*'):
    #     if os.path.isfile(f):
    #         os.remove(f)
    for f in glob.glob(DOWNLOAD_PARTIAL_FOLDER + '*'):
        if os.path.isfile(f):
            os.remove(f)
