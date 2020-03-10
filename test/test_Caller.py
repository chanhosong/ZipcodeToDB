import pykka
import actor.Caller as Caller
import unittest


class Test(unittest.TestCase):
    def test_parallel_run(self):
        # callers = [Caller.start().proxy() for _ in range(pool_size)]
        #
        # json_results = []
        # for i, query in enumerate(queries):
        #     if i < 10:
        #         json_results.append(callers[i % len(callers)].__call(query))
        #     else:
        #         pass
        #
        # gathered_results = pykka.get_all(json_results)
        # print(gathered_results)
        # # pprint.pprint(list(gathered_results))
        #
        # pykka.ActorRegistry.stop_all()
        #
        # gathered_results

if __name__ == '__main__':
    unittest.main()
