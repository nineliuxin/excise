from web.page_object.page.BasePage import BasePage
from web.page_object.page.PostPage import PostPage
from web.page_object.page.SelectedPage import SelectedPage


class ProfilePage(BasePage):
    def gotoSelected(self):
        return SelectedPage()

    def gotoPost_banner(self):
        element1 = self.driver.find_element_by_css_selector('.nav__btn--longtext')
        self.driver.execute_script("arguments[0].click();", element1)
        return PostPage()

    def gotoPost(self):
        return PostPage()