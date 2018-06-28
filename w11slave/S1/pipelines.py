# -*- coding: utf-8 -*-
import pymysql

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
        sql = "insert into douban(bookname,author,publish,originame,translater,ptime,pages,price,zhuangzheng,books,isbn,starts,commentcnt,weburl,bookintro,authorintro)" \
              "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
              %(item['bookname'],item['author'],item['publish'],item['originame'],item['translater'],item['ptime'],item['pages'],item['price'],item['zhuangzheng'],item['books'],item['isbn'],item['starts'],item['commentcnt'],item['weburl'],item['bookintro'],item['authorintro'])
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return item
        except Exception as e:
            print(str(e))

    def close_spider(self,spider):
        self.cursor.close()