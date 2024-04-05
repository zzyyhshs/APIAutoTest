# -*- coding: utf-8 -*-
# file: testLogin.py
# author: zhuyao
# email: zzyyhshs@163.com
import requests


"""
写框架的时候
1. 尽可能少的去写代码

"""

def test_login(base_url, header_json):
    url = f'{base_url}/passport/login'
    data = {
        "confirmPassword": "123456",
        "password": "123456",
        "username": "test12"
    }
    res = requests.post(url=url, headers=header_json, json=data)
    assert res.status_code == 200

