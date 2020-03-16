import pymongo
import utils.settings as settings
import log4p


class MongoDBManager:
    __logger = log4p.GetLogger(__name__, logging_level=settings.DEBUG_LEVEL, config=settings.LOGGING_CONFIG)

    def __init__(self):
        self.result = 0

        myclient = pymongo.MongoClient(settings.MONGODB_HOST)
        mydb = myclient[settings.ADDRESS_DATABASE]
        mycol = mydb['강원도']
        x = mycol.find_one()
        print(x)

