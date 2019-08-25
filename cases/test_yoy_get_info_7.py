import requests
from model.yoy_login_3 import yoy_login
import unittest

class TestGetInfo(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        yoy_login(self.s,"zhezhe","111111")

    def tearDown(self):
        self.s.close()

    def test_1(self):
        url = "http://47.104.190.48:8000/user/get/info"
        r = self.s.get(url)
        print(r.text)
        self.assertTrue(r.json()["username"] == "zhezhe")
        self.assertTrue(r.json()["name"] == "zzhe")

if __name__ == '__main__':
    unittest.main()

