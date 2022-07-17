# -*- coding = utf-8 -*-
# @Time : 2022/7/15 22:01
# @Author : 李兆堃
# @File : inputData.py
# @Software : PyCharm
import re
import time

import urllib.request, urllib.error


class Input:
    def __init__(self):
        self.website = None
        self.number = None
        pass

    def getAll(self):
        return self.getWebSite(), self.getNumber(), self.getLoginUrl(), self.getPanicTime()

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

    def getLoginUrl(self):  # 获取网址
        if self.website == 'JD':
            return 'https://passport.jd.com/uc/login'
        else:
            return 'https://login.taobao.com/member/login.jhtml'

    def getPanicTime(self):
        return input("\n请输入要抢购时间，时间格式：时:分:秒")


def getBeijinTime():
    """
　　 获取北京时间
    """

    findHour = re.compile('nhrs=(\d*)')
    findMinute = re.compile('nmin=(\d*)')
    findSecond = re.compile('nsec=(\d*)')
    head = {
        'Cookie': r'__51uvsct__1vdgvIYlGPwXNNU6=1; __51vcke__1vdgvIYlGPwXNNU6=56e59ebb-c43e-572b-95c2-92494ee28498; __51vuft__1vdgvIYlGPwXNNU6=1658064221869; __gads=ID=5c36285f4baaee11-22c410f738d500d6:T=1658064240:RT=1658064240:S=ALNI_MbsMucFguYn_9eE7S-L-iD0-zmN3w; __gpi=UID=000007ca4a02cda2:T=1658064240:RT=1658064240:S=ALNI_MbHPIv5CnLoyDn-00FldOfw1LOj-A; ASPSESSIONIDSECATSBC=PBHKLNEBIAJDHGEJPEMLKCJA; __vtins__1vdgvIYlGPwXNNU6={"sid": "871705ec-6f2f-5a59-bc87-1e6e0bcd8411", "vd": 4, "stt": 1341335, "dr": 1213095, "expires": 1658067363198, "ct": 1658065563198}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    url = r'https://www.beijing-time.org/t/time.asp'
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        res = response.read().decode('utf-8')
        sec = int(re.findall(findSecond, res)[0])
        if sec >= 60:
            sec -= 60

        netTime = re.findall(findHour, res)[0] + ':' + re.findall(findMinute, res)[0] + ':' + str(sec)  # 返回str
        return netTime
    except urllib.error as e:
        if hasattr(e, 'code'):  # 判断e中是否存在code值
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
