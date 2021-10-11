from web.page_object.common.MyPyMysql import MyPyMysql
import time

class BrandSql(MyPyMysql):
    def insertBrand(self, *data_list):
        sql = "insert into `brand`(`brand_name`,`brand_english_name`,`brand_img`) values %s"
        num = len(data_list)
        self.cur = self.conn.cursor()
        self.cur.executemany(sql, data_list)
        #if content:
        #   print('成功插入')
        self.conn.commit()
        self.cur.close()  # 关闭游标
        self.conn.close()  # 关闭pymysql连接

    def select_brand_id_by_brandname(self, brandname):
        sql = "select id from brand where brandname=%s" % brandname
        self.cur = self.conn.cursor()
        try:
            # 执行SQL语句
            self.cur.execute(sql)
            # 获取所有记录列表
            result = self.cur.fetchone()
            return result
        except:
            print("Error: unable to fetch data")

