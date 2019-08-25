# 下载图片的案例

from requests_html import HTMLSession

session = HTMLSession()
url = "http://699pic.com/sousuo-218808-13-1.html"
r = session.get(url)

image = r.html.find('.lazy')
for i in image:
    title = i.attrs.get('title')   # 全部属性的title属性
    img_url = i.attrs.get('data-original')   # 地址
    # print(title)
    # print(img_url)
    r2 = session.get(img_url)
    try:
        with open("%s.jpg" % title,"wb") as fp:     # 保存到本地：用 open函数
            fp.write(r2.content)
    # except:
    #     pass

    except Exception as msg:
        print("下载过程中出现一些异常：%s" % msg)

