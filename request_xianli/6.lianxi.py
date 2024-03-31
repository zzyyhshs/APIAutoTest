# -*- coding: utf-8 -*-
# file: 6.lianxi.py
# author: zhuyao
# email: zzyyhshs@163.com

import requests

class Address:
    def __init__(self, id, mobile, userId, **kwargs):
        self.id = id
        self.mobile = mobile
        self.userId = userId
        # print(kwargs)

    def __str__(self):
        return "地址id:%s，当前用户的id:%s，电话:%s" % (self.id, self.userId, self.mobile)



# 查询url
# 1.构建请求内容 url headers
url = "http://127.0.0.1:8088/address/list?userId=2403129RFR1YK2NC"
headers = dict()
headers["Content-Type"] = "application/json"
headers["Accept"] = "application/json"
# 2.发送请求
response = requests.post(url, headers=headers)

# 3.判断一下是否请求成功
assert "OK" in response.text, "请求异常:%s" % response.text

# 如果没有data不会报错
# address_data = response.json().get("data", {})
# 如果没有data会报错
address_data = response.json()["data"]
for item in address_data:
    """
    {
      "id": "240317B5MWACA0SW",
      "userId": "2403129RFR1YK2NC",
      "receiver": "string",
      "mobile": "13112341234",
      "province": "上海",
      "city": "上海",
      "district": "string",
      "detail": "string",
      "extand": null,
      "isDefault": 0,
      "createdTime": "2024-03-17T07:41:48.000+0000",
      "updatedTime": "2024-03-17T07:41:48.000+0000"
    }
    """
    # 拆包
    address = Address(**item)
    print(address)




