# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# def clean(value):
#     print(value)
#     return str(value).split('/')[1]

class SinaItem(scrapy.Item):
    # 大分类标题
    title_first = scrapy.Field()
    # 二级分类标题、链接
    title_second = scrapy.Field()
    link_second = scrapy.Field()
    # 三级分类标题、链接地址
    title_third = scrapy.Field()
    link_third = scrapy.Field()

class DangItem(scrapy.Item):
    # 图片
    img_urls = scrapy.Field()
    img_path = scrapy.Field()
    # images = scrapy.Field()
    # 名称
    title = scrapy.Field()
    # 详细
    detail = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 评论数
    comment_num = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 出版社
    publish = scrapy.Field()
    # 出版时间
    p_time = scrapy.Field()


