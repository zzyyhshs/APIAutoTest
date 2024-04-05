# -*- coding: utf-8 -*-
# file: config.py
# author: zhuyao
# email: zzyyhshs@163.com

# python的内置模块
import logging
import os
# 创建一个logger对象，这个对象可以帮助我们打印，保存log日志
logger = logging.getLogger("my_auto_test")

BASE_DIR = os.path.dirname(__file__)  # 根目录 d:/woniu_robot


def get_path(*test_case_files):
    return os.path.join(BASE_DIR, *test_case_files)


class APIConfig():
    '''
    接口相关的全局配置
    '''
    ALLURE_TEMP_DIR_PATH = get_path("test_api", "report", "temp") # 临时目录的路径
    ALLURE_REPORT_DIR_PATH = get_path("test_api", "report", "allure-report") # 测试报告的目录的路径

    ALLURE_BIN_PATH = get_path("common", "allure-2.8.1", "bin")
    # # 场景 1 : 登录-----新增动物类别----删除动物类别
    # SUIT_MODULE_1 = [path("test_add_category.py") , path("test_del_category.py")]
    # # 场景 2 :  分配笼位场景
    # SUIT_MODULE_2 = [path("test_suite_1.py")]


    TEST_SUITE_1 = [get_path("test_api", "cases", "testAddress.py")]

    TEST_SUITE_2 = [get_path("test_api", "cases", "testLogin.py")]

    SUITE_ALL = TEST_SUITE_1

