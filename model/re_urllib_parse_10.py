import re
from urllib import parse

# 1.正则
a = "https://i.cnblogs.com/PostDone.aspx?postid=11200105&actiontip=%e5%ad%98%e4%b8%ba%e8%8d%89%e7%a8%bf%e6%88%90%e5%8a%9f"
postid = re.findall("postid=(.+?)&action",a)[0]
print(postid)

# 2.把 urlencoded 转成中文
b = parse.unquote(a)  # 转成中文
print(b)

# 3.参数关联
'''
1.参数关联：上一个接口返回的参数，是下一个接口的请求参数
如：token = r.json()["token"]
    hh = {"token": token}      hh：头部
    就是：参数关联
    是一种动态变量
    token = "Whduwerydjsadhj41341423141432378898"    # 这种是写死了

2.问：上一个接口返回的参数，是下一个接口的请求参数，你是怎么解决的？
答：就是传"变量"，来"参数关联"就可以了。 ------> 期间：可能用到"格式化输出"
# 格式化输出
# 用 str 传递变量
'''