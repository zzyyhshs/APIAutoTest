# -*- coding: utf-8 -*-
# file: 1.function_view.py
# author: zhuyao
# email: zzyyhshs@163.com


# pytest自动加载我们的测试方法，会自动执行
# 参数化，在pytest自动执行的时候如何传递参数
def test_a(a, b):
    print(a, b)


test_a()
