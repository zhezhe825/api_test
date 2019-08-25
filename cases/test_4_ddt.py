import requests
import unittest
import ddt
from model.yoy_login_3 import yoy_login
import json

@ddt.ddt
class TestAddInfo(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        yoy_login(self.s,"zhezhe","111111")
    def tearDown(self):
        self.s.close()

    @ddt.data(
        {'body':'{"name":"zhe123","sex":"女"}','exp':"updata success!"},
        {'body':'{"name":"","sex":"女"}','exp':"name参数不能为空"},
        {'body':'{"name":"zhe123","":"女"}','exp':"sex参数不能为空"},
        {'body':'{"name":"zhe123","sex":"女"}','exp':"该昵称已被其他人使用！请换个试试"},
    )
    def test_1(self,test_data):
        url = "http://47.104.190.48:8000/user/info"
        r = self.s.post(url,data=json.loads(test_data["body"]))
        print(r.json())
        act = r.json()["msg"]
        self.assertTrue(act == test_data["exp"])

if __name__ == '__main__':
    unittest.main()

