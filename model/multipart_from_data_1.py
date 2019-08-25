'''
post请求的body中的请求参数类型，有以下常见5种数据类型
1.application/json
2.application/x-www-form-urlencoded
3.multipart/form-data：表单提交，图片上传，附件上传
4.text/xml
5.还有文件下载格式：content-type：octets/stream

本节学习：multipart/form-data
1.表单提交
'''

import requests
import re
from model.yoy_login_3 import yoy_login
from requests_toolbelt import MultipartEncoder


def addStudent(s):
    url = "http://47.104.190.48:8000/xadmin/hello/student/add/"
    r = s.get(url)
    token = re.findall('name="csrfmiddlewaretoken" value="(.+?)"',r.text)
    print(token[0])

    url = "http://47.104.190.48:8000/xadmin/hello/student/add/"
    m = MultipartEncoder(            # 变成表单形式了
        fields=[
            ("csrfmiddlewaretoken",token[0]),
            ("csrfmiddlewaretoken",token[0]),
            ("student_id","999"),
            ("name","zz"),
            ("gender","F"),
            ("age","20"),
            ("_save","")
        ]
    )
    r2 = s.post(url,data=m,headers={"content-type":m.content_type})
    # print(r2.text)
    if "学生列表" in r2.text:
        print("添加学生成功！")
        return True
    else:
        print("添加学生失败！")
        return False

if __name__ == '__main__':
    s = requests.session()
    yoy_login(s,"zhezhe","111111")
    result = addStudent(s)
    print(result)