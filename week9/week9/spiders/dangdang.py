# -*- coding: utf-8 -*-
import scrapy
from ..items import DangItem
from scrapy.loader import ItemLoader
from scrapy.http import Request


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input']
    page = 1
    def parse(self, response):
        """
        #=======itemloader实现============
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
        item.add_xpath('author','//ul[@class="bigimg"]/li[contains(@class,"line")]/p[@class="search_book_author"]/span[1]/a[1]/text()')
        # 出版社
        item.add_xpath('publish','//ul[@class="bigimg"]/li[contains(@class,"line")]/p[@class="search_book_author"]/span[3]/a/text()')
        # 出版时间
        item.add_xpath('p_time','//ul[@class="bigimg"]/li[contains(@class,"line")]/p[@class="search_book_author"]/span[2]/text()')
        yield item.load_item()
        """

        # =======单item实现============
        for li in response.css('ul li[class*="line"]'):
            item = DangItem()
            # 图片判断
            if li.css('.pic img::attr(data-original)').extract_first():
                item['img_urls'] = li.css('.pic img::attr(data-original)').extract_first()
            else:
                item['img_urls'] = li.css('.pic img::attr(src)').extract_first()
            # 标题
            item['title'] = li.css('p[class="name"] a::attr(title)').extract_first()
            # 详细
            item['detail'] = li.css('p[class="detail"]::text').extract_first()
            # 价格
            item['price'] = li.css('p[class="price"] span[class="search_pre_price"]::text').extract_first()
            # 评论数
            item['comment_num'] = li.css('p[class="search_star_line"] a[class="search_comment_num"]::text').extract_first()
             # 作者
            item['author'] = li.xpath('./p[@class="search_book_author"]/span[1]/a[1]/text()').extract_first()
            # 出版社
            item['publish'] = li.xpath('./p[@class="search_book_author"]/span[3]/a/text()').extract_first()
            # 出版时间
            item['p_time'] = li.xpath('./p[@class="search_book_author"]/span[2]/text()').extract_first()

            yield item

            # 循环收集10页数据
            self.page += 1
            if self.page <= 10:
                next_url = self.start_urls[0]+'&page_index='+str(self.page)
                yield Request(url=next_url,callback=self.parse)


