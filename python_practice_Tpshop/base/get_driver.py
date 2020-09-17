# 导包
from selenium import webdriver

url = r"http://localhost"

class GetDriver():

    # driver变量
    driver = None

    # 打开浏览器
    @classmethod
    def get_driver(cls):
        if not cls.driver:
            # 实例化浏览器对象
            cls.driver = webdriver.Firefox()
            # 最大化
            cls.driver.maximize_window()
            # 打开url
            cls.driver.get(url)

        return cls.driver

    # 关闭浏览器
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            # 关闭浏览器驱动
            cls.driver.quit()
            # 必须置空操作
            cls.driver = None

if __name__ == "__main__":
    GetDriver().get_driver()