# -*- coding: utf-8 -*-
import scrapy
from Kosmetik4less_Bot.items import Kosmetik4LessBotItem


class CatriceSpider(scrapy.Spider):
    name = 'Revolution'
    allowed_domains = ['kosmetik4less.de']
    start_urls = ['https://www.kosmetik4less.de/en/makeup-revolution']

    def parse(self, response):

        item = Kosmetik4LessBotItem()
        for product in response.css("div.product-card__image.desktop"):

            item['img'] = product.css("img.lazyload::attr(data-src)").extract_first()
            item['name'] = product.css("img.lazyload::attr(alt)")[0].extract()
            yield item
            
        for price in response.css("div.product-card__prices"):
            
            item['price'] = price.css("strong.product-card__price::text").extract_first()
            yield item

        base_url = "https://www.kosmetik4less.de/en/makeup-revolution?page={}"

        for i in range(2,16):

            next_page_url = base_url.format(i)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
