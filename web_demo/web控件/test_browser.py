import os

from selenium import webdriver


class TestBrowser(object):

    def setup(self):
        browser = os.getenv('browser')
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        return self
    def teardown(self):
        pass

    def test_browser(self):
        self.driver.get("https://www.baidu.com")
        print(self.driver)
