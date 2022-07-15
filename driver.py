# -*- coding = utf-8 -*-
# @Time : 2022/7/15 14:29
# @Author : 李兆堃
# @File : driver.py
# @Software : PyCharm

from selenium import webdriver


class Browser:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # 关闭自动测试状态显示 // 会导致浏览器报：请停用开发者模式
        # window.navigator.webdriver还是返回True,当返回undefined时应该才可行。
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # 关闭开发者模式
        chrome_options.add_experimental_option("useAutomationExtension", False)
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def getDriver(self):
        return self.browser

    def quit(self):
        self.browser.quit()
