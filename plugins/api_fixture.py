# -*- coding: utf-8 -*-
# file: api_fixture.py
# author: zhuyao
# email: zzyyhshs@163.com
import pytest

from test_api.datas.data import my_datas


def pytest_addoption(parser):
    # 必须有addini这一步，声明这个pytest.ini里面会有一个变量
    parser.addini(name="base_url", help="接口的baseurl", default="127.0.0.1")
    # 必须有addini这一步，声明这个pytest.ini里面会有一个变量
    parser.addini(name="port", help="端口", default="8080")


# 作用于函数
@pytest.fixture(scope="session")
def header_json():
    print("header_json执行一次")
    header = dict()
    header['Accept'] = 'application/json'
    header['Content-Type'] = 'application/json'
    return header


# 作用于函数
@pytest.fixture()
def header_text():
    header = dict()
    header['Accept'] = 'application/json'
    header['Content-Type'] = 'application/text'
    return header


# 作用于函数
@pytest.fixture(scope="session")
def base_url(pytestconfig):
    print("base_url执行一次")
    base_url = pytestconfig.getini("base_url")
    port = pytestconfig.getini("port")
    return f"{base_url}:{port}"



@pytest.fixture()
def data_driven_to_uri(request):
    return my_datas[request.function.__name__]["uri"]


@pytest.fixture()
def data_driven_to_body(request):
    return my_datas[request.function.__name__]["body"]


@pytest.fixture()
def data_driven_to_userId(request):
    return my_datas[request.function.__name__]["userId"]


@pytest.fixture()
def data_driven_to_addressId(request):
    return my_datas[request.function.__name__]["addressId"]


