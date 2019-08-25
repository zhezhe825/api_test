import unittest
import requests

class TestWeather(unittest.TestCase):
    '''测试天气接口'''

    def setUp(self):
        self.s = requests.session()
        self.url = "http://47.104.190.48:8000/weather_json/"

    def tearDown(self):
        self.s.close()

    def test_weather_1(self):
        '''time合法,city合法 ——>期望:成功'''
        par = {"time": "2019-04-05",
                "city": "上海"}
        r = self.s.get(self.url,params=par)
        print(r.json())

        self.assertTrue(r.json()["reason"] == "success")
        self.assertTrue(r.json()["error_code"] == 1)
        self.assertTrue(len(r.json()["detail"]) >= 1)

    def test_weather_2(self):
        '''time为空,city合法 ——>期望:time不能为空'''
        par = {"time": "",
                "city": "上海"}
        r = self.s.get(self.url,params=par)
        print(r.json())

        self.assertTrue(r.json()["reason"] == "时间格式不对,标准格式%Y-%m-%d，%Y-%m-%d %H:%M:%S")
        self.assertTrue(r.json()["error_code"] == 0)
        self.assertTrue(len(r.json()["detail"]) >= 1)

    def test_weather_3(self):
        '''time合法,city为空 ——>期望:city不能为空'''
        par = {"time": "2019-04-05",
                "city": ""}
        r = self.s.get(self.url,params=par)
        print(r.json())

        self.assertTrue(r.json()["reason"] == "城市不能为空")
        self.assertTrue(r.json()["error_code"] == 0)
        self.assertTrue(len(r.json()["detail"]) >= 1)


if __name__ == '__main__':
    unittest.main()
