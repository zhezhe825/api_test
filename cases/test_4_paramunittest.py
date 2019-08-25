import requests
import unittest
import paramunittest
from model.yoy_login_3 import yoy_login

s = requests.session()
yoy_login(s,"zhezhe","111111")

@paramunittest.parametrized(
    ({"name":"zhe123","sex":"女"},"updata success!"),
    ({"name":"","sex":"女"},"name参数不能为空"),
    ({"name":"zhe123","":"女"},"sex参数不能为空"),
    ({"name":"zhe123","sex":"女"},"该昵称已被其他人使用！请换个试试")
)
class TestAddInfo(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        yoy_login(self.s,"zhezhe","111111")
    def tearDown(self):
        self.s.close()
    def setParameters(self,body,exp):
        self.body = body
        self.exp = exp

    def test_1(self):
        url = "http://47.104.190.48:8000/user/info"
        r = self.s.post(url,data=self.body)
        print(r.json())
        act = r.json()["msg"]
        self.assertTrue(act == self.exp)

if __name__ == '__main__':
    unittest.main()