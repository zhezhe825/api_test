'''
本节学习：multipart/form-data
3.上传附件
'''

import requests
import re
from model.yoy_login_3 import yoy_login
from requests_toolbelt import MultipartEncoder


def chuanWenJian():
    url = "http://47.104.190.48:8000/xadmin/hello/fileimage/add/"
    r = s.get(url)
    token = re.findall('name="csrfmiddlewaretoken" value="(.+?)"',r.text)[0]


    url = "http://47.104.190.48:8000/xadmin/hello/fileimage/add/"
    m = MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken",token),
            ("csrfmiddlewaretoken",token),
            ("title","7777777777777"),
            ("image",("shu.jpg",open("D:\\上海—悠悠\\shu.jpg","rb"),"image/jpeg")),
            ("fiels",("shu.jpg",open(r"D:\上海—悠悠\shu.jpg","rb"),"image/jpeg")),
            ("_save","")
        ]
    )

    r2 = s.post(url,data=m,headers={"content-type":m.content_type})
    if "上传文件和图片列表 " in r2.text:
        print("传文件成功！")
    else:
        print("传文件失败！")

if __name__ == '__main__':
    s = requests.session()
    yoy_login(s,"zhezhe","111111")
    chuanWenJian()