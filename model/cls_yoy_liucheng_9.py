import requests
from lxml import etree

class YoyLiuCheng():
    def __init__(self,s):
        self.s = s

    def yoy_login(self,user,pwd):
        """练习题目——登录"""
        url = "http://47.104.190.48:8000/login"
        r = s.get(url)


        demo = etree.HTML(r.text)
        nodes = demo.xpath('//input[@name="csrfmiddlewaretoken"]')
        csrfmiddlewaretoken = nodes[0].attrib["value"]


        url2 = "http://47.104.190.48:8000/login_test/"
        body = {
            "csrfmiddlewaretoken":csrfmiddlewaretoken,
            "username":user,
            "password":pwd
        }
        r2 = s.post(url2,data=body)
        if "登录成功！" in r2.text:
            print("登录成功！")
        else:
            print("登录失败！")

    def yoy_add_info(self,name,sex):
        url = "http://47.104.190.48:8000/user/info"
        body = {
             "name":name,
             "sex":sex
            }
        r3 = s.post(url,data=body)
        if "msg" in r3.json():
            print("updata success!")
        else:
            print("用户新增信息失败！")

    def yoy_get_info(self):
        url = "http://47.104.190.48:8000/user/get/info/get"
        r4 = s.get(url)
        print(r4.json())

        assert r4.json()["sex"] == "女"


if __name__ == '__main__':
    s = requests.session()
    g = YoyLiuCheng(s)
    g.yoy_login("zhezhe","111111")
    g.yoy_add_info("zzhe","女")
    g.yoy_get_info()