# -*- coding = utf-8 -*-
# @Time : 2022/7/15 22:01
# @Author : 李兆堃
# @File : inputData.py
# @Software : PyCharm

class Input:
    def __init__(self):
        self.website = None
        self.number = None
        pass

    def getAll(self):
        return self.getWebSite(), self.getNumber(), self.getLoginUrl()

    def getWebSite(self):
        website = input("\n请输入要访问的网站，淘宝or京东")
        try:
            if website == '京东':
                self.website = 'JD'
            elif website == '淘宝':
                self.website = 'TB'
            else:
                raise ValueError
            return self.website
        except ValueError as e:
            print('输入错误！！')
            self.getWebSite()
            pass

    def getNumber(self):
        self.number = input("\n请输入要抢购的数量，全选or输入数量")
        try:
            if self.number != '全选' and int(self.number) not in range(1, 50):
                raise ValueError
        except ValueError:
            print('数量输入错误')
            self.getNumber()
        return self.number

    def getLoginUrl(self):       # 获取网址
        if self.website == 'JD':
            return 'https://passport.jd.com/uc/login'
        else:
            return 'https://login.taobao.com/member/login.jhtml'


