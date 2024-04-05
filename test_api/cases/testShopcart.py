# -*- coding: utf-8 -*-
# file: test_shopcart.py
# author: zhuyao
# email: zzyyhshs@163.com

import requests
'''
添加商品到购物车
'''


def test_shopcart_add(base_url, header_json):
    url = f'{base_url}/shopcart/add?userId=240331BYFKGANC00'
    data = {
        "buyCounts": 1,
        "itemId": "cake-1005",
        "itemImgUrl": "itemImgUrl",
        "itemName": "进口美食凤梨酥",
        "priceDiscount": "16020",
        "priceNormal": "17800",
        "specId": "cake-1005-spec-1",
        "specName": "巧克力"
    }
    res = requests.post(url=url, headers=header_json, json=data)
    assert res.status_code == 200

