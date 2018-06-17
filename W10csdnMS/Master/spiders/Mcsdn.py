from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Master.items import CsdnItem

class CsdnSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'csdn'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/courses/']

    """
    class scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor(allow=(), deny=(),
     allow_domains=(), deny_domains=(), deny_extensions=None, restrict_xpaths=(),
      restrict_css=(), tags=('a', 'area'), attrs=('href', ), 
      canonicalize=False, unique=True, process_value=None, strip=True)
    """
    links = LxmlLinkExtractor(allow="/(p[0-9])*$",allow_domains='csdn.net',restrict_css=('.btn.btn-xs.btn-default.btn-next',))
    rules = [
        # 设定爬去规则的‘组’，很重要！
        # 第一组规则：在点击下一页后，爬尾数0-9的页，控制范围
        # 第二组规则：在符合第一组规则的页面上，爬去信息区域链接
        Rule(links,callback='parse_directory', follow=True),
        Rule(LxmlLinkExtractor(restrict_css=('.course_dl_list a',)), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        # for div in response.css('.title-and-desc'):
        #     yield {
        #         'name': div.css('.site-title::text').extract_first(),
        #         'description': div.css('.site-descr::text').extract_first().strip(),
        #         'link': div.css('a::attr(href)').extract_first(),
        #     }
        self.logger.info('in------------------')
        item = CsdnItem()
        item['url'] = response.url
        print(item['url'])
        return item
