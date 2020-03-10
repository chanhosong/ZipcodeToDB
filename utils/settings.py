import datetime
import time
import os

# DEBUG LEVEL
DEBUG_LEVEL = 'debug'

# Settings for Project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
