import pytest

from web.page_object.common.BrandSql import BrandSql
from web.page_object.page.JeebeiWeb import JeebeiWeb
from web.page_object.testcases.BaseTestCase import BaseTestCase


class TestBrand(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.mainPage = JeebeiWeb.main()

    def test_select_all_brands(self):
        # todo
        self.brandPage = self.mainPage.gotoBrand()
        result = self.brandPage.select_all_brands()
        #result = [('初良优品', '', '', 0)]
        print(result)
        bsql = BrandSql('10.12.27.205', 3306, 'rong', 'qa-ins', 'aphrodite_app')
        bsql.insertBrand(*result)

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.mainPage.quit()