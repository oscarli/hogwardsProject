"""
@author: Oscar
@time: 2021/4/15 17:48
@file: test_selenium.py
@desc: 
"""
import time

import selenium
from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    assert True
    time.sleep(4)



