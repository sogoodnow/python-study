# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.exceptions import IgnoreRequest
import time,random,requests,json


class MasterMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.


    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        time.sleep(10)
        """
        http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=2646d627908f47f2b0c9a6f55246163e&returnType=2&count=1
        
        """
        # proxy_list = requests.get('http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=2646d627908f47f2b0c9a6f55246163e&returnType=2&count=1').json()
        # proxy_list = proxy_list['RESULT']
        # print(proxy_list)
        # proxy = random.choice(proxy_list)
        # proxy_url = "https://"+proxy['ip']+":"+proxy['port']
        # proxy_url = 'https://121.232.167.136:47718'
        # print(proxy_url)
        # request.meta['proxy'] = proxy_url
        # request.meta['proxy'] = 'http://' + pro_addr
        cookies = {}
        with open('../cookies.txt','rb') as file:
            raw_cookies = str(file.read(),encoding='utf-8');
            # print(raw_cookies)
            for line in raw_cookies.split(';'):
                # print(line.split('=',1))
                if line:
                    key,value = line.split('=',1)
                    cookies[key] = value
        # request['Cookie'] = cookies
        request.cookies = cookies

        # Called for each request that goes through the downloader
        # middleware.
        # print('here')
        # request.headers.setdefault('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
        # # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # 服务器禁止时，排除链接，设置新的代理并重新爬取
        if response.status != 200:
            raise IgnoreRequest
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
