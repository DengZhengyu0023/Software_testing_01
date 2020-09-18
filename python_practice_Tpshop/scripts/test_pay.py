# 导包
import unittest
from time import sleep

from base.auto_login import AutoLogin
from base.get_driver import GetDriver
from page.page import Page

# TestPay
class TestPay(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 实例化浏览器对象
        cls.driver = GetDriver.get_driver()
        # 实例化Page接口类
        cls.pay = Page(cls.driver)
        # 登录
        AutoLogin().auto_login()

    # 释放资源
    @classmethod
    def tearDownClass(cls):
        # 暂停
        sleep(2)
        # 关闭浏览器
        GetDriver.quit_driver()

    # 测试用例
    def test_pay(self):
        # 判断是否有订单
        if not self.pay.page_my_shop.page_my_shop_if_exist_order():
            # 下订单
            pass
        # 点击 立即支付
        self.pay.page_my_shop.page_my_shop_click_pay_now()
        # 切换到 订单支付窗口
        sleep(3)
        self.pay.page_my_shop.page_my_shop_switch_to_pay()
        # 点击货到支付
        self.pay.page_order_pay.page_order_pay_click_on_delivery()
        # 点击确认支付
        self.pay.page_order_pay.page_order_pay_click_sure_pay()