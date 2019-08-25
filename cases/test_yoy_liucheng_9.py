import requests
import unittest
from model.yoy_liucheng_6 import yoy_login,yoy_add_info,yoy_get_info

class TestYoy(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        yoy_login(self.s,"zhezhe","111111")
    def tearDown(self):
        self.s.close()

    def test_add_info(self):
        yoy_add_info(self.s,"zzhe","女")
    def test_get_info(self):
        yoy_get_info(self.s)

if __name__ == '__main__':
    unittest.main()