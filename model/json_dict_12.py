'''
dict 和 json 的区别：print打印出：
                     json实际类型为str,{}内为："" true false null []
                     dict的{}内为：'' True False None () []
'''

import json

# 一：dict、list、tuple 转 json

# 1.dict 转 json
k1 = {"a":1,          # dict
     "b":12.3,
     "c":True,
     "d":False,
     "f":None,
     "g":(1,2,3,4),
     "k":[1,2,3,4],
     "avc":{
         "ad":"1111",
         "cd":"2333"
     }}
a = json.dumps(k1)   # dumps：转成了json
print(a)             # 双引号"" true false null，对比字典 k 的打印结果看
                     # 可借助：“json在线解析”来核对
print(type(a))       # json 的类型为：str

# b = '{"a": 1, "b": 12.3, "c": true, "d": false, "f": null, "g": [1, 2, 3, 4], "k": [1, 2, 3, 4], "avc": {"ad": "1111", "cd": "2333"}}'
# print(b)
# print(type(b))     b：实际为：json格式的str

# 2.list 转 json
k2 = [1,2,True,False,None,"adbd"]
b = json.dumps(k2)       # dumps
print(b)

# 3.tuple 转 json
k3 = (1,2,True,False,None,"adbd")
c = json.dumps(k3)
print(c)


# 二：json 转 dict
# 标准的json格式的字符串
k4 = '{"a": 1, "b": 12.3, "c": true, "d": false, "f": null, "g": [1, 2, 3, 4], "k": [1, 2, 3, 4], "avc": {"ad": "1111", "cd": "2333"}}'
d = json.loads(k4)
print(d)
print(type(d))

result = d["avc"]["cd"]
result1 = d.get("avc").get("cd1","错了！")
# 需求：不知道返回的字典里面有没有这个key，如果有，则取值，没有给个默认值
# 用：  字典.get
print(result)
print(result1)


# 三：dict、str 互转
# 1.dict 转 str
k5 = {"aa":True,
     "bb":"ccccc"}
e = str(k5)     # str
print(e)
print(type(e))

# 2.str 转 dict
k6 = b = '{"aa":True, "bb":"ccccc"}'
f = eval(k6)       # eval函数
print(f)
print(type(f))

