"""
    订单支付页面
"""
from selenium.webdriver.common.by import By
from base.base import Base

# 货到付款
on_delivery = By.CSS_SELECTOR, "[src='/plugins/payment/cod/logo.jpg']"
#确认支付
sure_pay = By.CSS_SELECTOR, ".button-confirm-payment"

class PageOrderPay(Base):
    # 点击货到付款
    def page_order_pay_click_on_delivery(self):
        self.base_click(on_delivery)

    #点击确认支付
    def page_order_pay_click_sure_pay(self):
        self.base_click(sure_pay)