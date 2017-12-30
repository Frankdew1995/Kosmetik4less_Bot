# -*- coding: utf-8 -*-
import scrapy


class CatriceSpider(scrapy.Spider):
    name = 'Catrice'
    allowed_domains = ['kosmetik4less.de']
    start_urls = ['http://kosmetik4less.de/']

    def parse(self, response):
        pass
