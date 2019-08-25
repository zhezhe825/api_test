'''
测试数据怎样维护，怎样把每种场景都测到 ---> 就用到：数据驱动
比如：新增个人信息接口，用例不光是例子中的四种，还有其他情况，要写全可能要20几条用例
但是要把这些用例写全，那太长了，不利于测试数据的维护

所以，比较各用例间的差异，把 "变化的" 的提取出来，进行维护就好 (body和exp_result是变化的)
这就是：数据驱动的思想
数据驱动：可以自动生成多个测试用例

数据驱动的2种方式：@paramunittest.parametrized()
                   @ddt.ddt()
'''

'''
import unittest
import paramunittest

@paramunittest.parametrized(         # 一定是：元组
    ({"user":"zhezhe","pwd":"111111"},"期望结果1"),    # 四个用例
    ({"user":"zhezhe2","pwd":"111111"},"期望结果1"),
    ({"user":"zhezhe3","pwd":"111111"},"期望结果1"),
    ({"user":"zhezhe4","pwd":"111111"},"期望结果1")
)
class Test_xx(unittest.TestCase):

    def setParameters(self,body,exp_result):     # 固定的方法
        self.body = body               # 初始化
        self.exp_result = exp_result   # 初始化

    def test_x(self):
        body = self.body
        exp = self.exp_result
        act = "期望结果1"
        print(body)
        print(exp)
        self.assertTrue(act == exp)

if __name__ == '__main__':
    unittest.main()
'''



'''
import unittest
import ddt

@ddt.ddt
class Test_xx(unittest.TestCase):

    @ddt.data(            # 一定是：元组
        {"user":"zhezhe","pwd":"111111","exp":"期望结果1"},    #测试数据没有和代码分离
        {"user":"zhezhe2","pwd":"111111","exp":"期望结果1"},
        {"user":"zhezhe3","pwd":"111111","exp":"期望结果1"},
        {"user":"zhezhe4","pwd":"111111","exp":"期望结果1"}
    )
    def test_x(self,test_data):
        print(test_data["user"])
        print(test_data["pwd"])
        print(test_data["exp"])
        act = "期望结果1"
        self.assertTrue(act == test_data["exp"])

if __name__ == '__main__':
    unittest.main()
'''

'''
import unittest
import ddt

# 单独拿出来
# 这个数据还可以单独放在 excel，json，yaml，txt，数据库等；再进行读取

datas = [          # 元组，列表都可以
    {"user":"zhezhe","pwd":"111111","exp":"期望结果1"},    # 把测试数据和代码分离了
    {"user":"zhezhe2","pwd":"111111","exp":"期望结果1"},
    {"user":"zhezhe3","pwd":"111111","exp":"期望结果1"},
    {"user":"zhezhe4","pwd":"111111","exp":"期望结果1"}
]

@ddt.ddt
class Test_xx(unittest.TestCase):

    @ddt.data(*datas)
    def test_x(self,test_data):
        print(test_data["user"])
        print(test_data["pwd"])
        print(test_data["exp"])
        act = "期望结果1"
        self.assertTrue(act == test_data["exp"])

if __name__ == '__main__':
    unittest.main()
'''

