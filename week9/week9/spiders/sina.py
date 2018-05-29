# -*- coding: utf-8 -*-
import scrapy


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['http://news.sina.com.cn/guide/']
    start_urls = ['http://http://news.sina.com.cn/guide//']

    def parse(self, response):
        pass
