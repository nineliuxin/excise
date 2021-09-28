from web.page_object.page.BasePage import BasePage
from web.page_object.page.BrandDetailPage import BrandDetailPage


class BrandPage(BasePage):
    def gotoBrandDetailPage(self, name):
        self.driver.find_element_by_xpath("//*[contains(text(),'%s')]" % name)
        return BrandDetailPage()

    def select_all_brands(self):
        all_brands = self.driver.find_elements_by_xpath("//div[@class='met-img']//a")
        sum = len(all_brands)
        data_list = []
        for i in (0, 1):
            brand_name = all_brands[i].get_attribute("title")
            brand_img = ''
            try:
                img_element = self.driver.find_element_by_xpath("//*[contains(text(),'%s')]/../img" % brand_name)
                img_path = img_element[0].get_attribute("currentSrc")
                brand_img = img_path
            except:
                brand_img = ''
            finally:
                # todo 英文名称先写死为空
                brand_english_name = ''
                result = (brand_name, brand_english_name, brand_img, 'CURRENT_TIMESTAMP()')
                data_list.append(result)
        return data_list



