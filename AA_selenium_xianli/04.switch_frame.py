# -*- coding: utf-8 -*-
# file: 04.switch_frame.py
# author: zhuyao
# email: zzyyhshs@163.com

from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import UIConfig

# 1.打开浏览器
driver = webdriver.Chrome(executable_path=UIConfig.CHROME_DRIVER_PATH)

# 传递frame_name
driver.switch_to.frame('frame_name')
# 索引
driver.switch_to.frame(1)
# 元素
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])



