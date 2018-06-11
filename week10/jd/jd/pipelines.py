# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MongoPileline(object):
    def __init__(self,uri,db):
        self.uri = uri
        self.db = db
        self.client = None
        self.collection = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            uri=crawler.settings.get("MONGO_URI"),
            db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.uri)
        self.collection = self.client[self.db]


    def process_item(self, item, spider):
        pass


    def close_spider(self,spider):
        self.client.close()



