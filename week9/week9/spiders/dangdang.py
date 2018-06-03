# -*- coding: utf-8 -*-
import scrapy
from ..items import DangItem


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input']
    # http: // search.dangdang.com /?key = python & act = input& page_index=2
    def parse(self, response):
        item = DangItem()
        cname = response.css('ul li[class*="line"] p[class="name"] a::attr(title)').extract_first()
        print(cname)
        pass
