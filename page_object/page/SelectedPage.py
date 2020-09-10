from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page_object.driver.Client import AndroidClient
from page_object.page.BasePage import BasePage


class SelectedPage(BasePage):
    def addDefault(self):
        return self

    def gotoHS(self):
        # self.findByText("沪深").click()
        self.loadSteps("../data/SelectPage.yaml")
        return self

    def getPriceByName(self, name) -> float:
        price=self.loadSteps("../data/SelectPage.yaml", name=name)
        return float(price)