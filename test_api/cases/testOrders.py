# -*- coding: utf-8 -*-
# file: testOrders.py
# author: zhuyao
# email: zzyyhshs@163.com
import requests


def test_orders_create(base_url, header_json):
    url = f'{base_url}/orders/create'
    data = {
        "addressId": "240331CWY2KS50BC",
        "itemSpecIds": "cake-1005-spec-1",
        "leftMsg": "leftMsg",
        "payMethod": 0,
        "userId": "2403129RFR1YK2NC"
    }
    res = requests.post(url=url, headers=header_json, json=data)
    assert res.status_code == 200


def test_orders_getPaidOrderInfo(base_url, header_json):
    url = f'{base_url}/orders/getPaidOrderInfo'
    data = {
        "addressId": "240331CWY2KS50BC",
        "itemSpecIds": "cake-1005-spec-1",
        "leftMsg": "leftMsg",
        "payMethod": 0,
        "userId": "2403129RFR1YK2NC"
    }
    res = requests.post(url=url, headers=header_json, json=data)
    assert res.status_code == 200
