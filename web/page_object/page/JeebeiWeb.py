from web.page_object.page.JeebeiMainPage import JeebeiMainPage
from web.page_object.page.BasePage import BasePage

class JeebeiWeb(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_web_firefox()
        return JeebeiMainPage()