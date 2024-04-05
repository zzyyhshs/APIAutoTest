# -*- coding: utf-8 -*-
# file: test_func.py
# author: zhuyao
# email: zzyyhshs@163.com


import pytest

# 定义一个带参数的 fixture
# 全局的数据驱动
@pytest.fixture(params=[1, 2, 3, 4])
def input_data(request):
    print("\n当前的参数:", request.param)
    print("当前的测试用例名称:", request.node.name)
    return request.param


# 使用参数化的 fixture 进行测试
# indirect默认为False，如果设置为True则表示当前的参数input_data可以被fixture所接管
# 只针对单个测试函数
# @pytest.mark.parametrize("input_data", [1,2,3,4], indirect=True)
def test_input_data(input_data):
    assert input_data < 4


if __name__ == '__main__':
    pytest.main(["-vs", "./test_func.py"])