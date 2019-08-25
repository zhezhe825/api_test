'''
批量执行用例时：
unittest.TextTestRunner返回的是：text文本报告 ---> 不够直观,了解就行
为了方便观察，要生成一个html的测试报告。
因为，unittest本身是没有生成html测试报告的方法的。
所以，需要下载一个第三方的包：HTMLTestRunner_cn.py。
'''


import unittest
import os
from common.HTMLTestRunner_cn import HTMLTestRunner


fu = os.path.dirname(os.path.realpath(__file__))
start_dir = os.path.join(fu,"cases")
print(start_dir)

# 1.查用例
discover = unittest.defaultTestLoader.discover(start_dir,
                                               pattern="test*.py")
print(discover)

# 2.执行用例
# runner = unittest.TextTestRunner()
# runner.run(discover)

report_path = os.path.join(fu,"report","result.html")

with open(report_path,"wb") as fp:     #  r:读  w:写  b:二进制
    runner = HTMLTestRunner(stream=fp,
                            title="xxxx项目yyy模块的接口自动化测试报告",
                            description="http://xxxxx.cn,由zhezhe来写的！！")
    runner.run(discover)