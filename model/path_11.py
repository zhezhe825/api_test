import os

# 1.文件路径
print(__file__)   # 相对路径(当前文件的)

a1 = os.path.realpath(__file__)   # 真实路径(当前文件的)
print(a1)

a2 = os.path.dirname(os.path.realpath(__file__))
print(a2)      # （真实路径的）文件的“上一层目录”（文件夹）


# 2.文件的属性：__name__
print(__name__)
from model import yoy_login_3
print(yoy_login_3.__name__)

