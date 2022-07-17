# -*- coding = utf-8 -*-
# @Time : 2022/7/15 14:56
# @Author : 李兆堃
# @File : start.py
# @Software : PyCharm
import time

from findElement import Find


class Start:    # 必要的前置操作
    def __init__(self, browser, website, loginurl, userName: str, passWord: str, find):
        self.browser = browser
        self.website = website
        self.userName = userName
        self.passWord = passWord
        self.find = find
        self.url = loginurl
        pass

    def operate(self):
        self.openPage()
        self.login()

    def openPage(self):     # 打开网页
        self.browser.get(self.url)
        pass

    def login(self):        # 登录
        if self.website == 'JD':
            self.find.switchJDLogin().click()
        self.find.userNameTextArea().clear()
        self.find.passWordTextArea().clear()
        self.find.userNameTextArea().send_keys(self.userName)
        self.find.passWordTextArea().send_keys(self.passWord)
        self.find.clickLoginButton().click()
        time.sleep(2.5)
        pass    # 处理验证码
        pass
