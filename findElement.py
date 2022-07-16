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

    def switchJDLogin(self):
        return self.browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/a')

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
            self.browser.switch_to.window(self.browser.window_handles[1])
            return self.browser.find_element(By.XPATH, r'//*[@name="select-all"]')
        else:
            return self.browser.find_element(By.XPATH, r'//label[@for="J_SelectAllCbx1"]')
        pass

    def select(self, number: int):
        if self.website == 'JD':
            return self.browser.find_elements(By.XPATH, '//*[@name="checkItem"]')[: number]
        else:
            return self.browser.find_elements(By.XPATH, r'//*[@class="order-content"]//*[@class="cart-checkbox"]/label')[: number]
        pass

    def settleAccounts(self):
        if self.website == 'JD':
            return self.browser.find_element(By.XPATH, r'//*[@class="common-submit-btn"]/a')
        else:
            return self.browser.find_element(By.CSS_SELECTOR, r'#J_SmallSubmit')
        pass

    def submit(self):
        if self.website == 'JD':
            return self.browser.find_element(By.XPATH, r'//[@type="submit"]')
            pass
        else:
            return self.browser.find_element(By.XPATH, r'//[@title="提交订单"]')

    def drag(self, ele):
        # js = "var q=document.getElementById('J_GoToTop').scrollTop=" + str(num * 100)
        # self.browser.execute_script(js)
        self.browser.execute_script("arguments[0].scrollIntoView();", ele)
