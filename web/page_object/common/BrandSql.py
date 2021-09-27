from web.page_object.common.MyPyMysql import MyPyMysql
import time

class BrandSql(MyPyMysql):
    def insertBrand(self, data_list):
        sql = "insert into brand(brand_name,brand_english_name,brand_img,create_time) values (%s,%s,%s,%s)"
        num = data_list.count()
        self.cur = self.conn.cursor()
        content = self.cur.executemany(sql, data_list)
        if content:
            print('成功插入第{}条数据'.format(num - 1))
        self.conn.commit()