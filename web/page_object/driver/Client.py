import yaml
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver


class Client(object):
    driver: WebDriver
    @classmethod
    def restart_web_chrome(cls) -> WebDriver:
        # cls.driver = webdriver.Chrome()
        cls.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://xueqiu.com/")
        return cls.driver

    @classmethod
    def restart_web_firefox(cls) -> WebDriver:
        # cls.driver = webdriver.Firefox()
        cls.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.FIREFOX)
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://xueqiu.com/")
        return cls.driver

    # @classmethod
    # def initDriver(cls, key):
    #     driver_data = yaml.load(open("../data/driver.yaml"))
    #     platform = str(driver_data['platform'])
    #     cls.platform = platform
    #     url = driver_data[key]['url']
    #     implicitly_wait = driver_data[key]['implicitly_wait']
    #     caps = driver_data[key]['caps'][platform]
    #     cls.driver = webdriver.Remote(desired_capabilities=caps)
    #     cls.driver.implicitly_wait(implicitly_wait)
    #     cls.driver.get(url)
    #     return cls.driver