import unittest
from api.estate_open_apis import EstateOpenAPIs
import json


class TestEstateOpenAPIs(unittest.TestCase):
    def test_get_address(self):
        res_json = json.loads(EstateOpenAPIs().getCnrdlnService())


if __name__ == '__main__':
    unittest.main()
