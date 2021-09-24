from web.page_object.page.BasePage import BasePage

class BrandPage(BasePage):
    def gotoBrandDetailPage(self,num):
        pass

    def select_all_brands(self):
        all_brands = self.driver.find_elements_by_xpath("//div[@class='met-img']//a")
        sum = len(all_brands)
        for i in (0, 1) :
            brand_name = all_brands[i].get_attribute("title")
