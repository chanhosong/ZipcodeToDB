import pykka
import api_manager
import utils.settings as settings
import utils.log4py as log4py


def parallel_run(pool_size, queries):
    callers = [Caller.start().proxy() for _ in range(pool_size)]

    json_results = []
    for i, query in enumerate(queries):
        if i < 10:
            json_results.append(callers[i % len(callers)].call(query))
        else:
            pass

    gathered_results = pykka.get_all(json_results)
    print(gathered_results)
    # pprint.pprint(list(gathered_results))

    pykka.ActorRegistry.stop_all()

    return gathered_results


class Caller(pykka.ThreadingActor):
    __am = api_manager.ApiManager()
    __logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)

    def call(self, query):
        try:
            json = self.__am.getMapAdderess(query)
            print(f'Success: {json}')
            return json
        except Exception:
            print(f'Failed resolving {query}')
            return None
