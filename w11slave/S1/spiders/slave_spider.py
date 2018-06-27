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
        # 取得数据info块所有信息
        # p1_list = response.xpath('//*[@id="info"]/text()').extract()
        p1_list = response.xpath('//span[text()="出版年:"]/following::text()[1]').extract_first()

        print(str(p1_list))
        # # / following::text()[1]
        # for p in p1_list:
        #     print(p)
        #     if str(p).strip() !='':
        #         print(p)


        item = DoubanItem()

        # 书名
        item['bookname'] = response.xpath('//*[@id="wrapper"]/h1/span').extract_first()
        # 作者
        item['author'] = response.css('#info a::text').extract_first()
        # # 出版社
        # item['publish'] = response.xpath('//*[@id="info"]/text()[2]').extract_first()
        # # 原作名
        # item['originame'] = response.xpath('//*[@id="info"]/text()[4]').extract_first()

        # 译者
        # translater = Field()
        # # 出版年
        # ptime = Field()
        # # 页数
        # pages = Field()
        # # 定价
        # price = Field()
        # # 装帧
        # zhuangzheng = Field()
        # # 丛书
        # books = Field()
        # # isbn
        # isbn = Field()
        # # 评分
        # starts = Field()
        # # 评论人数
        # commentcnt = Field()
        return item
