# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MongoPileline(object):
    def __init__(self,MONGO_URI,MONGO_DB):
        self.MONGO_URI = MONGO_URI
        self.MONGO_DB = MONGO_DB

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            MONGO_URI = crawler.settings.get("MONGO_URI"),
            MONGO_DB = crawler.settings.get("MONGO_DB")
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.MONGO_URI)
        self.db = self.client[self.MONGO_DB]


    def process_item(self, item, spider):
        collection_name = item.__class__.__name__
        self.db[collection_name].insert(dict(item))
        return item


    def close_spider(self,spider):
        self.client.close()



