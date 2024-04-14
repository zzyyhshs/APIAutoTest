# -*- coding: utf-8 -*-
# file: 01.rumenshiyon.py
# author: zhuyao
# email: zzyyhshs@163.com

# 导包
from selenium import webdriver
import time

from config import UIConfig

# 1.打开浏览器
driver = webdriver.Chrome(executable_path=UIConfig.CHROME_DRIVER_PATH)
# driver = webdriver.Firefox(executable_path=Firefox_driver_path)
# driver = webdriver.Ie(executable_path=Ie_driver_path)
# 2.打开网页
driver.get("http://www.baidu.com/")
# 3.在百度搜索框中输入"UI自动化"
driver.find_element_by_id("kw").send_keys("UI自动化")
time.sleep(3)
# 4.点击搜索一下按钮
driver.find_element_by_id("su").click()
time.sleep(3)
# 5.截图，保存
driver.save_screenshot("百度.png")
# 6.关闭浏览器
driver.quit()
