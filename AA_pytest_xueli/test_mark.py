# -*- coding: utf-8 -*-
# file: test_mark.py
# author: zhuyao
# email: zzyyhshs@163.com



import pytest

def add(x, y):
    return x + y

@pytest.mark.smoke
def test_addition_smoke():
    assert add(1, 2) == 3

@pytest.mark.regress
def test_subtraction_regress():
    assert add(5, 3) == 2


class TestMathOperations:

    def setup_method(self):
        # 类似unittest中的setup方法
        print("\n初始化测试环境")

    def teardown_method(self):
        # 类似unittest中的teardown方法
        print("\n清理测试环境")

    # 有的函数名会携带特殊功能
    @pytest.mark.smoke123123
    def test_addition_smoke2(self):
        assert add(1, 2) == 3, "类管理用例比对成功"

    @pytest.mark.regress
    def test_subtraction_regress2(self):
        assert add(5, 3) == 2, "类管理用例比对错误"


if __name__ == '__main__':
    pytest.main(["-vs", "-m=smoke", "./test_mark.py"])


