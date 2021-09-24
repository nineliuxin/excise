from web.page_object.page.BasePage import BasePage

class JeebeiMainPage(BasePage):
    def gotoBrand(self):
        self.driver.find_element_by_partial_link_text("更多化妆品牌").click()
        return BrandPage()
