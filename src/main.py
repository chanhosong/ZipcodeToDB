import api_manager
import utils.settings as settings
import utils.log4py as log4py
import actor.caller as caller

if __name__ == '__main__':
    logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)
    am = api_manager.ApiManager()
    call = caller

    test_query = "강원도 강릉시 유천동 760-1"

    for sido in am.getFileName():
        call.parallel_run(settings.NUM_PARALLEL, am.makeQuery(sido))


    # for sido in am.getFileName():
    #     for query in am.makeQuery(sido):
    #         print(am.getMapAdderess(query))
    #         cl.run(am.getMapAdderess(query))
    #         time.sleep(10)
