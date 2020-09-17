#导包
import time

from base.get_driver import GetDriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

# Base类
class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        element = WebDriverWait(self.driver,
                                timeout=timeout,
                                poll_frequency=poll).until(lambda x: x.find_element(*loc))
        return element

    # 点击
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入
    def base_input(self, loc, values):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(values)

    # 截图
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    # 获取提示信息
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 判断某元素是否存在
    def base_element_is_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=3)
            return True
        except:
            return False

    # 切换 网页陌路
    def base_switch_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    # 切换回 默然网页目录
    def base_switch_dafult_frame(self):
        self.driver.switch_to.default_content()

    #
    def base_handles(self):
        print(self.driver.window_handles)