# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# 这个不用安装，内置模块，作用实现python脚本通过命令行的方式执行
import argparse

import pytest

from common.my_allure import generate_allure_report
from config import APIConfig





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 创建一个Argparse对象
    parser = argparse.ArgumentParser(description="")
    # 添加--type这个参数，并且 给定这个参数的选项，以及默认值
    parser.add_argument('--type', choices=['1', '2', 'all'], default="all")
    # 获取命令行 --type=xxx 项
    args = parser.parse_args()
    print(args.type)
    if args.type == "all":
        pytest.main(APIConfig.SUITE_ALL)
    elif args.type == "1":
        pytest.main(APIConfig.TEST_SUITE_1)
    elif args.type == "2":
        pytest.main(APIConfig.TEST_SUITE_2)
    generate_allure_report(APIConfig)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
