from api import open_api_manager
import utils.settings as settings
import log4p
import actor.caller as caller

if __name__ == '__main__':
    __logger = log4p.GetLogger(__name__, logging_level=settings.DEBUG_LEVEL, config=settings.LOGGING_CONFIG)
    am = open_api_manager.OpenApiManager()
    call = caller

    test_query = "강원도 강릉시 유천동 760-1"

    for sido in am.getFileName():
        call.parallel_run(settings.NUM_WORKER,
                          settings.NUM_CALL_LIMIT,
                          am.makeQuery(sido))
