from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from w11ms.Master.items import UrlItem

class MasterSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/']

    """
    class scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor(allow=(), deny=(),
     allow_domains=(), deny_domains=(), deny_extensions=None, restrict_xpaths=(),
      restrict_css=(), tags=('a', 'area'), attrs=('href', ), 
      canonicalize=False, unique=True, process_value=None, strip=True)
    """
    # 标签列表页上所有的标签链接
    # links1 = LxmlLinkExtractor(allow=".*?",allow_domains='book.douban.com',restrict_css=('.tagCol tbody tr td a',))
    links1 = LxmlLinkExtractor(restrict_css=('.tagCol tbody tr td a',))
    # links1 = LxmlLinkExtractor(allow="\?view=type&icn=index-sorttags-all",allow_domains='book.douban.com',restrict_css=('.tagCol tbody tr td a',))
    # 进入某一标签后，页面中的详情链接及分页
    links2 = LxmlLinkExtractor(allow_domains='book.douban.com',restrict_css=('.paginator .next a',))
    # 进入最终详情页面
    links3 = LxmlLinkExtractor(allow_domains='book.douban.com',restrict_css=('.subject-list .subject-item .pic .nbg a',))
    rules = [
        Rule(links1,callback='parse_directory', follow=True),
        Rule(links2,callback='parse_directory', follow=True),
        Rule(links2,callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        # for div in response.css('.title-and-desc'):
        #     yield {
        #         'name': div.css('.site-title::text').extract_first(),
        #         'description': div.css('.site-descr::text').extract_first().strip(),
        #         'link': div.css('a::attr(href)').extract_first(),
        #     }
        self.logger.info('in------------------')
        item = UrlItem()
        item['url'] = response.url
        print(item['url'])
        return item
