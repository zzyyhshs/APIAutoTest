# -*- coding: utf-8 -*-
# file: 1.request_get.py
# author: zhuyao
# email: zzyyhshs@163.com

import requests

url = "http://127.0.0.1:8088/index/carousel"
headers = dict()
headers["Accept"] = "application/json"

# response = requests.get(url=url)
response = requests.get(url, headers=headers)

# 检查响应状态码
"""
response.status_code：获取响应状态码，int类型
response.text：获取响应文本，str类型
response.headers：获取响应头，requests.structures.CaseInsensitiveDict类型
response.json()：获取反序列化后的json对象
"""

if response.status_code == 200:
    # 打印响应内容
    print("Response Content:", type(response.text))
    print(response.text)
    # 获取json格式
    print("Response Content to json:", type(response.json()))
    print(response.json())
    # 打印响应头
    print("Response Headers:", type(response.headers))
    print(response.headers)
    print(response.headers['Content-Type'])
else:
    print("Error:", response.status_code)


"""
发送一个get请求并添加断言：
1.对响应状态码的断言
2.对响应文本进行断言
"""

code = 200
assert code==200, "响应状态码错误"

