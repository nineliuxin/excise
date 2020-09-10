import time
import autoit

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.page_object.page.BasePage import BasePage
from web.page_object.page.LongTextPage import LongTextPage


class PostPage(BasePage):
    # 浮窗发帖
    _editor_text_locator = '.modal__tiny__editor .lite-editor__textarea \
       .medium-editor-element > p:last-child'
    _editor_emoji_locator = '.modal__tiny__editor .emoji__dropdown__parent .iconfont'
    _editor_image_locator = '.modal__tiny__editor .lite-editor__upload--img .iconfont'
    _editor_at_locator = '.modal__tiny__editor .lite-editor__toolbar__btn:nth-child(3)'
    _editor_topic_locator = '.modal__tiny__editor .lite-editor__toolbar__btn:nth-child(4)'
    _editor_stock_locator = '.modal__tiny__editor .last .iconfont'
    _editor_qa_locator = '//*[@class="modal modal--lg modal__tiny__editor"]\
    //*[@class="lite-editor__toolbar"]//*[contains(text(),"问答")]'
    _qa_input = '.modal__tiny__editor .pay-mention__container > input'
    _editor_reward_locator = '//*[@class="modal modal--lg modal__tiny__editor"]\
    //*[@class="lite-editor__toolbar"]//*[contains(text(),"悬赏")]'
    _editor_longtext_locator = '//*[@class="modal modal--lg modal__tiny__editor"]\
    //*[@class="lite-editor__toolbar"]//*[contains(text(),"长文")]'
    _editor_release_locator = '.modal__tiny__editor .lite-editor__toolbar__post'
    _emoji_choose = '.modal__tiny__editor .emoji__item:nth-child(1) img'
    _qa_pay_close = '//*[contains(text(),"确定提问金额")]/..//*[@class="close"]'
    _reward_pay_close = '//*[contains(text(),"设定悬赏金额")]/..//*[@class="close"]'
    _editor_quit = '.modal__tiny__editor .close'
    _result_box: str = '.mention-popup'

    # 个人首页发帖
    # _editor_content_locator= '.lite-editor.expand .lite-editor__textarea \
    #        .medium-editor-element > p:last-child'
    # _editor_emoji_locator='.lite-editor.expand .emoji__dropdown__parent .iconfont'
    # _editor_image_locator = '.lite-editor.expand .lite-editor__upload--img .iconfont'
    # _editor_at_locator = '.lite-editor.expand .lite-editor__toolbar__btn:nth-child(3) .iconfont'
    # _editor_topic_locator = '.lite-editor.expand .lite-editor__toolbar__btn:nth-child(4) .iconfont'
    # _editor_stock_locator = '.lite-editor.expand .last .iconfont'
    # _editor_qa_locator = '//*[@class="editor-container"]\
    #     //*[@class="lite-editor__toolbar"]//*[contains(text(),"问答")]'
    # _editor_reward_locator = '//*[@class="editor-container"]\
    #     //*[@class="lite-editor__toolbar"]//*[contains(text(),"悬赏")]'
    # _editor_longtext_locator = '//*[@class="editor-container"]\
    #     //*[@class="lite-editor__toolbar"]//*[contains(text(),"长文")]'


    def add_content_text(self, content):
        self.driver.find_element_by_css_selector(self._editor_text_locator).send_keys(content)

    def add_content_emoji(self):
        self.driver.find_element_by_css_selector(self._editor_emoji_locator).click()
        self.driver.find_element_by_css_selector(self._emoji_choose).click()

    def add_content_image(self, img_path):
        self.driver.find_element_by_css_selector(self._editor_image_locator).click()
        # autoit.run("E:\\Autoit_data\\0729\\uploadimg.exe")
        self.upload_img(img_path)
        time.sleep(5)

    def add_content_at(self, key, username):
        self.driver.find_element_by_css_selector(self._editor_at_locator).click()
        text1 = self.driver.find_element_by_css_selector(self._editor_text_locator).text
        # 每次都要比较文本非常繁琐，应该定位文本框区域 考虑autoit定位
        if '@' not in text1:
            self.driver.find_element_by_css_selector(self._editor_at_locator).click()
        # WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self._result_box)))
        self.add_content_text(key)
        WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.XPATH, '//*\
         [@class="mention-popup__bd mention-popup--list"]//*[text()="%s"]' % username)))
        self.driver.find_element_by_xpath('//*[@class="mention-popup__bd mention-popup--list"]\
            //*[text()="%s"]' % username).click()

    def add_content_topic(self, key, topic):
        topic = "#" + topic + "#"
        print(topic)
        self.driver.find_element_by_css_selector(self._editor_topic_locator).click()
        text1 = self.driver.find_element_by_css_selector(self._editor_text_locator).text
        if '#' not in text1:
            self.driver.find_element_by_css_selector(self._editor_topic_locator).click()
        # self.driver.find_element_by_css_selector(self._editor_topic_locator).click()
        self.add_content_text(key)
        WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.XPATH, '//*\
                [@class="mention-popup__bd mention-popup--list"]//*[text()="%s"]' % topic)))
        self.driver.find_element_by_xpath('//*[@class="mention-popup__bd mention-popup--list"]\
        //*[text()="%s"]' % topic).click()

    def add_content_stock(self, key, stock):
        self.driver.find_element_by_css_selector(self._editor_stock_locator).click()
        text1 = self.driver.find_element_by_css_selector(self._editor_text_locator).text
        if '$' not in text1:
            self.driver.find_element_by_css_selector(self._editor_stock_locator).click()
        self.add_content_text(key)
        WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.XPATH, '//*\
                        [@class="mention-popup__bd mention-popup--list"]//*[contains(text(),"%s")]' % stock)))
        self.driver.find_element_by_xpath('//*[@class="mention-popup__bd mention-popup--list"]\
                //*[contains(text(),"%s")]' % stock).click()

    def add_content_qa(self, key, username):
        self.driver.find_element_by_xpath(self._editor_qa_locator).click()
        self.driver.find_element_by_css_selector(self._qa_input).send_keys(key)
        WebDriverWait(self.driver, 10, 0.5).until(expected_conditions.presence_of_element_located((By.XPATH, '//*\
                                [@class="pay-mention__container"]//*[text()="%s"]' % username)))
        self.driver.find_element_by_xpath('//*[@class="pay-mention__container"]//*[text()="%s"]' % username).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self._qa_pay_close).click()

    def add_content_reward(self):
        self.driver.find_element_by_xpath(self._editor_reward_locator).click()
        self.driver.find_element_by_xpath(self._reward_pay_close).click()

    def  gotoLongTextPage(self):
        self.driver.find_element_by_css_selector(self._editor_longtext_locator).click()
        return LongTextPage()

    def content_release(self):
        self.driver.find_element_by_css_selector(self._editor_release_locator).click()

    def line_break(self):
        self.driver.find_element_by_css_selector(self._editor_text_locator).send_keys(Keys.ENTER)

    def quit_post(self):
        self.driver.find_element_by_css_selector(self._editor_quit).click()
