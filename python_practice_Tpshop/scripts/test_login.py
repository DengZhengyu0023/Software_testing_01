"""
    测试登录
"""
# 导包
import unittest

from parameterized import parameterized
from base.get_driver import GetDriver
from page.page import Page
from time import sleep

from tool.get_data import GetData

data = GetData().data_login()

# 测试类 继承unittest
class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 实例化浏览器对象
        cls.driver = GetDriver().get_driver()
        # 实例化page接口类
        cls.login = Page(cls.driver)
        # 点击登录链接
        cls.login.page_tpshop.page_tpshop_click_login_link()

    # teardown
    @classmethod
    def tearDownClass(cls):
        sleep(2)
        # 关闭浏览器对象
        GetDriver().quit_driver()

    # 测试用例
    @parameterized.expand(data)
    def test_login(self, username, password, verify_code, except_result, status):
        # 业务执行
        # 输入用户名
        self.login.page_login.page_input_username(username)
        # 输入密码
        self.login.page_login.page_input_password(password)
        # 输入验证码
        self.login.page_login.page_input_verify_code(verify_code)
        # 点击登录按钮
        self.login.page_login.page_click_login_button()
        # 判断测试用例是否正向
        if status == True:
            # 正向用例
            try:
                # 断言是否登录成功
                self.assertTrue(self.login.page_login.page_if_login_success())
            except Exception as e:
                #暂停
                sleep(0.5)
                # 登录失败 截图
                self.login.page_login.base_get_image()
            # 点击安全退出
            self.login.page_login.page_click_logout_link()
            # 点击登录链接
            self.login.page_tpshop.page_tpshop_click_login_link()
        else:
            # 反向用例
            # 获取提示信息
            msg = self.login.page_login.page_get_longin_info()
            #print(msg)
            try:
                # 断言提示信息
                self.assertEqual(msg, except_result)
            except Exception as e:
                # 暂停
                sleep(0.5)
                # 截图
                self.login.page_login.base_get_image()
            # 点击提示信息确认按钮
            self.login.page_login.page_click_login_info_ok_button()