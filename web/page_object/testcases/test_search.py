import pytest

from web.page_object.page.Web import Web
from web.page_object.testcases.BaseTestCase import BaseTestCase


class TestSearch(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.mainPage = Web.main()
    # @classmethod
    # def setup_method(cls):
    #     cls.searchPage = cls.mainPage.gotoSearch("alibaba")

    @pytest.mark.parametrize("user_info", [
        {"account": "156005347600", "password": "1111111"},
        {"account": "15600534760", "password": "1111111"}
    ])
    def test_search_add_stock_without_user(self, user_info):
        # todo
        self.searchPage = self.mainPage.gotoSearch("alibaba")
        self.loginPage = self.searchPage.follow("09988")
        self.loginPage.Login(user_info['account'], user_info['password'])
        self.loginPage.cancel_picturecode()
        self.loginPage.cancel()
        return self

    def teardown_method(self):
        self.searchPage.back()

    def teardown_class(self):
        self.mainPage.quit()