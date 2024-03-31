# -*- coding: utf-8 -*-
# file: raise_error.py
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
  "mobile": "string",
  "province": "string",
  "receiver": "string",
  "userId": "string"
}
# response = requests.post(url, headers=headers, json=json_data)
response = requests.post(url, headers=headers, data=json_data)
response.raise_for_status()

print(response.status_code)
print(response.text)