# -*- coding: utf-8 -*-
# file: testCarousel.py
# author: zhuyao
# email: zzyyhshs@163.com

import requests
'''
获取首页轮播图列表
'''


def test_index_carousel(base_url, header_json):
    url = f'{base_url}/index/carousel'
    res = requests.get(url=url, headers=header_json)
    assert res.status_code == 200

