"""
    我的页面
"""
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 昵称
nick_name = By.ID, "com.yunmall.lc:id/tv_user_nikename"

class PageMy(BaseAction):

    # 获取 昵称
    def page_my_get_nick_name(self):
        return self.base_get_text(nick_name)