# -*- coding: utf-8 -*-
# file: test_function1.py
# author: zhuyao
# email: zzyyhshs@163.com
import pytest


def add(x, y):
    return x + y

# 通过function编写测试用例
# @pytest.mark.run(order=2)
def test_addition():
    # 第一个执行
    assert add(1, 2) == 3


# @pytest.mark.run(order=1)
def test_subtraction():
    # 第二个执行
    assert add(5, 3) == 2

if __name__ == '__main__': # 以当前脚本为主路径执行的时候，才会判断通过
    # pytest.main(列表)
    result = pytest.main(["-vs", "./test_function1.py"])

