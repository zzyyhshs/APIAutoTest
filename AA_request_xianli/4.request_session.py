# -*- coding: utf-8 -*-
# file: 4.request_session.py
# author: zhuyao
# email: zzyyhshs@163.com
import requests

# 创建一个session对象
session = requests.session()
# 打印一下
print("初始创建cookies:", session.cookies)


url = "http://127.0.0.1:8088/passport/login"
headers = dict()
headers["Content-Type"] = "application/json"
headers["Accept"] = "application/json"
json_data = {
  "confirmPassword": "123456",
  "password": "123456",
  "username": "test12"
}
response = session.post(url, headers=headers, json=json_data)
print(response.status_code, response.text)
# 添加一个cookies
session.cookies["aa"] = "hhhhh"
# 通过session保存cookies，在下面的接口可以重复使用
print("登陆请求cookies:", session.cookies)


response = session.get("http://127.0.0.1:8088/index/carousel")
print(response.status_code, response.text)
