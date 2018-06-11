# -*- coding: utf-8 -*-
from scrapy import signals
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
from selenium.webdriver.chrome.options import Options

class JdSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JdDownloaderMiddleware(object):
    def __init__(self,timeout=None):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.driver.set_page_load_timeout(self.timeout)
        self.driver.set_window_size(1400,700)
        self.wait =WebDriverWait(self.driver,self.timeout)

    def __del__(self):
        self.driver.close()


    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # s = cls()
        # crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return cls(timeout=crawler.settings.get('DRIVER_TIME_OUT'))

    def process_request(self, request, spider):
        self.logger.debug('begin-----------')
        page = request.meta.get('page',1)

        try:
            self.driver.get(request.url)
            if page>1:
                # self.driver.implicitly_wait(5)
                cinput = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".J_bottomPage")))
                submit = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_bottomPage .p-skip .btn")))
                cinput.clear()
                cinput.send_keys(page)
                submit.click()
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.implicitly_wait(2)
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'page')))
                self.wait.until(EC.text_to_be_present_in_element((By.ID,'page_jump_num'),str(page)))
                return HtmlResponse(url=request.url,body=self.driver.page_source,request=request,encoding='utf-8',status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url,request=request,status=500)


