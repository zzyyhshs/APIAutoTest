# -*- coding: utf-8 -*-
# file: 02.element_dingwei.py
# author: zhuyao
# email: zzyyhshs@163.com
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from config import UIConfig

# 1.打开浏览器
driver = webdriver.Chrome(executable_path=UIConfig.CHROME_DRIVER_PATH)
# driver = webdriver.Firefox(executable_path=Firefox_driver_path)
# driver = webdriver.Ie(executable_path=Ie_driver_path)
# 2.打开网页
driver.get("http://www.baidu.com/")
# 3.获取在百度搜索框的元素
element = driver.find_element_by_id("kw")
# find_elements返回的是一个列表，列表里面包含的是元素定位到的所有的元素
# element = driver.find_elements_by_id("kw")
# 在百度搜索款中输入"UI自动化"，element.send_keys()

# ========元素操作=========
element.send_keys("UI自动化")


time.sleep(3)
# 4.获取百度一下按钮的元素
element = driver.find_element_by_id("su")
# 点击百度一下的按钮，element.click()
element.click()
# 悬停
ActionChains(driver).move_to_element(element).perform()


# ========浏览器操作=========
time.sleep(3)
# 5.截图，保存
driver.save_screenshot("百度.png")
# 刷新
driver.refresh()
# 返回
driver.back()
# 前进
driver.forward()
# 窗口最大化
driver.maximize_window()

# 获取所有的窗口，返回一个列表，列表中的元素是每一窗口的handle
window_handles = driver.window_handles()
# 切换窗口参数传递窗口handle，也可以直接传递窗口的name
driver.switch_to.window(window_handles[0])

# 6.关闭浏览器
driver.quit()

# 关闭当前页签
driver.close()


