# -*- coding = utf-8 -*-
# @Time : 2022/7/15 15:21
# @Author : 李兆堃
# @File : findElement.py
# @Software : PyCharm

from selenium.webdriver.common.by import By


class Find:
    def __init__(self, browser, website):
        self.browser = browser
        self.website = website

    # def enterLoginPage(self, website: str):
    #     if website == 'JD':
    #         return self.browser.find_element()
    #     else:
    #         return self.browser.find_element()

    def userNameTextArea(self):
        if self.website == 'JD':
            return self.browser.find_element(By.XPATH, r'//*[@id="loginname"]')
        else:
            return self.browser.find_element(By.XPATH, r'//*[@id="fm-login-id"]')

    def passWordTextArea(self):
        if self.website == 'JD':
            return self.browser.find_element(By.XPATH, r'//*[@id="nloginpwd"]')
        else:
            return self.browser.find_element(By.XPATH, r'//*[@id="fm-login-password"]')

    def clickLoginButton(self,):
        if self.website == 'JD':
            return self.browser.find_element(By.CSS_SELECTOR, r'.login-btn')
        else:
            return self.browser.find_element(By.CSS_SELECTOR, r'button[class*="password-login"]')

    def enterShoppingCart(self):
        if self.website == 'JD':
            return self.browser.find_element(By.XPATH, r'//*[@id="settleup"]/div[1]/a')
        else:
            return self.browser.find_element(By.XPATH, r'//*[@id="J_MiniCart"]/div[1]/a')
        pass

    def selectAll(self):
        if self.website == 'JD':
            return self.browser.find_element(By.XPATH, r'//*[@id="cart-body"]/div[2]/div[50]/div/div[2]/div/div/div/div[2]/div[1]/div[1]')
        else:
            return self.browser.find_element(By.XPATH, r'//*[@id="J_SelectAll2"]')
        pass

    def select(self, number: int):
        if self.website == 'JD':
            return [self.browser.find_element(By.XPATH, r'//*[@class="w"][0]/div[%d]/div[1]/div/div[1]/div[0]/div[0]/div/input' % i) for i in range(3, number +2)]
        else:
            return [self.browser.find_element(By.XPATH, r'//*[@id="J_OrderList"]/div[%d]//ul/li[1]//label' % i) for i in range(number - 1)]
        pass

    def settleAccounts(self):
        return self.browser.find_element(By.XPATH, r'//[@class="btn-area"]')
        pass

    def submit(self):
        if self.website == 'JD':
            return self.browser.find_element(By.XPATH, r'//[@type="submit"]')
            pass
        else:
            return self.browser.find_element(By.XPATH, r'//[@title="提交订单"]')
