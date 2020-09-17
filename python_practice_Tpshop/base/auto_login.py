"""
    如果没有登录 自动登录
"""
# 导包
from selenium.webdriver.common.by import By
from base.get_driver import GetDriver
from page.page import Page



# 登录链接
login_linK = By.PARTIAL_LINK_TEXT, "登录"

class AutoLogin:
    # 初始化
    def __init__(self):
        # 实例化浏览器对象
        self.driver = GetDriver.get_driver()
        # 实例化Page类
        self.page_auto_login = Page(self.driver)

    # 进行登录步骤
    def auto_login(self):
        # 判断登录链接是否存在 不存在则认为没有登录
        if not self.page_auto_login.page_tpshop.base_element_is_exist(login_linK):
            return
        # 点击登录链接
        self.page_auto_login.page_login.base_click(login_linK)
        # 输入用户名
        self.page_auto_login.page_login.page_input_username("13444444444")
        # 输入密码
        self.page_auto_login.page_login.page_input_password("123456")
        # 输入验证码
        verify_code = input("请输入验证码：")
        self.page_auto_login.page_login.page_input_verify_code(verify_code)
        # 点击登录按钮
        self.page_auto_login.page_login.page_click_login_button()




if __name__ == "__main__":
    a = AutoLogin()
    a.auto_login()