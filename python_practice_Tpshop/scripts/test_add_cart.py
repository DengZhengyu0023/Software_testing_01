"""
    测试添加购物车
"""
# 导包
import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page import Page
from base.auto_login import AutoLogin
from tool.get_logger import GetLogger

# 获得日志器
#log = GetLogger().get_logger()

# TestAddCart类 继承unittest类
class TestAddCart(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 实例化浏览器对象
        cls.driver = GetDriver.get_driver()
        # 实例化Page接口类
        cls.add_cart = Page(cls.driver)
        # 判断登录情况
        AutoLogin().auto_login()

    # 关闭资源
    @classmethod
    def tearDownClass(cls):
        # 暂停
        sleep(2)
        # 关闭浏览器
        GetDriver.quit_driver()

    def test_add_cart(self):
        # 点击我的购物车
        self.add_cart.page_my_shop.page_my_shop_click_my_cart()
        # 判断是否有 去购物 按钮
        print(self.add_cart.page_cart.page_cart_shopping_is_exist())
        if not self.add_cart.page_cart.page_cart_shopping_is_exist():
            # 点击 全选
            self.add_cart.page_cart.page_cart_click_select_all()
            # 删除选中商品
            self.add_cart.page_cart.page_cart_click_del_selected_goods()
            # 点击删除提示框 删除
            self.add_cart.page_cart.page_cart_click_del_info_delete()
        # 点击 去购物
        self.add_cart.page_cart.page_cart_click_shopping()
        # 搜索框输入小米
        self.add_cart.page_tpshop.page_tpshop_input_search("小米")
        # 点击 搜索
        self.add_cart.page_tpshop.page_tpshop_click_search()
        # 点击加入购物车
        sleep(2)
        self.add_cart.page_goods.page_click_goods_add_cart()
        # 切换网页目录
        sleep(2)
        self.add_cart.page_goods.page_cart_switch_to_result()
        # 获取添加结果提示
        sleep(2)
        result = self.add_cart.page_goods.page_get_add_cart_result()
        print(result)
        # 断言
        try:
            self.assertEqual(result, "添加成功")
            # 点击 去购物车结算
            self.add_cart.page_goods.page_click_pay_to_cart()
        except Exception:
            sleep(2)
            # 截图
            self.add_cart.page_goods.base_get_image()