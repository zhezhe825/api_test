import requests
from lxml import etree

s = requests.session()
url = "https://www.cnblogs.com/yoyoketang/ajax/news.aspx"
r = s.get(url)

demo = etree.HTML(r.text)
nodes = demo.xpath('//*[@id="profile_block"]')[0]  # 00.一次定位
print(nodes.text)

# fu = nodes.xpath('text()')  # 01.二次定位
# print(fu)
# zi = nodes.xpath('a')    # 01.二次定位
# for i,j in zip(fu,zi):   # 02.两个for循环：用zip
#     print("%s%s" % (i,j.text))

print(nodes.tag)   # 1.获取tag
print(nodes.attrib)   # 2.除了tag 和text的其他属性,用：attrib
print(nodes.get("id"))  # 3.获取某一个属性，用：get

print(nodes.iter())   # 4.获取所有的子节点,用：iter()
for i in nodes.iter():
    print(i.text)

print(nodes.text)   # 获取当前节点下的第一个文本元素
print(nodes.xpath('text()'))   # 5.获取当前节点下的所有的文本元素，用：text()
print(nodes.xpath('.//text()'))  # 6.获取本节点和子节点（子子孙孙节点）的所有文本元素，
                                  # 用：.//text()