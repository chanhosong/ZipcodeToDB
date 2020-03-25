import datetime
import time
import os
from pathlib import Path

# DEBUG LEVEL
DEBUG_LEVEL = 'DEBUG'

# Settings for Project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR_ZIPCODE = 'data/zipcode_DB/'
DATA_DIR_ADDRESS = 'data/address/'
LOGGING_CONFIG = os.path.dirname(ROOT_DIR) + '/log4p.json'
LOGGING_DIR = 'logs/'

# Date Time Format
timestr = None
datestr = None
FORMAT_DATE = "%Y%m%d"
FORMAT_DATETIME = "%Y%m%d%H%M%S"

# Number of concurrent call
NUM_WORKER = 2
NUM_CALL_LIMIT = 2

# Settings for MongoDB
MONGODB_HOST = 'mongodb://localhost:27017/'
ADDRESS_DATABASE = 'address'
ADDRESS_ZIPCODE = 'zipcode'
ESTATE_DATABASE = 'estate'


def get_time_str():
    global timestr
    return datetime.datetime.fromtimestamp(int(time.time())).strftime(FORMAT_DATETIME)


def get_date_str():
    global datestr
    return datetime.datetime.fromtimestamp(int(time.time())).strftime(FORMAT_DATE)
