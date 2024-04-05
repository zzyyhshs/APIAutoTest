# -*- coding: utf-8 -*-
# file: test_example.py.py
# author: zhuyao
# email: zzyyhshs@163.com

import pytest


def func(x):
    return x + 1


def test_answer():
    # 第一条测试用例
    assert func(3) == 5, "两个数不一致"


def test_answer2():
    # 第一条测试用例
    assert func(4) == 5, "两个数不一致"


def test_answer3():
    # 第一条测试用例
    assert func2(4) == 5, "函数不存在"


if __name__ == '__main__': # 以当前脚本为主路径执行的时候，才会判断通过
    # pytest.main(列表)
    result = pytest.main(["-vs", "./test_example.py"])
    # 检查测试结果并作出相应的处理
    if result == 0:
        print("所有测试用例通过！")
    else:
        print("有测试用例失败，请查看详细信息。")

