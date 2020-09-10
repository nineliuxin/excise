import os
from time import sleep

import autoit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.remote.command import Command

from web.page_object.driver.Client import Client
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage(object):
    def __init__(self):
        self.driver: WebDriver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver = Client.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return Client

    def loadSteps(self):
        pass

    def back(self):
        self.driver.back()

    def quit(self):
        sleep(3)
        self.driver.quit()

    def set_cookie(self, cookie_dict):
        self.driver.delete_cookie(cookie_dict['name'])
        self.driver.execute(Command.ADD_COOKIE, {'cookie': cookie_dict})

    def upload_img(self, path):
        os.system(r"E:\Autoit_data\0729\uploadimg.exe "+path)
