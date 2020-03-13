import pykka
import api_manager
import utils.settings as settings
import utils.log4py as log4py


def parallel_run(pool_size, call_limit, queries):
    logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)
    callers = [Caller.start().proxy() for _ in range(pool_size)]

    json_results = []
    for i, query in enumerate(queries):
        if i < call_limit:
            json_results.append(callers[i % len(callers)].call(query))
        else:
            pass

    gathered_results = pykka.get_all(json_results)

    pykka.ActorRegistry.stop_all()

    logger.debug(gathered_results)

    return gathered_results


class Caller(pykka.ThreadingActor):
    __am = api_manager.ApiManager()
    __logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)

    def call(self, query):
        try:
            json = self.__am.getMapAdderess(query)
            self.__logger.debug(f'Success: {json}')
            return json
        except Exception:
            self.__logger.debug(f'Failed resolving {query}')
            return None
