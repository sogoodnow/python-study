# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.exceptions import IgnoreRequest
import time,random,requests,json


class MasterMiddleware(object):
    def __init__(self,proxy_list=None):
        # 获取代理池
        self.proxy_list = proxy_list
        # 取出最后一个
        if proxy_list:
            self.proxy = "https://"+self.proxy_list.pop()
            with open("./proxy.txt","a+") as file:
                file.write(self.proxy+'\n')
        print("===========>代理连接：", self.proxy)


    @classmethod
    def from_crawler(cls, crawler):
        # 生成实例时初始化代理池
        proxy_url = crawler.settings.get('PROXY_URL')
        proxy_list = requests.get(proxy_url).json()['data']['proxy_list']
        return cls(proxy_list=proxy_list)

    def process_request(self, request, spider):
        request.meta['proxy'] = self.proxy
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        # 错误处理，判断代理池有无代理，没有则重新生成
        if len(self.proxy_list)==0:
            proxy_url = spider.settings.get('PROXY_URL')
            self.proxy_list = requests.get(proxy_url).json()['data']['proxy_list']
        self.proxy = "https://"+self.proxy_list.pop()
        print("===========>新的连接：",self.proxy)
        request.meta['proxy'] =  self.proxy
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
