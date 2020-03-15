import utils.settings as settings
import utils.log4py as log4py
from urllib import request
from urllib.parse import urlencode


class EstateOpenAPIs:
    __logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)
    __host = 'http://apis.data.go.kr/'
    __resApiKey = 'b58d37f7456e74b62b2b8f2a03d57d6b'

    def __init__(self):
        self.__logger.debug("Estate API Host : {}, Private Key : {}".format(self.__host, self.__resApiKey))
        self.result = 0

    def getCnrdlnService(self, address, page=1, size=10, fmt='json'):
        api_name = '1611000/nsdi/eios/CnrdlnService.{}?'.format(fmt)
        params = urlencode({'query': address, 'page': page, 'size': size})
        header = {'Authorization': 'KakaoAK ' + self.__resApiKey}
        rest_api = self.__host + api_name + params

        full_url = request.Request(rest_api, headers=header, method='GET')

        self.__logger.debug("Full URL={}".format(full_url.get_full_url()))
        self.__logger.debug("query={}, page={}, size={}".format(address, page, size))

        return request.urlopen(full_url).read().decode('utf-8')
