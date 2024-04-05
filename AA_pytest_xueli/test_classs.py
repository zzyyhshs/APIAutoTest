# -*- coding: utf-8 -*-
# file: test_classs.py
# author: zhuyao
# email: zzyyhshs@163.com
import pytest


def add(x, y):
    return x + y


# 通过function编写测试用例

def test_addition_func():
    assert add(1, 4) == 3


class TestMathOperations:

    def setup_method(self):
        # 类似unittest中的setup方法
        print("\n初始化测试环境")

    def teardown_method(self):
        # 类似unittest中的teardown方法
        print("\n清理测试环境")

    def test_addition(self):
        assert add(1, 2) == 3, "类管理用例比对成功"

    def test_subtraction(self):
        assert add(5, 3) == 2, "类管理用例比对错误"


if __name__ == '__main__': # 以当前脚本为主路径执行的时候，才会判断通过
    # pytest.main(列表)
    result = pytest.main(["-vs", "./test_classs.py"])

