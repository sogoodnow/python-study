# -*- coding: utf-8 -*-
import pymysql
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class Image_pipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        '''通过抓取的item对象获取图片信息，并创建Request请求对象添加调度队列，等待调度执行下载'''
        for imgurl in item['img_url']:
            yield Request(imgurl)

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")
        item['img_path'] = file_paths
        return item


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
        try:
            self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
            self.cursor = self.db.cursor()
        except Exception as e:
            print(str(e))

    def process_item(self, item, spider):
        # 出版日期简单处理
        if str(item['p_time']).split('/')[1]:
            item['p_time'] = str(item['p_time']).split('/')[1]
        sql = "insert into dangdang(title,detail,price,comment_num,author,publish,p_time)values('%s','%s','%s','%s','%s','%s','%s')"%(item['title'],item['detail'],item['price'],item['comment_num'],item['author'],item['publish'],item['p_time'])
        try:
            print(item)
            print(sql)
            self.cursor.execute(sql)
            self.db.commit()
            return item
        except Exception as e:
            print(str(e))

    def close_spider(self,spider):
        self.cursor.close()