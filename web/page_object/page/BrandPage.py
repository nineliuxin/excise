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
        for i in range(0, sum):
            brand_name = all_brands[i].get_attribute("title")
            brand_img = ''
            try:
                img_element = self.driver.find_element_by_xpath("//*[contains(text(),'%s')]/../img" % brand_name)
                print(img_element)
                img_path = img_element.get_attribute("src")
                brand_img = img_path
            except:
                brand_img = ''
            finally:
                # todo 英文名称先写死为空
                brand_english_name = ''
                result = (brand_name, brand_english_name, brand_img)
                data_list.append(result)
            '''
            img_element = self.driver.find_element_by_xpath("//*[contains(text(),'%s')]/../img" % brand_name)
            print(img_element)
            img_path = img_element.get_attribute("src")
            brand_img = img_path
            # todo 英文名称先写死为空
            brand_english_name = ''
            result = (brand_name, brand_english_name, brand_img)
            data_list.append(result)
            '''
        return data_list



