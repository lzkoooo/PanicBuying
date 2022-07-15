# -*- coding = utf-8 -*-
# @Time : 2022/7/15 14:56
# @Author : 李兆堃
# @File : start.py
# @Software : PyCharm

from findElement import Find


class Start:    # 必要的前置操作
    def __init__(self, browser, website: str, userName: str, passWord: str, find):
        self.browser = browser
        self.website = website
        self.userName = userName
        self.passWord = passWord
        self.find = find
        self.url = None
        pass

    def operate(self):
        self.url = self.getUrl()
        self.openPage()
        self.login()

    def getUrl(self):       # 获取网址
        if self.website == 'JD':
            return 'https://passport.jd.com/uc/login'
        else:
            return 'https://login.taobao.com/member/login.jhtml'

    def openPage(self):     # 打开网页
        self.browser.get(self.url)
        pass

    def login(self):        # 登录
        self.find.userNameTextArea().send_keys(self.userName)
        self.find.passWordTextArea().send_keys(self.passWord)
        self.find.clickLoginButton().click()
        pass
