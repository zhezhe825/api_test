from model.yoy_login_3 import yoy_login
import requests

def yoy_add_info(s,name,sex):
    url = "http://47.104.190.48:8000/user/info"
    body = {
         "name":name,
         "sex":sex
        }
    r3 = s.post(url,data=body)
    # assert r3.json()["msg"] == "updata success!"

    return r3.json()

if __name__ == '__main__':
    s = requests.session()
    yoy_login(s,"zhezhe","111111")
    yoy_add_info(s,"zzhe","女")