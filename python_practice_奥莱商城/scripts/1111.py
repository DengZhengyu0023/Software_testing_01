from base.base_driver import init_driver
from page.page import Page


class Test001:
    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.test_001 = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_001(self):
        self.test_001.page_home.page_home_login_if_not(self.test_001)