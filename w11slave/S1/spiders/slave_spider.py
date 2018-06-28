from scrapy_redis.spiders import RedisSpider
from w11slave.S1.items import DoubanItem

class SlaveSpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'slave_redis'
    redis_key = 'master:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(SlaveSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        item = DoubanItem()
        # 书名
        item['bookname'] = str(response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()).strip()
        # 作者
        if response.xpath('//*[@id="info"]/span[contains(text(),"作者:")]/following::a[1]').extract_first():
            item['author'] = ''.join(str(response.xpath('//*[@id="info"]/span[contains(text(),"作者:")]/following::a[1]/text()').extract_first()).strip().split())
        else:
            item['author'] = '无'
        # 出版社
        item['publish'] = str(response.xpath('//*[@id="info"]/span[contains(text(),"出版社:")]/following::text()[1]').extract_first()).strip()
        # 原作名
        if response.xpath('//*[@id="info"]/span[contains(text(),"原作名:")]').extract_first():
            item['originame'] = str(response.xpath('//*[@id="info"]/span[contains(text(),"原作名:")]/following::text()[1]').extract_first()).strip()
        else:
            item['originame'] = '无'
        # 译者
        if response.xpath('//*[@id="info"]/span[contains(text(),"译者:")]').extract_first():
            item['translater'] = str(response.xpath('//*[@id="info"]/span[contains(text(),"译者:")]/following::a[1]/text()').extract_first()).strip()
        else:
            item['translater'] = '无'
        # 出版年
        item['ptime']  = str(response.xpath('//*[@id="info"]/span[contains(text(),"出版年:")]/following::text()[1]').extract_first()).strip()
        # 页数
        item['pages'] = str(response.xpath('//*[@id="info"]/span[contains(text(),"页数:")]/following::text()[1]').extract_first()).strip()
        # 定价
        item['price'] = str(response.xpath('//*[@id="info"]/span[contains(text(),"定价:")]/following::text()[1]').extract_first()).strip()
        # 装帧
        item['zhuangzheng'] = str(response.xpath('//*[@id="info"]/span[contains(text(),"装帧:")]/following::text()[1]').extract_first()).strip()
        # 丛书
        item['books'] = str(response.xpath('//*[@id="info"]/span[contains(text(),"丛书:")]/following::a[1]/text()').extract_first()).strip()
        # isbn
        item['isbn'] = str(response.xpath('//*[@id="info"]/span[contains(text(),"ISBN:")]/following::text()[1]').extract_first()).strip()
        # 评分
        item['starts'] = str(response.css('#interest_sectl .ll.rating_num::text').extract_first()).strip()
        # 评论人数
        item['commentcnt'] = str(response.css('.rating_sum span a span::text').extract_first()).strip()
        # 网址
        item['weburl'] = str(response.url)
        # # 书籍简介
        item['bookintro'] = ''.join(response.css('.related_info #link-report .intro p::text').extract())
        # 作者简介
        item['authorintro'] = ''.join(response.css('.related_info .indent:not(#link-report) .intro p::text').extract())

        # print(item)
        return item
