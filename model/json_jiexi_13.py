'''
为什么有时候 print(r.json()) 会报错？
报错：json.decoder.JSONDecodeError
因为：返回的是html页面, 并不是json的,你再 r.json() 当然会报错。
'''

# 一、报错：json.decoder.JSONDecodeError
import requests
import urllib3
urllib3.disable_warnings()
url2 = "https://www.cnblogs.com/yoyoketang/"
r2 = requests.get(url2, verify=False)
print(r2.text)       # str, 返回 html 页面
# print(r2.json())   # json.decoder.JSONDecodeError

'''
正解是把 r.text 的结果复制出来,json在线解析 —>看是不是json格式 —>
是：再执行 r.json()
'''

# 二、响应内容为字典的2种表达形式
import requests
import json
url = "http://japi.juhe.cn/qqevaluate/qq"
par = {
     "key": "8dbee1fcd8627fb6699bce7b986adc45",
     "qq":  "283340479"
}
r = requests.get(url,params=par)
# 方法一：
print(r.json())  # 字典：requests直接封装好了,把json转换成dict

# 方法二：
print(r.text)           # str：json的str
a = json.loads(r.text)  # 转字典
print(a)
