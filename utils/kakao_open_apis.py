import utils.settings as settings
import utils.log4py as log4py
from urllib import request
from urllib.parse import urlencode


class KakaoOpenAPIs:
    __logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)
    __host = 'https://dapi.kakao.com/v2/local/'
    __resApiKey = 'b58d37f7456e74b62b2b8f2a03d57d6b'

    def __init__(self):
        self.__logger.debug("API Host : {}, Private Key : {}".format(self.__host, self.__resApiKey))
        self.result = 0

    def getAddress(self, address, page=1, size=10, fmt='json'):
        api_name = 'search/address.{}?'.format(fmt)
        params = urlencode({'query': address, 'page': page, 'size': size})
        header = {'Authorization': 'KakaoAK ' + self.__resApiKey}
        rest_api = self.__host + api_name + params

        full_url = request.Request(rest_api, headers=header, method='GET')

        self.__logger.debug("Full URL={}".format(full_url.get_full_url()))
        self.__logger.debug("query={}, page={}, size={}".format(address, page, size))

        return request.urlopen(full_url).read().decode('utf-8')
