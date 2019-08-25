'''
unittest框架：单元测试框架，也可做自动化测试，python自带的
unittest：管理测试用例，执行用例，查看结果，生成 html 报告（多少通过，多少失败 ）
自动化：自己的代码，验证别人的代码

大驼峰命名：PrintEmployeePaychecks()
小驼峰：printEmployeePaychecks()
下划线命名：print_employee_paychecks()

类：大驼峰命名
其他：小驼峰，下划线命名

class：测试的集合，一个集合又是一个类
unittest.TestCase：继承
继承的作用：子类继承父类（TestExample 继承 TestCase），父类有的，子类都有
'''
'''
self.assertEqual(0 + 1, 2, msg="失败原因：0+1 不等于 2！")
断言失败可用：msg="。。。" 给出提示信息
 .通过    F 失败:开发的BUG    E:你自己的代码的BUG
'''

import unittest
# print(help(unittest))   # help：查看帮助文档

class TestExample(unittest.TestCase):

    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
        # self.assertEqual(0 + 1, 2, msg="失败原因：0+1 不等于 2！")

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()

