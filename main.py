# -*- coding = utf-8 -*-
# @Time : 2022/7/15 14:27
# @Author : 李兆堃
# @File : main.py
# @Software : PyCharm

from driver import Browser
from operation import Operate
from inputData import Input


def main():
    site, num, url, panicTime, username, password = Input().getAll()
    chrome = Browser().getDriver()
    op = Operate(chrome, num, site, url, username, password, panicTime)
    op.operate()
    chrome.quit()
    pass


if __name__ == "__main__":
    main()
