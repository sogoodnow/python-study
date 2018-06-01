# -*- coding: utf-8 -*-
import scrapy


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/']
    # http: // search.dangdang.com /?key = python & act = input& page_index=2
    def parse(self, response):

        pass
