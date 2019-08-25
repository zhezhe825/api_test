# 获取隐藏参数
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()

s = requests.session()
s.verify=False
url = "https://account.chsi.com.cn/passport/login"
r = s.get(url)


demo = etree.HTML(r.text)
nodes = demo.xpath('//input[@name="lt"]')
lt = nodes[0].get('value')
nodes = demo.xpath('//input[@name="execution"]')
execution = nodes[0].get('value')


body = {
    "username":"847892758927",
    "password":"2374987987",
    "submit":"登录",
    "lt":lt,
    "execution":execution,
    "_eventId":"submit"
}
r2 = s.post(url,data=body)
if "登录_学信网" in r2.text:
    print("成功！")
else:
    print("失败！")


'''
demo = etree.HTML(r.text)
nodes = demo.xpath('//input[@name="csrfmiddlewaretoken"]')
csrfmiddlewaretoken = nodes[0].attrib["value"]

yoy_login_3.py中，是： .attrib('value')
在本模块中，是： .get('value')
'''