# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class CsdnItem(Item):
    # 课程标题
    title = Field()
    # 课程地址
    curl = Field()
    # 课时
    period = Field()
    # 讲师
    teacher = Field()
    # 适合人群
    people = Field()
    # 学习人数
    members = Field()
    # 价格
    price = Field()
    # 课程大纲
    curriculum = Field()

