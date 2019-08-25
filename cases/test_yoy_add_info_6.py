from model.yoy_login_3 import yoy_login
from model.yoy_add_info_4 import yoy_add_info
import requests
import unittest

class TestAddInfo(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        yoy_login(self.s,"zhezhe","111111")

    def tearDown(self):
        self.s.close()

    def test_add_info_1(self):
        '''name正确，sex正确 ——> 成功'''
        b = yoy_add_info(self.s,"zzhe","女")
        print(b)
        self.assertTrue(b["msg"] == "updata success!")

    def test_add_info_2(self):
        '''name为空，sex正确 ——> name参数不能为空'''
        c = yoy_add_info(self.s,"","女")
        print(c)
        self.assertTrue(c["msg"] == "name参数不能为空")

    def test_add_info_3(self):
        '''name正确，sex为空 ——> sex参数不能为空'''
        c = yoy_add_info(self.s,"zzhe","")
        print(c)
        self.assertTrue(c["msg"] == "sex参数不能为空")

    def test_add_info_4(self):
        '''添加一个已存在的name'''
        b = yoy_add_info(self.s,"zzhe","女")
        print(b)
        self.assertTrue(b["msg"] == "该昵称已被其他人使用！请换个试试")

if __name__ == '__main__':
    unittest.main()
