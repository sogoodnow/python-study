# -*- coding: utf-8 -*-
import pymysql
from scrapy.pipelines.images import ImagesPipeline
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Mysql_pipeline(object):
    def __init__(self,host,database,user,password,port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.db=None
        self.cursor=None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get("MYSQL_HOST"),
            database = crawler.settings.get("MYSQL_DATABASE"),
            user = crawler.settings.get("MYSQL_USER"),
            password = crawler.settings.get("MYSQL_PASS"),
            port = crawler.settings.get("MYSQL_PORT")
        )

    def open_spider(self,spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = "insert into dangdang(img,name,detail,price," \
              "comment_num,author,publish,p_time) " \
              "values ('%s','%s','%s','%s','%d','%s','%s','%s')"%\
              (item['img'],item['name'],item['detail'],item['price'],int(item['comment_num']),item['author'],item['publish'],item['p_time'])
        self.cursor.execute(sql)

    def close_spider(self,spider):
        self.cursor.close()