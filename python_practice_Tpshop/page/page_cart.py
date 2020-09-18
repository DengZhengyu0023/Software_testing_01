"""
    Tpshop商城购物车页面
"""
# 导包
from selenium.webdriver.common.by import By
from base.base import Base


# 去购物按钮
shopping = By.PARTIAL_LINK_TEXT, "去购物"
# 全选 框
select_all = By.CSS_SELECTOR, ".cart-checkbox > .checkall-true"
# 删除 选中商品
selected_goods = By.CSS_SELECTOR, ".deleteAll"
# 删除提示框 删除
del_info_delete = By.CSS_SELECTOR, ".select-remove"
# 去结算
go_pay = By.PARTIAL_LINK_TEXT, "去结算"


# PageCart类
class PageCart(Base):
    # 判断 去购物 按钮是否存在
    def page_cart_shopping_is_exist(self):
        return self.base_element_is_exist(shopping)

    # 点击 去购物 按钮
    def page_cart_click_shopping(self):
        self.base_click(shopping)

    # 点击 全选 框
    def page_cart_click_select_all(self):
        #print(self.base_find_element(select_all).is_selected())
        if not self.base_find_element(select_all):
            self.base_click(select_all)

    # 点击 删除选中
    def page_cart_click_del_selected_goods(self):
        self.base_click(selected_goods)

    # 点击删除提示框 删除
    def page_cart_click_del_info_delete(self):
        self.base_click(del_info_delete)

    # 点击 去结算
    def page_cart_click_go_pay(self):
        self.base_click(go_pay)