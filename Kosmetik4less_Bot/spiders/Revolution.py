# -*- coding: utf-8 -*-
import scrapy
from Kosmetik4less_Bot.items import Kosmetik4LessBotItem


class CatriceSpider(scrapy.Spider):
    name = 'Revolution'
    allowed_domains = ['kosmetik4less.de']
    start_urls = ['https://www.kosmetik4less.de/en/makeup-revolution']

    def parse(self, response):
        item = Kosmetik4LessBotItem()
        item['img'] = response.css("a.product-card__container img ::attr(data-src)").extract_first()
        item['name'] = response.css("p.product-card__name::text")[0].extract()
        yield item
        next_page_url = response.css("li.page-item > a.page-link::attr(href)")[4].extract()
        if next_page_url:
            yield scrapy.Request(url = next_page_url,callback=self.parse)


