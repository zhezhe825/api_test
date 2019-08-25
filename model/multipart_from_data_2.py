'''
本节学习：multipart/form-data
2.上传图片
'''

import requests
import re
from model.yoy_login_3 import yoy_login
from requests_toolbelt import MultipartEncoder


def chuanTuPian():
    url = "http://47.104.190.48:8000/xadmin/hello/uploadimage/add/"
    r = s.get(url)
    token = re.findall('name="csrfmiddlewaretoken" value="(.+?)"',r.text)[0]


    url = "http://47.104.190.48:8000/xadmin/hello/uploadimage/add/"
    m = MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken",token),
            ("csrfmiddlewaretoken",token),
            ("name","11111111111"),
            ("image",("shu.jpg",open("D:\\上海—悠悠\\shu.jpg","rb"),"image/jpeg")),
            # ("image",("shu.jpg",open(r"D:\上海—悠悠\shu.jpg","rb"),"image/jpeg"))
            ("add_time_0","2019/08/20"),
            ("add_time_1","12:45"),
            ("initial-add_time_0","2019/08/20"),
            ("initial-add_time_1","12:45"),
            ("_save","")
        ]
    )

    r2 = s.post(url,data=m,headers={"content-type":m.content_type})
    if "传图片列表" in r2.text:
        print("传图片成功！")
    else:
        print("传图片失败！")

if __name__ == '__main__':
    s = requests.session()
    yoy_login(s,"zhezhe","111111")
    chuanTuPian()