import requests
import unittest
from model.bky_liucheng_2 import bky_login,bky_save,bky_delete

class TestBky(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        s = bky_login(self.s)
    def tearDown(self):
        self.s.close()

    # 方法一：globals()
    def test_01_save(self):
        postid = bky_save(self.s)
        globals()["id"] = postid  # 全局变量        # 用例之间怎么实现数据共享
        print(postid)
    def test_02_delete(self):
        result = bky_delete(self.s,globals()["id"])
        print(result)

    # # 方法二：中间变量
    # def test_111(self):
    #     p = bky_save(self.s)
    #     result = bky_delete(self.s,p)
    #     print(result)

if __name__ == '__main__':
    unittest.main()