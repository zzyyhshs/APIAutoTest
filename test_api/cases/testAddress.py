# -*- coding: utf-8 -*-
# file: testAddress.py
# author: zhuyao
# email: zzyyhshs@163.com
import allure
import pytest
import requests

from common.decorators import logs

@allure.feature("美食宇宙项目")
@allure.story("地址相关用例")
class TestAddress:

    @logs
    @allure.title("添加地址")
    @allure.link("www.baidu.com")
    def test_address_add(self, base_url, header_json, data_driven_to_uri, data_driven_to_body):
        url = f'{base_url}{data_driven_to_uri}'
        res = requests.post(url=url, headers=header_json, json=data_driven_to_body)
        assert res.status_code == 200

    @logs
    @allure.title("删除地址")
    @allure.link("www.bing.com")
    def test_address_delete(self, base_url, header_json, data_driven_to_uri, data_driven_to_userId, data_driven_to_addressId):
        url = f'{base_url}{data_driven_to_uri}?userId={data_driven_to_userId}&addressId={data_driven_to_addressId}'
        header = dict()
        header['Accept'] = 'application/json'
        header['Content-Type'] = 'application/json'
        res = requests.post(url=url, headers=header_json)
        assert res.status_code == 200



if __name__ == '__main__':
    pytest.main(["-vs", "testAddress.py"])
