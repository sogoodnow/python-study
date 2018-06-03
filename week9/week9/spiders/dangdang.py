# -*- coding: utf-8 -*-
import scrapy
from ..items import DangItem
from scrapy.loader import ItemLoader


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input']
    # http: // search.dangdang.com /?key = python & act = input& page_index=2
    def parse(self, response):
        item = ItemLoader(item=DangItem(),response=response)
        # 标题
        item.add_css('title','ul li[class*="line"] p[class="name"] a::attr(title)')
        # 详细
        item.add_css('detail','ul li[class*="line"] p[class="detail"]::text')
        # 价格
        item.add_css('price','ul li[class*="line"] p[class="price"] span[class="search_pre_price"]::text')
        # 评论数
        item.add_css('comment_num', 'ul li[class*="line"] p[class="search_star_line"] a[class="search_comment_num"]::text')
        # 作者
        item.add_xpath('author','//ul[@class="bigimg"]/li[contains(@class,"line")]/p[class="search_book_author"]/span[1]/a[1]/text()')
        # 出版社
        item.add_xpath('publish','//ul[@class="bigimg"]/li[contains(@class,"line")]/p[class="search_book_author"]/span[3]/a/text()')
        # 出版时间
        item.add_xpath('p_time','//ul[@class="bigimg"]/li[contains(@class,"line")]/p[class="search_book_author"]/span[2]/text()')

        return item.load_item()
