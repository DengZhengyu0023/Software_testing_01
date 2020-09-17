"""
    商品页面
"""
#导包
from selenium.webdriver.common.by import By

from base.base import Base

# 加入购物车
add_cart = By.PARTIAL_LINK_TEXT, "加入购物车"
# 去购物车结算
pay_to_cart = By.PARTIAL_LINK_TEXT, "去购物车结算"
# 添加结果
add_cart_result = By.CSS_SELECTOR, ".conect-title>span"
# 添加结果网页目录
frame_name = By.CSS_SELECTOR, "#layui-layer-iframe1"

class PageGoods(Base):
    # 点击 加入购物车
    def page_click_goods_add_cart(self):
        self.base_click(add_cart)

    # 点击 去购物车结算
    def page_click_pay_to_cart(self):
        self.base_click(pay_to_cart)

    # 获取添加购物车结果
    def page_get_add_cart_result(self):
        return self.base_get_text(add_cart_result)

    # 切换 加入购物车 结果目录
    def page_cart_switch_to_result(self):
        element = self.base_find_element(frame_name)
        self.base_switch_frame(element)