from web.page_object.page.BasePage import BasePage
from web.page_object.page.LoginPage import LoginPage


class SearchPage(BasePage):
    def follow(self, key):
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]/../../../..//*[@class="follow__control"]'%key).click()
        return LoginPage()

