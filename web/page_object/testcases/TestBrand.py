import pytest

from web.page_object.page.JeebeiWeb import JeebeiWeb
from web.page_object.testcases.BaseTestCase import BaseTestCase


class TestBrand(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.mainPage = JeebeiWeb.main()

    def test_select_all_brands(self):
        # todo
        self.brandPage = self.mainPage.gotoBrand()
        return self

    def teardown_method(self):
        self.searchPage.back()

    def teardown_class(self):
        self.mainPage.quit()