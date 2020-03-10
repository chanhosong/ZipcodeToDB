import os
import json
import pandas as pd
import utils.settings as settings
import utils.log4py as log4py
from utils.kakao_open_apis import KakaoOpenAPIs


class ApiManager:
    __logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)
    __data_path = 'data/zipcode_DB/'
    __query_column = ['시도', '시군구', '읍면', '건물번호본번', '건물번호부번']
    __kakaoApis = KakaoOpenAPIs()

    def __init__(self):
        self.result = 0

    def getMapAdderess(self, query):
        res_json = json.loads(self.__kakaoApis.getAddress(query))
        # road_address = res_json['documents'][0]['road_address']
        # address_name = road_address['address_name']
        # total_count = res_json['meta']['total_count']
        # x = road_address['x']
        # y = road_address['y']
        # zip_code = road_address['zone_no']

        # self.__logger.debug("road_address={}, zip_code={}, x={}, y={}".format(address_name, zip_code, x, y))

        return res_json

    def makeQuery(self, sido):
        return list(map(lambda x: '{} {} {} {}-{}'.format(x[0], x[1], x[2], x[3], x[4])
                        , self.getZipcode(sido)[self.__query_column].values))

    def getFileName(self):
        return list(filter(lambda x: x.endswith('.txt'), os.listdir(self.__data_path)))

    def getZipcode(self, sido):
        return pd.read_csv(self.__data_path + sido, delimiter='|')

    def totalColumnCount(self):
        cnt = 0
        for i in self.getFileName():
            cnt += len(self.getZipcode(i))

        # 6,319,248 / 300,000 = 21일
        print(cnt)