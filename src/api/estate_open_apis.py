import utils.settings as settings
from urllib import request
from urllib.parse import urlencode
import log4p


class EstateOpenAPIs:
    __logger = log4p.GetLogger(__name__, logging_level=settings.DEBUG_LEVEL, config=settings.LOGGING_CONFIG)
    __host = 'http://apis.data.go.kr'

    def __init__(self):
        self.result = 0

    """
    def getCnrdlnService(self, address, page=1, size=10, fmt='json'):
        api_name = '/1611000/nsdi/eios/CnrdlnService.{}?'.format(fmt)
        params = urlencode({'query': address, 'page': page, 'size': size})
        rest_api = self.__host + api_name + params

        full_url = request.Request(rest_api, method='GET')

        self.__logger.logger.debug("Full URL={}".format(full_url.get_full_url()))
        self.__logger.logger.debug("query={}, page={}, size={}".format(address, page, size))

        return request.urlopen(full_url).read().decode('utf-8')
    """

    """
    표준지공시지가정보서비스
    """
    def getReferLandPriceService(self, restApiKey, idcode, stdryear, page=1, row=10, fmt='json'):
        api_name = '/1611000/nsdi/ReferLandPriceService/attr/getReferLandPriceAttr?ServiceKey={}&'.format(restApiKey)
        params = urlencode({'ldCode': idcode, 'stdrYear': stdryear, 'format': fmt, 'numOfRows': row, 'pageNo': page})
        rest_api = self.__host + api_name + params

        full_url = request.Request(rest_api, method='GET')

        self.__logger.logger.debug("Estate API Host : {}, Private Key : {}".format(self.__host, restApiKey))
        self.__logger.logger.debug("Full URL={}".format(full_url.get_full_url()))
        self.__logger.logger.debug("idcode={}, page={}, row={}".format(idcode, page, row))

        return request.urlopen(full_url).read().decode('utf-8')
