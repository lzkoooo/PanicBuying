# -*- coding = utf-8 -*-
# @Time : 2022/7/15 16:27
# @Author : 李兆堃
# @File : operation.py
# @Software : PyCharm
import time

import driver
from findElement import Find
from inputData import getBeijinTime
from start import Start


class Operate:
    def __init__(self, browser, num, website, loginUrl, username, password, panicTime):
        self.browser = browser
        self.num = num
        self.website = website
        self.loginUrl = loginUrl
        self.username = username
        self.password = password
        self.find = None
        self.website = website
        self.panicTime = panicTime
        pass

    def operate(self):
        self.getFindElement()
        st = Start(self.browser, self.website, self.loginUrl, self.username, self.password, self.find)
        st.operate()  # 登录已完成
        self.prepare()  # 准备操作
        self.panic()

    def getFindElement(self):
        self.find = Find(self.browser, self.website)

    def prepare(self):
        self.find.enterShoppingCart().click()
        time.sleep(3)
        if self.num == '全选':
            self.find.selectAll().click()
        else:
            # 清除选项
            self.find.selectAll().click()
            time.sleep(0.5)
            self.find.selectAll().click()
            time.sleep(0.5)
            # 正式操作
            elements = self.find.select(int(self.num))
            for i in range(int(self.num)):
                self.find.drag(elements[i])
                time.sleep(0.7)
                elements[i].click()

        pass

    def panic(self):
        while True:
            if getBeijinTime() >= self.panicTime:
                break

        while self.browser.current_url[8] == 'c':
            self.find.settleAccounts().click()
            time.sleep(0.3)
        self.find.submit().click()
