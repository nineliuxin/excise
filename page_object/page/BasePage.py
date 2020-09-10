import inspect
import json

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.Client import AndroidClient
from page_object.page.Wrapper import handle_black


class BasePage(object):
    element_black = [
        (By.XPATH, "ddd")
    ]
    def __init__(self):
        self.driver: WebDriver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver = AndroidClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient

    def screenshot(self, name):
        self.driver.save_screenshot(name)

    @handle_black
    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self.driver.find_elements(*locator)
        else:
            elements = self.driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self.driver.find_element(*locator)
        else:
            element = self.driver.find_element(locator, value)
        return element

    @handle_black
    def findByText(self, text) -> WebElement:
        locator = (By.XPATH, "//*[@text='%s']" % text)
        print(locator)
        return self.find(locator)

    def loadSteps(self, po_path, **kwargs):
        file = open(po_path, 'r', encoding='UTF-8')
        po_data = yaml.load(file)
        key = inspect.stack()[1].function
        po_method = po_data[key]
        raw = json.dumps(po_method)
        for key, value in kwargs.items():
            raw = raw.replace('${' + key + '}', value)
        po_method = json.loads(raw)

        po_elements = dict()
        if po_data.keys().__contains__("elements"):
            po_elements = po_data['elements']
        # po_elements=yaml.load(open('xxx.yaml'))['elements']

        for step in po_method:
            step: dict
            element_platform = dict()
            if step.keys().__contains__("element"):
                element_platform = po_elements[step['element']][AndroidClient.platform]
            else:
                element_platform = {"by": step['by'], "locator": step['locator']}
            element: WebElement = self.find(element_platform['by'], element_platform['locator'])
            action = str(step['action']).lower()
            # todo: 定位失败，多数是弹框，try catch后进入一个弹框处理 元素智能等待
            if action == "click":
                element.click()
            elif action == "sendkeys":
                text = str(step['text'])
                element.send_keys(text)
            elif action == "text":
                return element.text
            else:
                return element
