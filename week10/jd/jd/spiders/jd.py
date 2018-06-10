# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from week10.jd.jd.items import Product
from urllib.parse import quote


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    base_url = 'https://list.jd.com/list.html?cat=670,671,672&page='

    def start_requests(self):
        max_page = self.settings.get('PAGE_COUNT')
        for page in range(1,max_page+1):
            url = self.base_url + str(page)
            yield Request(url=url,callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        products = response.css('#plist ul li.gl-item')
        print(products)
        for p in products:
            item = Product()
            item['img'] = p
            item['price'] = p
            item['name'] = p
            item['comment_cnt'] = p
            yield item
