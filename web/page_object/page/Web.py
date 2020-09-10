from web.page_object.page.MainPage import MainPage
from web.page_object.page.BasePage import BasePage



class Web(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_web_chrome()
        return MainPage()
