"""
    Tpshop商城登录页面
"""
# 导包
from selenium.webdriver.common.by import By
from base.base import Base

# 用户名
login_username = By.CSS_SELECTOR, "#username"
# 密码
login_password = By.CSS_SELECTOR, "#password"
# 验证码
login_verify_code = By.CSS_SELECTOR, "#verify_code"
# 登录按钮
login_button = By.CSS_SELECTOR, ".J-login-submit"
# 安全退出
logout_link = By.PARTIAL_LINK_TEXT, "安全退出"
# 登录提示信息
login_info = By.CSS_SELECTOR, ".layui-layer-content"
# 登录提示信息确认按钮
login_info_ok_button = By.CSS_SELECTOR, ".layui-layer-btn0"
# 立即注册链接
register_now_link = By.PARTIAL_LINK_TEXT, "立即注册"

# PageLogin类
class PageLogin(Base):

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(login_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(login_password, password)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        self.base_input(login_verify_code, verify_code)

    # 点击登录按钮
    def page_click_login_button(self):
        self.base_click(login_button)

    # 获取登录提示信息
    def page_get_longin_info(self):
        return self.base_get_text(login_info)

    # 点击登录提示信息确定按钮
    def page_click_login_info_ok_button(self):
        self.base_click(login_info_ok_button)

    # 点击安全退出
    def page_click_logout_link(self):
        self.base_click(logout_link)

    # 判断是否登录成功
    def page_if_login_success(self):
        return self.base_element_is_exist(logout_link)

    # 点击立即注册链接
    def page_click_register_now_link(self):
        self.base_click(register_now_link)
