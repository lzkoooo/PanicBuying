# -*- coding = utf-8 -*-
# @Time : 2022/7/15 14:27
# @Author : 李兆堃
# @File : main.py
# @Software : PyCharm

from driver import Browser
from operation import Operate
from inputData import Input


def main():
    site, num, url = Input().getAll()
    chrome = Browser().getDriver()
    if site == 'JD':
        username = '15127026818'
        password = '15127026818lzk-'
    else:
        username = 'tb05090174'
        password = '15127026818lzk-'
    op = Operate(chrome, num, site, url, username, password)
    op.operate()
    chrome.quit()
    pass


if __name__ == "__main__":
    main()
