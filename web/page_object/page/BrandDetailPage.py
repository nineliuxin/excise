from web.page_object.page.BasePage import BasePage
from web.page_object.page.ProductPage import ProductPage

class BrandDetailPage(BasePage):
    _page_size = 6
    def select_all_products(self):
        all_brand_products = []
        this_pages = self.driver.find_elements_by_xpath("//div[@class='met_pager']/a")
        this_page_size = len(this_pages)
        if this_page_size < self._page_size:
            all_brand_products.append(self.select_this_page_products())
        else:
            NextPage = self.gotoNextPage()
            return self.select_all_products(NextPage)
        return all_brand_products

    def select_this_page_products(self):
        this_page_elements = self.driver.find_elements_by_xpath("//div[@class='news_list_title']/a")
        sum = len(this_page_elements)
        data_list = []
        for i in (0, sum):
            productname = this_page_elements[i].text()
            # todo 进入产品详情页获取产品详情
            result = self.gotoProductPage(productname).get_all_detail()
            data_list.append(result)
        return data_list

    def gotoProductPage(self, productname):
        self.driver.find_element_by_xpath("//div[@class='news_list_title']/a[@text='%s']" % productname).click()
        return ProductPage()

    def gotoNextPage(self):
        try:
            self.driver.find_element_by_xpath("//span[@class='NextSpan']/a[text()='下一页']").click()
            return BrandDetailPage()
        except:
            pass

