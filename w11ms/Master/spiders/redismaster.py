from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from w11ms.Master.items import UrlItem

class MasterSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag',]

    """
    class scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor(allow=(), deny=(),
     allow_domains=(), deny_domains=(), deny_extensions=None, restrict_xpaths=(),
      restrict_css=(), tags=('a', 'area'), attrs=('href', ), 
      canonicalize=False, unique=True, process_value=None, strip=True)
    """
    # 标签列表页上所有的标签链接(开始页)  and  进入某一标签后，页面中的详情链接及分页
    links1 = LxmlLinkExtractor(restrict_css=('.tagCol tbody tr td a','.paginator .next a',))
    # 进入最终详情页面
    links2 = LxmlLinkExtractor(allow = "https://book.douban.com/subject/[0-9]+" )
    rules = [
        Rule(links1,callback='parse_directory', follow=True),
        Rule(links2,callback='parse_directory', follow=False),
    ]

    def parse_directory(self, response):
        self.logger.info('in------------------')
        item = UrlItem()
        item['url'] = response.url
        print(item['url'])
        return item
