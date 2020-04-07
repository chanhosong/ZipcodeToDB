import os
import pandas as pd
import utils.settings as settings


class KeyManager:
    def getKakaoKeys(self):
        return pd.read_csv(os.path.dirname(settings.ROOT_DIR) + '/' + settings.KAKAO_SECRETKEYS, header=None)[0]

    def getGovKeys(self):
        return pd.read_csv(os.path.dirname(settings.ROOT_DIR) + '/' + settings.GOV_OPENAPI_SECRETKEYS, header=None)[0]
