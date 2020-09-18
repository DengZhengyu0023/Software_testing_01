"""
    page接口
"""
from page.page_Tpshop import PageTpshop
from page.page_cart import PageCart
from page.page_fill_order_info import PageFillOrderInfo
from page.page_goods import PageGoods
from page.page_login import PageLogin
from page.page_order_pay import PageOrderPay
from page.page_pay import PagePay
from page.page_register import PageRegister
from page.page_my_shop import PageMyShop


class Page:

    def __init__(self, driver):
        self.driver = driver

    # Tpshop首页
    @property
    def page_tpshop(self):
        return PageTpshop(self.driver)

    # Tpshop登录页
    @property
    def page_login(self):
        return PageLogin(self.driver)

    # Tpshop注册页面
    @property
    def page_register(self):
        return PageRegister(self.driver)

    @property
    def page_my_shop(self):
        return PageMyShop(self.driver)

    @property
    def page_cart(self):
        return PageCart(self.driver)

    @property
    def page_goods(self):
        return PageGoods(self.driver)

    @property
    def page_fill_order_info(self):
        return PageFillOrderInfo(self.driver)

    @property
    def page_pay(self):
        return PagePay(self.driver)

    @property
    def page_order_pay(self):
        return PageOrderPay(self.driver)