import time

from selenium import webdriver
from selenium.webdriver import TouchActions, ActionChains
from selenium.webdriver.remote.webdriver import WebDriver

from web_demo.web控件.BaseTestCase import BaseTestCase


class TestClick(BaseTestCase):
    driver: WebDriver
    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("http://sahitest.com/demo/clicks.htm")
        return cls.driver

    def test_double_clcik(self):
        # self.driver.find_element_by_css_selector('body > form > input[type=button]:nth-child(8)')
        # self.driver.implicitly_wait(10)
        el1 = self.driver.find_element_by_css_selector('body > form > input[type=button]:nth-child(8)')
        ActionChains(self.driver).double_click(el1).perform()

    def test_clcik_me(self):
        # self.driver.find_element_by_css_selector('body > form > input[type=button]:nth-child(10)')
        # self.driver.implicitly_wait(10)
        el1 = self.driver.find_element_by_css_selector('body > form > input[type=button]:nth-child(10)')
        ActionChains(self.driver).click(el1).perform()

    def test_right_clcik(self):
        # self.driver.find_element_by_css_selector('body > form > input[type=button]:nth-child(13)')
        # self.driver.implicitly_wait(10)
        el1 = self.driver.find_element_by_css_selector('body > form > input[type=button]:nth-child(13)')
        ActionChains(self.driver).context_click(el1).perform()


class TestDrag(BaseTestCase):
    driver: WebDriver
    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://www.runoob.com/try/try.php?filename=tryhtml5_draganddrop")

    def test_drag_drop(self):
        self.driver.switch_to.frame('iframeResult')
        el1 = self.driver.find_element_by_css_selector("#drag1")
        self.driver.implicitly_wait(10)
        el2 = self.driver.find_element_by_css_selector("#div1")
        action = ActionChains(self.driver)
        action.drag_and_drop(el1, el2).perform()

    def test_move_to(self):
        self.driver.switch_to.frame('iframeResult')
        el1 = self.driver.find_element_by_css_selector("#drag1")
        self.driver.implicitly_wait(10)
        el2 = self.driver.find_element_by_css_selector("#div1")
        action = ActionChains(self.driver)
        action.click_and_hold(el1).release(el2).perform()
        time.sleep(5)


