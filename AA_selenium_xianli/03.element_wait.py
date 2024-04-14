# -*- coding: utf-8 -*-
# file: 03.元素等待.py
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


# ======元素等待的第一种方式:强制等待======
time.sleep(10)

# ======元素等待的第二种方式:隐式等待======
# 是一个全局，设置之后，后面所有的元素获取都会进行等待
driver.implicitly_wait(3)
# 调用find_element就会触发隐式等待
# 如果元素获取不到，那么就会一直等待，如果超过设置的时间，那么就会报错
# 如果元素提前获取到了，那么就跳出等待，直接返回元素
element = driver.find_element_by_id("kw")


# ======元素等待的第三种方式:显式等待======
# 每一个元素都需要进行等待，
# 如果元素获取不到，那么就会一直等待，如果超过设置的时间，那么就会报错
# 如果元素提前获取到了，那么就跳出等待，直接返回元素
element = WebDriverWait(driver, 5, 1).until(EC.presence_of_element_located(('id', 'kw')))

