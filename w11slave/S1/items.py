# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class DoubanItem(Item):
    # 书名
    bookname = Field()
    # 作者
    author = Field()
    # 出版社
    publish = Field()
    # 原作名
    originame = Field()
    # 译者
    translater = Field()
    # 出版年
    ptime = Field()
    # 页数
    pages = Field()
    # 定价
    price = Field()
    # 装帧
    zhuangzheng = Field()
    # 丛书
    books = Field()
    # isbn
    isbn = Field()
    # 评分
    starts = Field()
    # 评论人数
    commentcnt = Field()



