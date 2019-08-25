from requests_html import HTMLSession

session = HTMLSession()   # 00.类似于：打开无界面的浏览器
url = "https://www.cnblogs.com/yoyoketang/tag/django/"
r = session.get(url)
r.html.render()    # 01.是一种看不见的浏览器，具有渲染作用

print(r.html.links)   # 02.获取页面全部链接（相对地址+绝对地址）
print(r.html.absolute_links)  # 03.绝对路径链接

# t = r.html.xpath('//*[@class="postTitl2"]')   # 1.xpath语法
t = r.html.find('.postTitl2')   # 2.css语法
for i in t:
    print(i.text)
    print(i.absolute_links)

t1 = r.html.find('.postTitl2',first=True)   # 3.只获取第一个内容：加first=True
t2 = r.html.find('.postTitl2>a',first=True)
# print(t2)
# print(t2.html)  # 返回的是：html 的原始数据
print(t2.text)
print(t2.absolute_links)

print(t2.attrs)    # 4.获取全部属性：attrs --> 字典
print(t2.attrs["href"])

print(t2.search('python测{}联动')) # 5.搜索文本：search 类似正则 ,知道前后取中间 —> 前{}后
print(t2.search('python测{}联动')[0])
