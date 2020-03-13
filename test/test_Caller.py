import api_manager
import actor.caller as caller
import unittest


class Test(unittest.TestCase):
    __am = api_manager.ApiManager()
    __call = caller

    def test_parallel_run(self):
        print(self.__am.getFileName())
        # for sido in self.__am.getFileName():
        #     print(self.__call.parallel_run(settings.NUM_PARALLEL, self.__am.makeQuery(sido)))


if __name__ == '__main__':
    unittest.main()
