# -*- coding: utf-8 -*-
# file: 7.lianxi2.py
# author: zhuyao
# email: zzyyhshs@163.com


# 查询url
# 1.构建请求内容 url headers
import requests


def get_address_count():
    url = "http://127.0.0.1:8088/address/list?userId=2403129RFR1YK2NC"
    headers = dict()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    # 2.发送请求
    response = requests.post(url, headers=headers)
    # 3. 获取地址的数据
    address_data = response.json()["data"]
    # 4.返回一个地址数量
    return len(address_data)


# a. 查询地址数量
address_count_old = get_address_count()
# b. 新增
pass
# c. 再查询一次地址数量
address_count_new = get_address_count()
# d. 对2次的数据进行验证（断言）
assert address_count_old + 1 == address_count_new, "地址新增失败"



