#导包
import time

from tool.get_logger import GetLogger
from selenium.webdriver.support.wait import WebDriverWait

# 获得日志器
log = GetLogger().get_logger()

# Base类
class Base:
    # 初始化
    def __init__(self, driver):
        log.info("[base]: 正在获得初始化driver对象: {}".format(driver))
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info("[base]: 正在定位 {} 元素，定位超时时间为 {}".format(loc, timeout))
        element = WebDriverWait(self.driver,
                                timeout=timeout,
                                poll_frequency=poll).until(lambda x: x.find_element(*loc))
        return element

    # 点击
    def base_click(self, loc):
        log.info("[base]: 正在对 {} 元素进行点击".format(loc))
        self.base_find_element(loc).click()

    # 输入
    def base_input(self, loc, values):
        # 获得元素
        el = self.base_find_element(loc)
        # 清空
        log.info("[base]: 正在对 {} 元素清空".format(loc))
        el.clear()
        # 输入
        log.info("[base]: 正在对 {} 元素输入 {}".format(loc, values))
        el.send_keys(values)

    # 截图
    def base_get_image(self):
        log.info("[base]: 正在截图")
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    # 获取提示信息
    def base_get_text(self, loc):
        log.info("[base]: 正在获取 {} 文本信息".format(loc))
        return self.base_find_element(loc).text

    # 判断某元素是否存在
    def base_element_is_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=3)
            log.info("[base]: 定位 {} 元素成功".format(loc))
            return True
        except:
            log.info("[base]: 定位 {} 元素失败".format(loc))
            return False

    # 切换 网页目录
    def base_switch_frame(self, frame_name):
        log.info("切换网页目录到 {}".format(frame_name))
        self.driver.switch_to.frame(frame_name)

    # 切换回 默然网页目录
    def base_switch_dafult_frame(self):
        log.info("切换回默认网页目录")
        self.driver.switch_to.default_content()

    # 打印handle
    def base_handles(self):
        print(self.driver.window_handles)

    # 获得指定title页面所有的handles
    def base_get_title_handle(self, title):
        # 获得当前所有handles
        log.info("正在遍历handles: {}".format(self.driver.window_handles))
        for handle in self.driver.window_handles:
            # 切换handle
            log.info("切换到窗口: {}".format(handle))
            self.driver.switch_to.window(handle)
            # 判断当前页面是否为目标页面
            log.info("判断当前页面页面title: {} 是否等于指定的title: {}".format(
                                                    self.driver.title, title))
            if self.driver.title == title:
                # 返回handle
                log.info("title相同条件成立,返回当前handle {}".format(handle))
                return handle

    # 切换窗口
    def base_switch_to_window(self, title):
        log.info("正在切换tltle为 {} 的窗口".format(title))
        self.driver.switch_to.window(self.base_get_title_handle(title))