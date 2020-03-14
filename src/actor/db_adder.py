import pykka
import os
import json
import utils.settings as settings
import utils.log4py as log4py


def parallel_run(pool_size, call_limit, lists):
    logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)
    adders = [DBAdder.start().proxy() for _ in range(pool_size)]

    results = []
    for i, content in enumerate(lists):
        if i < call_limit:
            results.append(adders[i % len(adders)].store_to_mongodb(content))
        else:
            pass

    gathered_results = pykka.get_all(results)

    pykka.ActorRegistry.stop_all()

    logger.debug(gathered_results)

    return gathered_results


class DBAdder(pykka.ThreadingActor):
    __logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)

    def __init__(self):
        super().__init__()
        self.result = 0

    def store_to_mongodb(self, content):
        try:
            res = json.dumps(content, ensure_ascii=False)

            self.__logger.debug(f'Success: {res}')
            return True
        except Exception as e:
            self.__logger.debug(f'Failed resolving {content}')
            return e
