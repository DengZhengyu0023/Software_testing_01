"""
    注册页面
"""
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

# 已有账号，去登陆
go_login = By.XPATH, "//*[@text='已有账号，去登录']"

class PageRegister(BaseAction):
    # 点击 已有账号，去登录
    def page_register_go_login(self):
        self.base_click(go_login)