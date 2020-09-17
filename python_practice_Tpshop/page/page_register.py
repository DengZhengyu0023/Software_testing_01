"""
    Tpshop商城注册页面
"""

# 导包
from selenium.webdriver.common.by import By
from base.base import Base

# 手机注册链接
phone_register_link = By.PARTIAL_LINK_TEXT, "手机注册"
# 输入手机号
input_phone_number = By.CSS_SELECTOR, "#username"
# 输入验证码
input_verify_code = By.CSS_SELECTOR, ".J_imgcode"
# 输入设置密码
input_set_password = By.CSS_SELECTOR, ".J_password"
# 输入确认密码
input_sure_password = By.CSS_SELECTOR, ".J_password2"
# 输入推荐人手机号
input_referrer_phone_number = By.CSS_SELECTOR, "[name='invite']"
# 安全退出链接
logout_link = By.PARTIAL_LINK_TEXT, "安全退出"
# 注册提示信息
register_info = By.CSS_SELECTOR, ".layui-layer-content"
# 点击注册提示信息确认按钮
info_ok_button = By.PARTIAL_LINK_TEXT, "确定"
# 点击 同意协议并注册 按钮
agree_button = By.CSS_SELECTOR, ".J_btn_agree"

# PageRegister类
class PageRegister(Base):
    # 点击手机注册
    def page_register_click_phone_register(self):
        self.base_click(phone_register_link)

    # 输入手机号
    def page_register_input_phone_number(self, number):
        self.base_input(input_phone_number, number)

    # 输入验证码
    def page_register_input_verify_code(self, verify_code):
        self.base_input(input_verify_code, verify_code)

    # 输入设置密码
    def page_register_input_set_password(self, set_password):
        self.base_input(input_set_password, set_password)

    # 输入确认密码
    def page_register_input_sure_password(self, sure_password):
        self.base_input(input_sure_password, sure_password)

    # 输入推荐人手机号
    def page_register_input_referrer_phone_number(self, referrer_phone_number):
        self.base_input(input_referrer_phone_number, referrer_phone_number)

    # 判断注册是否成功
    def page_register_if_register_success(self):
        return self.base_element_is_exist(logout_link)

    # 点击安全退出
    def page_register_click_loginout(self):
        self.base_click(logout_link)

    # 获取注册提示信息
    def page_register_get_register_info(self):
        return self.base_get_text(register_info)

    # 点击注册提示信息确认按钮
    def page_register_click_info_ok_button(self):
        self.base_click(info_ok_button)

    # 点击 同意协议并注册 按钮
    def page_register_click_agree_button(self):
        self.base_click(agree_button)