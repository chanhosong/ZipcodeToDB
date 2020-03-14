from api import open_api_manager
import utils.settings as settings
import utils.log4py as log4py
import actor.caller as caller

if __name__ == '__main__':
    logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)
    am = open_api_manager.OpenApiManager()
    call = caller

    test_query = "강원도 강릉시 유천동 760-1"

    for sido in am.getFileName():
        call.parallel_run(settings.NUM_WORKER,
                          settings.NUM_CALL_LIMIT,
                          am.makeQuery(sido))
