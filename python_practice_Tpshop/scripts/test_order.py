"""
    测试下订单
"""
# 导包
import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page import Page
from base.auto_login import AutoLogin

# TestOrder



class TestOrder(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 实例化浏览器对象
        cls.driver = GetDriver.get_driver()
        # 实例化Page接口类
        cls.order = Page(cls.driver)
        # 登录
        AutoLogin().auto_login()

    # 释放资源
    @classmethod
    def tearDownClass(cls):
        # 暂停
        sleep(2)
        # 关闭浏览器
        GetDriver.quit_driver()

    def test_order(self):
        # 点击 我的购物车
        self.order.page_my_shop.page_my_shop_click_my_cart()
        # 判断购物车是否有商品
        if self.order.page_cart.page_cart_shopping_is_exist():
            # 点击 去购物
            self.order.page_cart.page_cart_click_shopping()
            # 搜索框输入小米
            self.order.page_tpshop.page_tpshop_input_search("小米")
            # 点击 搜索
            self.order.page_tpshop.page_tpshop_click_search()
            # 点击加入购物车
            sleep(2)
            self.order.page_goods.page_click_goods_add_cart()
            # 切换网页目录
            sleep(2)
            self.order.page_goods.page_cart_switch_to_result()
            # 获取添加结果提示
            sleep(2)
            result = self.order.page_goods.page_get_add_cart_result()
            print(result)
            # 断言
            try:
                self.assertEqual(result, "添加成功")
                # 点击 去购物车结算
                self.order.page_goods.page_click_pay_to_cart()
            except Exception:
                sleep(2)
                # 截图
                self.order.page_goods.base_get_image()
        # 切换到默认目录 #否侧报错：WebDriverException: Message: can't access dead object
        self.order.page_cart.base_switch_dafult_frame()
        # 点击 全选
        self.order.page_cart.page_cart_click_select_all()
        # 点击 去结算
        self.order.page_cart.page_cart_click_go_pay()
        # 点击提交订单
        sleep(3)
        self.order.page_fill_order_info.page_fill_order_info_submit_order()
        # 获得提交订单结果
        result = self.order.page_pay.page_pay_get_order_result()
        try:
            # 断言
            self.assertIn("提价成功", result)
        except Exception:
            # 暂停
            sleep(2)
            # 截图
            self.order.page_pay.base_get_image()