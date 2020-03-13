import datetime
import time
import os
from pathlib import Path

# DEBUG LEVEL
DEBUG_LEVEL = 'debug'

# Settings for Project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = 'data/zipcode_DB/'

# Date Time Format
timestr = None
FORMAT_DATE = "%Y%m%d"
FORMAT_DATETIME = "%Y%m%d%H%M%S"

# Number of concurrent call
NUM_PARALLEL = 10

def get_time_str():
    global timestr

    timestr = datetime.datetime.fromtimestamp(int(time.time())).strftime(FORMAT_DATETIME)

    return timestr
