'''
若以后 "调用登录" 时，只有 login(s)，没有"zhezhe"和"111111"
那么，在 "定义登录函数" 时，就要把 user="zhezhe"和 pwd="111111" 这两个默认值给加上
然后用 login(s) 才可以登录成功.(当仅有 s 一个参数时适用)
'''

import requests
from lxml import etree

'''将函数里面的账号和密码用参数表示，这就是 "参数化" 了'''

def yoy_login(s,user,pwd):
    """练习题目——登录"""
    url = "http://47.104.190.48:8000/login"
    r = s.get(url)


    demo = etree.HTML(r.text)
    nodes = demo.xpath('//input[@name="csrfmiddlewaretoken"]')
    csrfmiddlewaretoken = nodes[0].attrib["value"]


    url2 = "http://47.104.190.48:8000/login/json"
    body = {
        "csrfmiddlewaretoken":csrfmiddlewaretoken,    # 用 "变量" ，更具有 "普遍性"
        "username":user,
        "password":pwd
    }
    r2 = s.post(url2,data=body)
    print("登录结果：%s" % r2.text)
    return r2.json()

if __name__ == '__main__':
    s = requests.session()
    yoy_login(s,"zhezhe","111111")

