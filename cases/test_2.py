'''
前置(测试用例的)：def setUp(self):

                  1.数据的准备工作(连接mysql，删除，新增数据，修改数据)
                  2.有依赖的接口，比如依赖登录
                  3.公用的死数据，可以放前置

后置(测试用例的)：def tearDown(self):
                  关闭浏览器（之前是一直打开浏览器，从来没有关闭过）

类的前置：@classmethod
          def setUpClass(cls):

类的后置：@classmethod
          def tearDownClass(cls):
'''
'''
unittest框架中：
用例之间是相互独立的，用例的执行顺序也不是：自上向下
用例执行顺序是按（assic码）：0-9 ，A-Z， a-z顺序执行的
'''
'''
一个 .py文件,对应一个接口
一个def对应一个用例
一个用例可以有多个断言
'''

import unittest

class TestOne(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有的测试用例之前，只执行一次！！")
    @classmethod
    def tearDownClass(cls):
        print("所有的测试用例之后，只执行一次！！")

    def setUp(self):
        print("先登录,数据准备---每个用例之前都会执行")
    def tearDown(self):
        print("关闭,数据清理---每个用例之后都会执行")

    def test_2(self):             # 顺序可互调，没影响
        print("测试用例2222222")
    def test_1(self):
        print("测试用例11111111")

if __name__ == '__main__':
    unittest.main()