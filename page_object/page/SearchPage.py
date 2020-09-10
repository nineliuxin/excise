from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    _edit_locator=(By.CLASS_NAME, "android.widget.EditText")

    def search(self, key):
        # self.find(self._edit_locator).send_keys(key)
        self.loadSteps("../data/SearchPage.yaml", keyword=key)
        return self

    def addToSelected(self, key):
        self.loadSteps("../data/SearchPage.yaml", keyword=key)
        return self


    def removeFromSelected(self, key):
        self.loadSteps("../data/SearchPage.yaml", keyword=key)
        return self

    def isInSelected(self, key):
        ele = self.loadSteps("../data/SearchPage.yaml", keyword=key)
        id = ele.get_attribute("resourceId")
        print(id)
        return "followed_btn" in id

    def cancel(self):
        self.loadSteps("../data/SearchPage.yaml")

    def searchByUser(self, key):
        # todo: 作业2
        # self.find(self._edit_locator).send_keys(key)
        # self.findByText("用户").click()
        self.loadSteps("../data/SearchPage.yaml", keyword=key)
        return self

    def isFollowed(self, key):
        # todo: 作业2
        ele = self.loadSteps("../data/SearchPage.yaml", keyword=key)
        id = ele.get_attribute("resourceId")
        print(id)
        return "followed_btn" in id