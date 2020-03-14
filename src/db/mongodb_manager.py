import pymongo
import utils.settings as settings


class MongoDBManager:
    def __init__(self):
        self.result = 0

        myclient = pymongo.MongoClient(settings.MONGODB_HOST)
        mydb = myclient[settings.ADDRESS_DATABASE]
        mycol = mydb['강원도']
        x = mycol.find_one()
        print(x)

