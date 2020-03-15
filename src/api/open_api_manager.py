import os
import json
import xmltodict
import pandas as pd
import utils.settings as settings
import utils.log4py as log4py
from api.kakao_open_apis import KakaoOpenAPIs
from api.estate_open_apis import EstateOpenAPIs


class OpenApiManager:
    __logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)
    __data_path = os.path.dirname(settings.ROOT_DIR) + '/' + settings.DATA_DIR_ZIPCODE
    __query_column = ['시도', '시군구', '읍면', '건물번호본번', '건물번호부번']
    __kakao_Apis = KakaoOpenAPIs()
    __estate_Apis = EstateOpenAPIs()

    def __init__(self):
        self.result = 0

    def getMapAdderess(self, query):
        return json.loads(self.__kakao_Apis.getAddress(query))

    def makeQuery(self, sido):
        return list(map(lambda x: '{} {} {} {}-{}'.format(x[0], x[1], x[2], x[3], x[4])
                        , self.getZipcode(sido)[self.__query_column].values))

    def getFileName(self):
        return list(filter(lambda x: x.endswith('.txt'), os.listdir(self.__data_path)))

    def getZipcode(self, sido):
        return pd.read_csv(self.__data_path + sido, delimiter='|')

    def xmlToJson(self, xml):
        return json.dumps(xmltodict.parse(xml), indent=4)

    def totalColumnCount(self):
        cnt = 0
        for i in self.getFileName():
            cnt += len(self.getZipcode(i))

        # 6,319,248 / 300,000 = 21일
        print(cnt)
