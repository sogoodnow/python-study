from scrapy_redis.spiders import RedisSpider
from S1.items import CsdnItem


class SlaveSpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    redis_key = 'csdn:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(SlaveSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        item = CsdnItem()
        # 标题
        item['title'] = str(response.css('div[class*="info_right"] h1::text').extract_first()).strip()
        # 课时
        item['period'] = str(response.css('.info_right.no_combo .prog .pinfo::text').extract_first()).strip().split('/')[1]
        # 讲师
        item['teacher'] = str(response.css('.professor_box .professor_top .professor_name a::text').extract_first()).strip()
        # 适合人群
        item['people'] =  str(response.css('.forwho .for::text').extract_first()).strip()
        # 学习人数
        item['members'] =  str(response.css('.forwho .howmany .num::text').extract_first()).strip()
        # 价格
        item['price'] =  str(response.css('.sale .money::text').extract_first()).strip()
        # 课程大纲
        # dtlist = response.css('.outL_box dt span::text').extract()
        ls = []
        if len(response.css('.outL_box dt span::text'))==1:
            # item['curriculum'] = response.css('.outL_box dd li .ellipsis::text').extract()
            for i in response.css('.outL_box dd li .ellipsis::text').extract():
                ls.append(str(i).strip())
            item['curriculum'] = ls
        else:
            # item['curriculum'] = response.css('.outL_box dt span::text').extract()
            for i in response.css('.outL_box dt span::text').extract():
                ls.append(str(i).strip())
            item['curriculum'] = ls
        item['curl'] = response.url
        return item
