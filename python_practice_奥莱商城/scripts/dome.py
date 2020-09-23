# 导包
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 可以操作toast
desired_caps['automationName'] = 'Uiautomator2'
# # 是否重置应用:(True:不重置)
# desired_caps['noReset'] = no_reset

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def scroll_page(direction="up"):
    """
    滑动屏幕
    :param direction:滑动方向
        'up': 从上往上
        'down': 从上往下
        'left': 从右往左
        'right': 从左往右
    :return:
    """
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]

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
    driver.swipe(*param_dict[direction], 3000)

def find_element_with_scroll(feature, direction="up"):
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
            return driver.find_element(*feature)

        except Exception:
            scroll_page(direction)

            if driver.page_source == page_source:
                print("到底了")
                break
            page_source = driver.page_source

if __name__ == "__main__":
    find_element_with_scroll((By.XPATH, "//*[@text='关于平板电脑']")).click()
