"""
    支付页面
"""
from selenium.webdriver.common.by import By

from base.base import Base

# 提交订单结果
order_result = By.CSS_SELECTOR, ".erhuh>h3"

class PagePay(Base):
    # 获取提交订单结果
    def page_pay_get_order_result(self):
        return self.base_get_text(order_result)