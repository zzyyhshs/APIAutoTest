# -*- coding: utf-8 -*-
# file: test_ddt.py
# author: zhuyao
# email: zzyyhshs@163.com



import pytest


def add(x, y):
    return x + y

"""
(str, list)

[(), (), ...]
每一个元组表示一条数据，元组中的数据数量和定义函数中的接收参数数量一致

人话：定义一个测试方法，有多少条数据，执行多少次
"""
@pytest.mark.parametrize("x, y, expected", [
    (i, i+1, i*2+1) for i in range(10)
])
def test_addition_func(x, y, expected):
    assert add(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (5, 3, 8),
    (10, -5, 5)
])
def test_addition_func2(x, y, expected):
    assert add(x, y) == expected


class TestMathOperations:
    @pytest.mark.parametrize("x, y, expected", [
        (1, 2, 3),
        (5, 3, 8),
        (10, -5, 5)
    ])

    def test_addition_class(self, x, y, expected):
        assert add(x, y) == expected


if __name__ == '__main__':
    pytest.main(["-vs", "-m=smoke", "./test_ddt.py"])

