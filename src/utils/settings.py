import datetime
import time
import os
from pathlib import Path

# DEBUG LEVEL
DEBUG_LEVEL = 'debug'

# Settings for Project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR_ZIPCODE = 'data/zipcode_DB/'
DATA_DIR_ADDRESS = 'data/address/'

# Date Time Format
timestr = None
FORMAT_DATE = "%Y%m%d"
FORMAT_DATETIME = "%Y%m%d%H%M%S"

# Number of concurrent call
NUM_WORKER = 2
NUM_CALL_LIMIT = 2


def get_time_str():
    global timestr

    timestr = datetime.datetime.fromtimestamp(int(time.time())).strftime(FORMAT_DATETIME)

    return timestr
