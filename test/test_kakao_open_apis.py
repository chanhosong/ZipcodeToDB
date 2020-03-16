import unittest
import utils.settings as settings
from api.kakao_open_apis import KakaoOpenAPIs
import json


class TestKakaoOpenAPIs(unittest.TestCase):
    settings.init_logs_dir()

    def test_get_address(self):
        test_query = "강원도 강릉시 유천동 760-1"

        res_json = json.loads(KakaoOpenAPIs().getAddress(test_query))

        print(res_json)

        road_address = res_json['documents'][0]['road_address']

        self.assertEqual(res_json['meta']['total_count'], 1)
        self.assertEqual(road_address['x'], '128.871000945246')
        self.assertEqual(road_address['y'], '37.7620970890927')
        self.assertEqual(road_address['zone_no'], '25458')


if __name__ == '__main__':
    unittest.main()
