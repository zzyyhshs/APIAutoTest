# -*- coding: utf-8 -*-
# file: conftest.py
# author: zhuyao
# email: zzyyhshs@163.com

# 在这个文件中定义fixture
# import pytest
#
#
# @pytest.fixture()
# def user_data():
#     print("执行user_data fixture")
#     # 定义一个 Fixture 函数，用于提供测试数据
#     return {"username": "testuser", "password": "password123"}


# 定义一个pytest_plugins变量，这个变量类型是一个元组
# 导入: 模块.文件
pytest_plugins = ("plugins.my_fixture")

