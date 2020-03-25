import pymongo
import utils.settings as settings


class MongoDBManager:
    __client = None

    def __init__(self):
        self.result = 0

        self.__client = pymongo.MongoClient(settings.MONGODB_HOST)
        # client = self.__client.init_db()
        # db = client[settings.ADDRESS_DATABASE]
        # collection = db[settings.ADDRESS_ZIPCODE]
        # print(db)

    def init_db(self):
        return self.__client

