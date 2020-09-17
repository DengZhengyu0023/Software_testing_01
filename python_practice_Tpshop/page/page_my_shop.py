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

# PageMyShop类
class PageMyShop(Base):
    # 返回首页
    def page_my_shop_click_go_back_homepage(self):
        self.base_click(go_back_homepage)

    # 我的购物车
    def page_my_shop_click_my_cart(self):
        self.base_click(my_cart)