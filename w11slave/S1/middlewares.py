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
    def __init__(self,proxy_url=None):
        # time.sleep(10)
        # 每次生成5个代理【讯代理】
        # {"ERRORCODE": "0", "RESULT": [{"port": "41378", "ip": "182.39.30.90"}, {"port": "49794", "ip": "171.12.138.50"},
        #                               {"port": "30214", "ip": "118.120.184.142"},
        #                               {"port": "48768", "ip": "221.225.136.76"},
        #                               {"port": "46862", "ip": "27.150.118.119"}]}

        self.proxy_list = requests.get(proxy_url).json()['RESULT']

        # 取出最后一个
        proxy = self.proxy_list.pop()
        self.proxy_url = "https://" + proxy['ip'] + ":" + proxy['port']
        print("===========>代理连接：", self.proxy_url)


    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        proxy_url = crawler.settings.get('PROXY_URL')
        s = cls(proxy_url=proxy_url)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.meta['proxy'] = self.proxy_url
        return None

    def process_response(self, request, response, spider):
        # 服务器禁止时，排除链接，设置新的代理并重新爬取
        if "sorry" in str(response.url) :
            raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # 错误处理，判断代理池有无代理，没有则重新生成
        if len(self.proxy_list)==0:
            proxy_url = spider.settings.get('PROXY_URL')
            # 防止获取代理超时，间隔10秒后重新获取
            time.sleep(10)
            self.proxy_list = requests.get(proxy_url).json()['RESULT']
        new_proxy = self.proxy_list.pop()
        self.proxy_url = "https://" + new_proxy['ip'] + ":" + new_proxy['port']
        print("===========>新的连接：",self.proxy_url)
        request.meta['proxy'] = self.proxy_url
        # 返回requeset重新处理
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
