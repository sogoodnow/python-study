from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DmozSpider(CrawlSpider):
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
    rules = [
        Rule(LinkExtractor(restrict_css=('.course_dl_list a', )), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        # for div in response.css('.title-and-desc'):
        #     yield {
        #         'name': div.css('.site-title::text').extract_first(),
        #         'description': div.css('.site-descr::text').extract_first().strip(),
        #         'link': div.css('a::attr(href)').extract_first(),
        #     }
        item = self.item
        item['url'] = response.url
        print(item['url'])
        return item
