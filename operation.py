# -*- coding = utf-8 -*-
# @Time : 2022/7/15 16:27
# @Author : 李兆堃
# @File : operation.py
# @Software : PyCharm
import driver
from findElement import Find
from start import Start


class Operate:
    def __init__(self, browser, username, password):
        self.browser = browser
        self.username = username
        self.password = password
        self.find = None
        self.website = None
        pass

    def operate(self):
        self.getWebSite()
        self.getFindElement()
        st = Start(self.browser, self.website, self.username, self.password, self.find)
        st.operate()    # 登录已完成
        self.Go()       # 抢购操作

    def getWebSite(self):
        website = input("请输入要访问的网站，淘宝or京东")
        try:
            if website == '京东':
                self.website = 'JD'
            elif website == '淘宝':
                self.website = 'TB'
            else:
                raise ValueError
        except ValueError as e:
            print('输入错误！！')
            self.getWebSite()
            pass

    def getFindElement(self):
        self.find = Find(self.browser, self.website)

    def Go(self):
        
        pass
