"""
    Tpshop商城首页
"""
# 导包
from selenium.webdriver.common.by import By
from base.base import Base

# 登录链接
login_link = By.LINK_TEXT, "登录"
# 注册链接
register_link = By.LINK_TEXT, "注册"
# 首页logo链接
logo_link = By.CSS_SELECTOR, ".ecsc-logo > img:nth-child(1)"
# 我的购物车
my_cart = By.CSS_SELECTOR, ".share-shopcar-index"
# 搜索框
search = By.CSS_SELECTOR, "[name='q']"
# 搜索按钮
search_button = By.CSS_SELECTOR, ".ecsc-search-button"



# Page类
class PageTpshop(Base):
    # 点击首页loge
    def page_tpshop_click_logo_link(self):
        self.base_click(logo_link)

    # 点击登录链接
    def page_tpshop_click_login_link(self):
        self.base_click(login_link)

    # 点击注册链接
    def page_tpshop_click_register_link(self):
        self.base_click(register_link)

    # 点击 我的购物车
    def page_tpshop_click_my_cart(self):
        self.base_click(my_cart)

    # 搜索框输入内容
    def page_tpshop_input_search(self, values):
        self.base_input(search, values)

    # 点击 搜索 按钮
    def page_tpshop_click_search(self):
        self.base_click(search_button)