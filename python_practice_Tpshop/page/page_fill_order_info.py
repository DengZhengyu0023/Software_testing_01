"""
    填写核对订单信息
"""
# 导包
from selenium.webdriver.common.by import By

from base.base import Base
# PageFillOrderInfo
submit_order = By.CSS_SELECTOR, ".checkout-submit"


class PageFillOrderInfo(Base):
    # 点击 提交订单
    def page_fill_order_info_submit_order(self):
        self.base_click(submit_order)