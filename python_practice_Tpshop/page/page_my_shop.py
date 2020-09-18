"""
    我的商城页面
"""
# 导包
from selenium.webdriver.common.by import By
from base.base import Base

# 返回首页
go_back_homepage = By.LINK_TEXT, "返回商城首页"
# 我的购物车
my_cart = By.CSS_SELECTOR, ".share-shopcar-index"
# 立即支付
pay_now = By.CSS_SELECTOR, ".ps_lj"
# 订单支付title
pay_title = "订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"

# PageMyShop类
class PageMyShop(Base):
    # 返回首页
    def page_my_shop_click_go_back_homepage(self):
        self.base_click(go_back_homepage)

    # 我的购物车
    def page_my_shop_click_my_cart(self):
        self.base_click(my_cart)

    # 判断是否有订单
    def page_my_shop_if_exist_order(self):
        return self.base_element_is_exist(pay_now)

    # 点击 立即支付
    def page_my_shop_click_pay_now(self):
        self.base_click(pay_now)

    # 切换到订单支付窗口
    def page_my_shop_switch_to_pay(self):
        self.base_switch_to_window(pay_title)