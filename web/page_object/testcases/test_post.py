from time import sleep

import pytest

from web.page_object.page.LoginPage import LoginPage
from web.page_object.page.MainPage import MainPage
from web.page_object.page.ProfilePage import ProfilePage
from web.page_object.page.Web import Web
from web.page_object.testcases.BaseTestCase import BaseTestCase


class TestPostEditorFunction(BaseTestCase):
    # topic_info = {
    #     {"key": "在一起", "topic": "在一起才是向往的生活"}
    # }
    @classmethod
    def setup_class(cls):
        cls.mainPage: MainPage = Web.main()
        cls.loginPage: LoginPage = cls.mainPage.gotoLogin()
        cls.profilePage: ProfilePage = cls.loginPage.login_by_cookie().gotoProfile()

    def setup_method(self):
        self.postPage = self.profilePage.gotoPost_banner()

    def test_add_emoji(self):
        self.postPage.add_content_emoji()

    @pytest.mark.parametrize("content", [("这是我的第一个帖子")])
    def test_add_text(self, content):
        self.postPage.add_content_text(content)

    @pytest.mark.parametrize("img", [(r"C:\Users\Administrator\Desktop\霓虹映像\masami1.jpg")])
    def test_add_image(self, img):
        self.postPage.add_content_image(img)

    @pytest.mark.parametrize("at_info", [{"key": "Lavignel", "username": "Lavignel0y"}])
    def test_add_at(self, at_info):
        key = at_info['key']
        username = at_info['username']
        self.postPage.add_content_at(key, username)

    # @pytest.mark.parametrize("key,topic", [("在一起", "在一起才是向往的生活​")])
    # def test_add_topic(self, key, topic):
    #     self.postPage.add_content_topic(key, topic)

    @pytest.mark.parametrize("topic_info", [{"key": "在一起", "topic": "在一起才是向往的生活"}])
    def test_add_topic(self, topic_info):
        key = topic_info['key']
        topic = topic_info['topic']
        self.postPage.add_content_topic(key, topic)

    @pytest.mark.parametrize("stock_info", [{"key": "ali", "stock": "阿里健康"}])
    def test_add_stock(self, stock_info):
        key = stock_info['key']
        stock = stock_info['stock']
        self.postPage.add_content_stock(key, stock)

    @pytest.mark.parametrize("qa_info", [{"key": "123", "username": "12345AA32"}])
    def test_add_qa(self, qa_info):
        key = qa_info['key']
        username = qa_info['username']
        self.postPage.add_content_qa(key, username)

    def test_add_reward(self):
        self.postPage.add_content_reward()

    # def test_release(self):
    #     self.postPage.add_content_text("这是我发表的第一个帖子")
    #     self.postPage.content_release()

    def teardown_method(self):
        sleep(5)
        self.postPage.quit_post()

# class TestPostAll(object):
#     @classmethod
#     def setup_class(cls):
#         cls.mainPage: MainPage = Web.main()
#         cls.loginPage: LoginPage = cls.mainPage.gotoLogin()
#         cls.profilePage: ProfilePage = cls.loginPage.login_by_cookie()
#
#     def setup_method(self):
#         self.postPage = self.profilePage.gotoPost_banner()


