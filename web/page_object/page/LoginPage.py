from web.page_object.page.BasePage import BasePage
from web.page_object.page.ProfilePage import ProfilePage
from selenium.webdriver.remote.command import Command

class LoginPage(BasePage):
    def Login(self, account, password):
        self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(account)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        self.driver.find_element_by_css_selector('.modal__login__btn').click()
        return self

    def cancel_picturecode(self):
        # 处理图片验证码
        self.driver.find_element_by_xpath('//*[@class="geetest_close"]').click()
        return self

    def cancel(self):
        # 退出登录界面
        self.driver.find_element_by_css_selector('.modal__login .close').click()
        return self
    def login_by_cookie(self):
        # self.driver.set_cookie({'name': 'device_id', 'value': '24700f9f1986800ab4fcc880530dd0ed'})
        # self.driver.add_cookie({'name': 'xq_a_token', 'value': '59c7f29a02092d444535c5d3662384e5e0e0bf41'})
        # self.driver.add_cookie({'name': 'xqat', 'value': '59c7f29a02092d444535c5d3662384e5e0e0bf41'})
        # self.driver.add_cookie({'name': 'xq_r_token', 'value': '3c8b682d95eba120dcd04fdf9c28e266a5e3d0cc'})
        # self.driver.add_cookie({'name': 'xq_is_login', 'value': '1'})
        # self.driver.add_cookie({'name': 'u', 'value': '4933045715'})
        # self.driver.add_cookie({"name": "bid", "value": "27c69a0fccba2ec77d9a24ec4cb25b48_kd5q149u"})
        # self.driver.add_cookie({"name": "Hm_lpvt_1db88642e346389874251b5a1eded6e3", "value": "1595985537"})
        # self.driver.add_cookie({"name": "Hm_lvt_1db88642e346389874251b5a1eded6e3", "value": "1595753262,1595927375,\
        # 1595927455,1595928624"})

        self.set_cookie({'name': 'device_id', 'value': '24700f9f1986800ab4fcc880530dd0ed'})
        self.set_cookie({'name': 'xq_a_token', 'value': '59c7f29a02092d444535c5d3662384e5e0e0bf41'})
        self.set_cookie({'name': 'xqat', 'value': '59c7f29a02092d444535c5d3662384e5e0e0bf41'})
        self.set_cookie({'name': 'xq_r_token', 'value': '3c8b682d95eba120dcd04fdf9c28e266a5e3d0cc'})
        self.set_cookie({'name': 'xq_is_login', 'value': '1'})
        self.set_cookie({'name': 'u', 'value': '4933045715'})
        self.set_cookie({"name": "bid", "value": "27c69a0fccba2ec77d9a24ec4cb25b48_kd5q149u"})
        self.set_cookie({"name": "Hm_lpvt_1db88642e346389874251b5a1eded6e3", "value": "1595987353"})
        self.set_cookie({"name": "Hm_lvt_1db88642e346389874251b5a1eded6e3", "value": "1595753262,1595927375,\
                1595927455,1595928624"})

        # self.driver.add_cookie({'name': '__utma', 'value': '1.792609483.1595927352.1595927352.1595927352.1'})
        # self.driver.add_cookie({'name': '__utmc', 'value': '1'})
        # self.driver.add_cookie({'name': '__utmz', 'value': '1.1595927352.1.1.utmcsr=(direct)|utmccn=(direct)|\
        # utmcmd=(none)'})
        # self.driver.add_cookie({'name': '__utmb', 'value': '1.2.10.1595927352'})
        #
        # self.driver.add_cookie({'name': 'snbim_minify', 'value': 'true'})
        # self.driver.add_cookie({'name': 'captcha_id', 'value': '9ibyE945WmGbWynrQKQT4f7aMLtWsU'})
        # self.driver.add_cookie({'name': 'acw_tc', 'value': '2760823e15959435392967503e0b1cb9fc2cb2c\
        # f50eda88317a5dcd1c57b32'})
        # self.driver.add_cookie({'name': 'xq_id_token', 'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9\
        # .eyJ1aWQiOjQ5MzMwNDU3MTUsImlzcyI6InVjIiwiZXhwIjoxNTk4NTIwODQ5LCJjdG0iOjE1OTU5NDUwMTI3NjAsImNpZ\
        # CI6ImQ5ZDBuNEFadXAifQ.jEoRO1wRCcWZnlJcgY9qPDIsx9VU33E5_VwerJ85fbnUKKOOfuFjz45mihxNO6wQBLUlR_jXE\
        # 12pqNOFnvm9cjMVY0afI1ipvKgPPofiNB4hsWQr20gwtXHyUeY9IRmyum5FvOYRnDaLhYeOlPOwABSLCKC3aXkwAwOPy-r5\
        # 1y8oKlgLSRbainKILrxPvXU_7N77POfXqtgAouuoNDthbRF60AVN16nzU9U0KSmVy9kWK54asKxUUkgunk1C3modO4YDBucB\
        # V-zyy8SGV1ArijCAtVhhQeljnBRtNE3MitiuJ50e0nP4mkEYzIENZo7Bl_4dDDIkPEP1OQ0-Cn2h_A'})
        # self.driver.add_cookie({'name': 'xq_is_login', 'value': '1'})
        # self.driver.add_cookie({'name': 's', 'value': 'c411gjadlx'})

        print(self.driver.get_cookies())
        self.driver.refresh()
        print(self.driver.get_cookies())

        return self

    def gotoProfile(self):
        return ProfilePage()