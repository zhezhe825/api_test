import requests
import unittest
from model.yoy_login_3 import yoy_login

class TestYoyLogin(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        self.s.close()

    def test_login_1(self):
        '''用户名正确，密码正确——>登录成功'''
        a = yoy_login(self.s,"zhezhe","111111")
        # print(a)
        self.assertTrue(a["msg"] == "login success!")
        self.assertTrue(a["status"] == 0)

    def test_login_2(self):
        '''用户名为空，密码正确——>用户名不能为空'''
        a = yoy_login(self.s,"","111111")
        # print(a)
        self.assertTrue(a["msg"] == "用户名不能为空")
        self.assertTrue(a["status"] == 4)

    def test_login_3(self):
        '''用户名正确，密码密码——>密码不能为空'''
        a = yoy_login(self.s,"zhezhe","")
        # print(a)
        self.assertTrue(a["msg"] == "用密码不能为空")
        self.assertTrue(a["status"] == 4)

#            。。。。其他情况

if __name__ == '__main__':
    unittest.main()