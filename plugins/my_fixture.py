# -*- coding: utf-8 -*-
# file: my_fixture.py
# author: zhuyao
# email: zzyyhshs@163.com
import pytest

from common.my_common import Connection


@pytest.fixture()
def user_data():
    print("执行user_data fixture")
    # 定义一个 Fixture 函数，用于提供测试数据
    return {"username": "testuser", "password": "password1234"}


@pytest.fixture()
def db_connection():
    print("执行db_connection fixture")
    # 定义一个 Fixture 函数，用于连接数据库
    connection = Connection()
    yield connection  # 使用 yield 关键字，可以在测试函数执行完后继续执行后续清理操作
    connection.close()  # 在 Fixture 函数的最后执行清理操作


@pytest.fixture()
def my_fixture():
    print("执行my_fixture fixture")




