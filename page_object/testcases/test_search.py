import pytest

from page_object.page.App import App
from page_object.page.MainPage import MainPage



class TestSearch(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()

    def setup_method(self):
        self.mainPage: MainPage = TestSearch.mainPage
        self.searchPage = self.mainPage.gotoSearch()

    def test_is_selected_stock(self):
        self.searchPage.search("alibaba")
        assert self.searchPage.isInSelected("BABA")==True
        assert self.searchPage.isInSelected("88")==False

    def teardown_method(self):
        self.searchPage.cancel()

    def test_is_follow_user(self):
        # todo: 作业2
        self.searchPage.searchByUser("alibaba")
        assert self.searchPage.isFollowed("阿里爸爸") == True
        assert self.searchPage.isFollowed("alibaba19") == False