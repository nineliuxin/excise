from web.page_object.page.BasePage import BasePage
from web.page_object.page.LoginPage import LoginPage
from web.page_object.page.SearchPage import SearchPage


class MainPage(BasePage):
    def gotoSelected(self):
        pass

    def gotoSearch(self, key):
        self.driver.find_element_by_css_selector('.Header_nav__search_1YZ input').send_keys(key)
        self.driver.find_element_by_css_selector('span.Header_nav__search__addon_2nk').click()
        return SearchPage()

    def gotoLogin(self):
        # self.driver.find_element_by_css_selector('.nav__login__btn ').click()
        return LoginPage()