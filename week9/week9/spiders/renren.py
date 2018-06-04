# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from urllib.parse import urlencode

import json

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.renren.com/']
    start_urls = ['http://www.renren.com']

    def start_requests(self):
        # 设置登录参数，发起post请求，第一次请求，在所有请求之前
        url = 'http://www.renren.com/ajaxLogin/login?'
        pramas = {'email':'13951502395','password':'qiuguochang2018',
                  'captcha_type':'web_login',
                  'uniqueTimestamp':'201844168865'}
        url = url + urlencode(pramas)
        # 第一次请求完成后调用
        return [Request(url,method='POST',callback=self.parse)]


    def parse(self, response):
        homeUrl = json.loads(response.text)
        homeUrl = homeUrl['homeUrl']
        # 登录成功后，获取页面信息，防止域过滤，dont_filter=True
        return [Request(homeUrl,callback=self.home,dont_filter=True)]

    def home(self,response):
        # 获取登录后，登录用户的名字并打印
        print('in==============')
        # print(response.css('.hd-name a::text').extract_first())
        print(response.css('.hd-name::text').extract_first())


