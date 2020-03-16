import pykka
import json
import utils.settings as settings
import log4p


def parallel_run(pool_size, call_limit, lists):
    logger = log4p.GetLogger(__name__, logging_level=settings.DEBUG_LEVEL, config=settings.LOGGING_CONFIG)
    adders = [DBAdder.start().proxy() for _ in range(pool_size)]

    results = []
    for i, content in enumerate(lists):
        if i < call_limit:
            results.append(adders[i % len(adders)].store_to_mongodb(content))
        else:
            pass

    gathered_results = pykka.get_all(results)

    pykka.ActorRegistry.stop_all()

    logger.logger.debug(gathered_results)

    return gathered_results


class DBAdder(pykka.ThreadingActor):
    __logger = log4p.GetLogger(__name__, logging_level=settings.DEBUG_LEVEL, config=settings.LOGGING_CONFIG)

    def __init__(self):
        super().__init__()
        self.result = 0

    def store_to_mongodb(self, content):
        try:
            res = json.dumps(content, ensure_ascii=False)

            # add code to connect to mongodb

            self.__logger.logger.debug(f'Success: {res}')
            return True
        except Exception as e:
            self.__logger.logger.debug(f'Failed resolving {content}')
            return e
