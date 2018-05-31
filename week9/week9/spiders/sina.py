# -*- coding: utf-8 -*-
import scrapy
from ..items import SinaItem


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        dlist = response.css('.article div.section')
        item = SinaItem()
        for di in dlist:
            # 遍历大分类,第一层
            item['title_first'] = ' '.join(di.css('h2::text').extract())
            print('*'*10+item['title_first']+'*'*10)

            # 第二层标题及链接
            lev2_list = di.css('.clearfix')
            for l2 in lev2_list:
                # 标题
                if l2.css('h3 a::text').extract_first():
                    item['title_second'] = l2.css('h3 a::text').extract_first()
                elif l2.css('h3 span::text').extract_first():
                    item['title_second'] = l2.css('h3 span::text').extract_first()
                elif l2.css('h3::text').extract_first():
                    item['title_second'] = l2.css('h3::text').extract_first()
                # 链接
                if l2.xpath('./h3/a/@href').extract_first():
                    item['link_second'] = l2.xpath('./h3/a/@href').extract_first()
                else:
                    item['link_second'] = ''
                print(' |'*2+item['title_second']+':'+item['link_second'])
                # -----------第三层-----------
                l3_list = l2.css('li')
                for l3 in l3_list:
                    item['title_third'] = l3.css('a::text').extract_first()
                    item['link_third'] = l3.css('a::attr(href)').extract_first()
                    print(' |'*6+item['title_third'] + ':' + item['link_third'])


