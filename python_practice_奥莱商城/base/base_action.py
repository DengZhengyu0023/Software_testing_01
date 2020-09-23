from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def base_find_elements(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def base_click(self, feature):
        self.base_find_element(feature).click()

    def base_input(self, feature, text):
        self.base_find_element(feature).send_keys(text)

    def base_get_text(self, feature):
        return self.base_find_element(feature).text

    def base_is_toast_exist(self, message):
        """
        判断toast是否存在
        :param message:部分内容
        :return:是否存在
        """
        message_xpath = By.XPATH, "//*[contains(@text, '%s')]" % message
        try:
            self.base_find_element(message_xpath)
            return True
        except TimeoutException:
            return False

    def base_get_toast_text(self, message):
        """
        获取toast
        :param message:toast部分内容
        :return:toast全部内容
        """
        if self.base_is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@test, '%s')]" % message
            return self.base_find_element(message_xpath).text
        else:
            raise Exception("toast未出现")

    def base_scroll_page(self, direction="up"):
        """
        滑动屏幕
        :param direction:滑动方向
            'up': 从上往上
            'down': 从上往下
            'left': 从右往左
            'right': 从左往右
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

        mid_x = width // 2
        mid_y = height // 2

        top_y = height // 4
        bottom_y = height // 4 * 3

        left_x = width // 4
        right_x = width // 4 * 3

        param_dict = {"up": (mid_x, bottom_y, mid_x, top_y),
                      "down": (mid_x, top_y, mid_x, bottom_y),
                      "left": (right_x, mid_y, left_x, mid_y),
                      "right": (left_x, mid_y, right_x, mid_y)}
        if direction not in param_dict.keys():
            raise Exception("请检查参数： up/dowm/left/right")
        self.driver.swipe(*param_dict[direction], 3000)

    def base_find_element_with_scroll(self, feature, direction="up"):
        """
        滑动屏幕找元素
        :param direction:滑动方向
            'up': 从上往上
            'down': 从上往下
            'left': 从右往左
            'right': 从左往右
        :return:
        """
        page_source = ""

        while True:
            try:
                return self.base_find_element(feature)

            except Exception:
                self.base_scroll_page(direction)

                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source