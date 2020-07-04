# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas
import pymysql

dbInfo = {
    'host': '106.13.24.153',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'lyp'
}


class SpidersPipeline:
    def process_item(self, item, spider):
        # print('=======================================================================')
        # print(item)
        # print('=======================================================================')
        list = [item['mtitle'], item['mtype'], item['mdate']]
        movie = pandas.DataFrame(data=list)
        movie.to_csv('./moviemaoyan.csv', mode='a', encoding='utf8', index=False, header=False)

        return item


class SpiderMysqlPipeline:

    def __init__(self,  conn, cur):
        self.conn = conn
        self.cur = cur
        print('__init__')

    @classmethod
    def from_crawler(cls, crawler):
        print('from_crawler')

        conn = pymysql.connect(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            db=crawler.settings.get('MYSQL_DB'),
            charset='utf8mb4'
        )
        cur = conn.cursor()

        return cls(
            conn=conn,
            cur=cur
        )

        # host=crawler.settings.get('MYSQL_HOST'),
        # port=self.port,
        # user=self.user,
        # password=self.password,
        # db=self.db,
        # charset='utf8mb4'

        # )

    # def open_spider(self, spider):
    #     self.conn = pymysql.connect(
    #         host=self.host,
    #         port=self.port,
    #         user=self.user,
    #         password=self.password,
    #         db=self.db,
    #         charset='utf8mb4'
    #     )
    #     self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        print('=======================================================================')
        print(item)
        print('=======================================================================')
        list = [item['mtitle'], item['mtype'], item['mdate']]
        movie = pandas.DataFrame(data=list)
        movie.to_csv('./moviemaoyan.csv', mode='a', encoding='utf8', index=False, header=False)

        sql = "INSERT INTO `movie` (`name`, `type`, `publish_date`) VALUES (%s, %s, %s)"
        self.cur.execute(sql, (item['mtitle'], item['mtype'], item['mdate']))

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.commit()
        self.conn.close()
