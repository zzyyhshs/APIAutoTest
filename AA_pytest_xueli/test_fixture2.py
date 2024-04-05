# -*- coding: utf-8 -*-
# file: test_fixture2.py
# author: zhuyao
# email: zzyyhshs@163.com


import pytest

@pytest.fixture()
def base_user():
    print("base user fixture")
    return {"username": "test123", "password": "123"}


@pytest.fixture()
def username(base_user):
    print("username fixture")
    return base_user["username"]


@pytest.fixture()
def password(base_user):
    print("password fixture")
    return base_user["password"]


# 测试函数，通过参数传递 Fixture 函数的名称来使用 Fixture
def test_login(username, password):
    assert username=="test123" and password=="123", "身份验证失败"


if __name__ == '__main__':
    pytest.main(["-vs", "./test_fixture2.py"])
