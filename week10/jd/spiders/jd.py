# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from ..items import JdItem

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
        products = response.css("#plist ul li")
        for pd in products:
            item = JdItem()
            item['img'] = pd.css(".p-img a img::attr(src)").extract_first()
            item['price'] = pd.css(".p-price strong[class='J_price'] i").extract_first()
            item['name'] = pd.css(".p-name a em::text").extract_first()
            # pd.xpath('//div[@class="p-commit p-commit-n"]/strong/a/text()')
            item['comment_cnt'] = pd.css(".p-commit .comment::text").extract_first()
            print(item)
            yield item


