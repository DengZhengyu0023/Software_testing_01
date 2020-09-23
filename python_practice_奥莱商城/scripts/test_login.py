from time import sleep

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver(False)
        self.page_login = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        # 关闭 更新
        self.page_login.page_home.page_home_click_close()
        # 点击 我
        self.page_login.page_home.page_home_click_me()
        # 点击 已有账号，去登陆
        self.page_login.page_register.page_register_go_login()
        # 输入 用户名
        self.page_login.page_login.page_login_input_username(username)
        # 输入 密码
        self.page_login.page_login.page_login_input_password(password)
        # 点击 登录 按钮
        self.page_login.page_login.page_login_click_login()

        # 判断登录是否正确
        if toast is None:
            # 断言
            assert self.page_login.page_my.page_my_get_nick_name() == "itheima_test", "登录后的用户名与输入的用户名不一致"
        else:
            assert self.page_login.page_login.base_is_toast_exist(toast)
