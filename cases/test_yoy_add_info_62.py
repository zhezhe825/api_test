import requests
import unittest
from model.yoy_login_3 import yoy_login


class TestAddInfo(unittest.TestCase):
    '''新增用户信息'''
    def setUp(self):
        self.s = requests.session()
        yoy_login(self.s,"zhezhe","111111")
    def tearDown(self):
        self.s.close()

    def test_1(self):
        '''name合法，sex合法 ——> 成功'''
        url = "http://47.104.190.48:8000/user/info"
        body = {
            "name":"zzhe",
            "sex":"女"
        }
        r = self.s.post(url,data=body)
        print(r.text)
        self.assertTrue(r.json()["msg"] == "updata success!")

    def test_2(self):
        '''name为空，sex合法 ——> name参数不能为空'''
        url = "http://47.104.190.48:8000/user/info"
        body = {
            "name":"",
            "sex":"女"
        }
        r = self.s.post(url,data=body)
        print(r.text)
        self.assertTrue(r.json()["msg"] == "name参数不能为空")

    def test_3(self):
        '''name合法，sex为空 ——> sex参数不能为空'''
        url = "http://47.104.190.48:8000/user/info"
        body = {
            "name":"zzhe",
            "sex":""
        }
        r = self.s.post(url,data=body)
        print(r.text)
        self.assertTrue(r.json()["msg"] == "sex参数不能为空")

    def test_4(self):
        '''name已存在 ——> 成功'''
        url = "http://47.104.190.48:8000/user/info"
        body = {
            "name":"zzhe",
            "sex":"女"
        }
        r = self.s.post(url,data=body)
        print(r.text)
        self.assertTrue(r.json()["msg"] == "该昵称已被其他人使用！请换个试试")


if __name__ == '__main__':
    unittest.main()


