# -*- coding: utf-8 -*-
# file: 05.chrome_option.py
# author: zhuyao
# email: zzyyhshs@163.com

from selenium import webdriver


from config import UIConfig

def create_chrome_option():
    """配置chrome option"""
    options = webdriver.ChromeOptions()
    # 设置默认文件下载地址
    options.add_experimental_option('prefs', {'download.default_directory': "./download/"})
    # 谷歌无头模式
    options.add_argument('--headless')
    # 设置最大化窗口
    options.add_argument('--start-maximized')
    # 指定chrome浏览器的启动路径
    # options.binary_location = r"C:\Users\15064\AppData\Local\Google Chrome\App\chrome.exe"
    return options

options = create_chrome_option()
# 1.打开浏览器
driver = webdriver.Chrome(executable_path=UIConfig.CHROME_DRIVER_PATH, options=options)


