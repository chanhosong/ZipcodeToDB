import pykka
from api import open_api_manager
import utils.settings as settings
import log4p


def parallel_run(pool_size, call_limit, queries):
    __logger = log4p.GetLogger(__name__, logging_level=settings.DEBUG_LEVEL, config=settings.LOGGING_CONFIG)
    callers = [Caller.start().proxy() for _ in range(pool_size)]

    json_results = []
    for i, query in enumerate(queries):
        if i < call_limit:
            json_results.append(callers[i % len(callers)].map_address_call(query))
        else:
            pass

    gathered_results = pykka.get_all(json_results)

    pykka.ActorRegistry.stop_all()

    __logger.logger.debug(gathered_results)

    return gathered_results


class Caller(pykka.ThreadingActor):
    __am = open_api_manager.OpenApiManager()
    __logger = log4p.GetLogger(__name__, logging_level=settings.DEBUG_LEVEL, config=settings.LOGGING_CONFIG)

    def map_address_call(self, query):
        try:
            json = self.__am.getMapAdderess(query)
            self.__logger.logger.debug(f'Success: {json}')
            return json
        except Exception as e:
            self.__logger.logger.debug(f'Failed resolving {query}')
            return e
