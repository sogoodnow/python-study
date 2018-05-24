# -*- coding: utf-8 -*-
import scrapy


class FangSpider(scrapy.Spider):
    name = 'fang'
    allowed_domains = ['fang.5i5j.com']
    start_urls = ['http://fang.5i5j.com/bj/loupan/']

    def parse(self, response):
        print(response.status)
        # pass
