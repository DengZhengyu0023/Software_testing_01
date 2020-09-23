"""
    登录页面
"""
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 输入用户名
input_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 输入密码
input_password = By.ID, "com.yunmall.lc:id/logon_password_textview"
#登录
login = By.ID, "com.yunmall.lc:id/logon_button"

class PageLogin(BaseAction):

    # 输入用户名
    def page_login_input_username(self, username):
        self.base_input(input_username, username)

    # 输入密码
    def page_login_input_password(self, password):
        self.base_input(input_password, password)
        
    # 点击登录
    def page_login_click_login(self):
        self.base_click(login)