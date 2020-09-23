"""
    page接口
"""
# 导包
from page.page_home import PageHome
from page.page_login import PageLogin
from page.page_my import PageMy
from page.page_register import PageRegister


class Page:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 首页
    @property
    def page_home(self):
        return PageHome(self.driver)

    # 注册页面
    @property
    def page_register(self):
        return PageRegister(self.driver)

    # 登录页面
    @property
    def page_login(self):
        return PageLogin(self.driver)

    # 我的 页面
    @property
    def page_my(self):
        return PageMy(self.driver)