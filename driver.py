# -*- coding = utf-8 -*-
# @Time : 2022/7/15 14:29
# @Author : 李兆堃
# @File : driver.py
# @Software : PyCharm
import os

from selenium import webdriver


class Browser:

    def __init__(self):
        executable_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = executable_path
        chrome_options = webdriver.ChromeOptions()
        # 关闭自动测试状态显示 // 会导致浏览器报：请停用开发者模式
        # window.navigator.webdriver还是返回True,当返回undefined时应该才可行。
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # 关闭开发者模式
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument("--user-data-dir=" + r"C:\Users\16240\AppData\Local\Google\Chrome\User Data")
        self.browser = webdriver.Chrome(executable_path, chrome_options=chrome_options)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def getDriver(self):
        return self.browser

    def quit(self):
        self.browser.quit()
