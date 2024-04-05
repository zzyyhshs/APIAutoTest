# -*- coding: utf-8 -*-
# file: my_allure.py
# author: zhuyao
# email: zzyyhshs@163.com
import os
import shutil
import time

from config import APIConfig


def mk_trend(config:APIConfig):
    '''
    生成趋势图
    :param config:
    :return:
    '''
    ALLURE_REPORT_HISTORY = os.path.join(config.ALLURE_REPORT_DIR_PATH , "history")
    ALLURE_TEMP_HISTORY = os.path.join(config.ALLURE_TEMP_DIR_PATH , "history")

    # 首先需要删除temp目录下。存在的history
    if  os.path.exists(ALLURE_TEMP_HISTORY):
        # 删除目录以及目录下的所有文件
        shutil.rmtree(ALLURE_TEMP_HISTORY)
    # 从report目录中。复制history目录树。到 temp的hisotry
    shutil.copytree(ALLURE_REPORT_HISTORY , ALLURE_TEMP_HISTORY)



def generate_allure_report(config: APIConfig):
    '''
    生成测试报告的代码
    :return:
    '''
    # 根据临时文件，生成正式的测试报告
    # 执行生成测试报告的命令
    # .../bin/allure generate -c 存放一个临时文件的路径 -o 生成的测试报告路径
    cmd = f"{config.ALLURE_BIN_PATH}/allure generate -c {config.ALLURE_TEMP_DIR_PATH} -o {config.ALLURE_REPORT_DIR_PATH}"
    print(cmd)
    os.popen(cmd) # python调用操作系统的命令
    # time.sleep(5)
    mk_trend(config)