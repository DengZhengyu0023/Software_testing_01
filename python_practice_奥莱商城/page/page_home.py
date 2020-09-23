"""
    首页
"""
# 导包
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

# 我
me = By.ID, "com.yunmall.lc:id/tab_me"
# 关闭更新
close = By.ID, "com.yunmall.lc:id/img_close"

class PageHome(BaseAction):
    # 点击  我
    def page_home_click_me(self):
        self.base_click(me)

    # 关闭 更新
    def page_home_click_close(self):
        self.base_click(close)

    # 自动登录
    def page_home_login_if_not(self, page, username="itheima_test", password="itheima"):
        # 点击 关闭更新
        page.page_home.page_home_click_close()
        #点击 我
        self.base_click(me)
        # 判断是否登录
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        else:
            # 点击 已有账号，去登录
            page.page_register.page_register_go_login()
            # 输入 用户名
            page.page_login.page_login_input_username(username)
            # 输入 密码
            page.page_login.page_login_input_password(password)
            # 点击 登录 按钮
            page.page_login.page_login_click_login()