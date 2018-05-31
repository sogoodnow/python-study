# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib.parse import urlencode


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.renren.com/']
    start_urls = ['http://www.renren.com']

    def start_requests(self):

        # http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201844168865
        # email = 13951502395 & icode = & origURL = http % 3
        # A % 2
        # F % 2
        # Fwww.renren.com % 2
        # Fhome & domain = renren.com & key_id = 1 & captcha_type = web_login & password = 482
        # c9b45ab50f5659babb10f8203b4f950984db6b007c27275c3c0a51cea86f2 & rkey = 534
        # ea44d0764829b5c7418a7bfa43e5b & f = http % 253
        # A % 252
        # F % 252
        # Fzhibo.renren.com % 252
        # Ftop
        pass


    def parse(self, response):
        pass
