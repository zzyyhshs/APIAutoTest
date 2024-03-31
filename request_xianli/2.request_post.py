# -*- coding: utf-8 -*-
# file: 2.request_post.py
# author: zhuyao
# email: zzyyhshs@163.com

import requests
import json

url = "http://127.0.0.1:8088/address/add"
headers = dict()
headers["Content-Type"] = "application/json"
headers["Accept"] = "application/json"
json_data = {
  "addressId": "string",
  "city": "string",
  "detail": "string",
  "district": "string",
  "mobile": "13111111111",
  "province": "string",
  "receiver": "string",
  "userId": "string"
}
json_str = json.dumps(json_data)

"""
# 在请求时会自动讲数据对象进行json序列化
json：如果要发送的是反序列化后的json
data：发送文本格式的，str
headers：请求头
"""
# response = requests.post(url, headers=headers, json=json_data)
response = requests.post(url, headers=headers, data=json_str)


print(response.status_code)
print(response.text)


