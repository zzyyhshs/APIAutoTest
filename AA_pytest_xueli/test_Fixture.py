# -*- coding: utf-8 -*-
# file: fixture.py
# author: zhuyao
# email: zzyyhshs@163.com


import pytest
from common.my_common import authenticate



# 测试函数，通过参数传递 Fixture 函数的名称来使用 Fixture
def test_login(user_data, db_connection):
    user = authenticate(user_data["username"], user_data["password"])
    assert user.is_authenticated, "身份验证失败"


if __name__ == '__main__':
    pytest.main(["./test_Fixture.py"])