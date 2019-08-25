from model.yoy_login_3 import yoy_login
import requests



def yoy_get_info(s):
    url = "http://47.104.190.48:8000/user/get/info/get"
    r4 = s.get(url)
    print(r4.json())

    assert r4.json()["sex"] == "女"

if __name__ == '__main__':
    s = requests.session()
    yoy_login(s,"zhezhe","111111")
    yoy_get_info(s)