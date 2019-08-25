'''
用例之间怎么实现数据共享
即：上一个用例的返回结果，是下一个用例的输入。如：postid

答：2种方式
（1）全局变量：用 globals() 把用例之间共享的参数，弄成全局变量； globals() 的数据类型为字典
（2）中间变量：写在一个def中
'''


import unittest

class Test(unittest.TestCase):

    # 方式一：
    def test_1(self):
        postid = "62531"
        globals()["id"] = postid
        self.assertTrue(postid)
    def test_2(self):
        b = globals()["id"]
        print(b)

    # 方式二：写在一个def中
    def test_3(self):
        p = "5134516"
        b = p
        print(b)



if __name__ == '__main__':
    unittest.main()