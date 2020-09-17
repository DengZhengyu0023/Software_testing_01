"""
    手机注册测试
"""
# 导包
import unittest

from time import sleep
from parameterized import parameterized
from base.get_driver import GetDriver
from page.page import Page
from tool.get_data import GetData

data = GetData().data_register()

# 测试类test_register 继承unittest
class TestRegister(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 实例化浏览器对象
        cls.driver = GetDriver.get_driver()
        # 实例化Page接口类
        cls.register = Page(cls.driver)
        # 点击注册链接
        cls.register.page_tpshop.page_tpshop_click_register_link()

    # tearDown
    @classmethod
    def tearDownClass(cls):
        # 暂停
        sleep(2)
        # 关闭浏览器0
        GetDriver().quit_driver()

    # 测试用例
    @parameterized.expand(data)
    def test_register(self, number, verify_code, set_password, sure_password,
                      referrer_phone_number, except_result, status):
        # 点击手机注册
        self.register.page_register.page_register_click_phone_register()
        # 输入手机号
        sleep(1)
        self.register.page_register.page_register_input_phone_number(number)
        # 输入验证码
        sleep(1)
        self.register.page_register.page_register_input_verify_code(verify_code)
        # 输入设置密码
        sleep(1)
        self.register.page_register.page_register_input_set_password(set_password)
        # 输入确认密码
        sleep(1)
        self.register.page_register.page_register_input_sure_password(sure_password)
        # 输入推荐人手机号
        sleep(1)
        if referrer_phone_number is not None:
            self.register.page_register.page_register_input_referrer_phone_number(referrer_phone_number)

        # 点击 同意协议并注册 按钮
        self.register.page_register.page_register_click_agree_button()

        # 判断测试用例是否正向
            # 正向用例
        if status is True:
            try:
                # 断言是否注册成功
                self.assertTrue(self.register.page_register.page_if_login_success())
            except:
                # 暂停
                sleep(0.5)
                # 注册失败 截图
                self.register.page_register.base_get_image()
            # 点击安全退出
            self.register.page_register.page_register_click_loginout()
            # 点击注册链接
            self.register.page_tpshop.page_tpshop_click_register_link()
        else:
            # 获取注册提示信息
            register_msg = self.register.page_register.page_register_get_register_info()
            print(register_msg)
            try:
                # 断言提示信息
                self.assertEqual(register_msg, except_result)
            except:
                # 暂停
                sleep(0.5)
                # 截图
                self.register.page_register.base_get_image()
            # 点击信息确认按钮
            self.register.page_register.page_register_click_info_ok_button()