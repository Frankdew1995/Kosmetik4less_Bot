# -*- coding: utf-8 -*-
import scrapy
from Kosmetik4less_Bot.items import Kosmetik4LessBotItem


class CatriceSpider(scrapy.Spider):
    name = 'Revolution'
    allowed_domains = ['kosmetik4less.de']
    start_urls = ['https://www.kosmetik4less.de/en/makeup-revolution']

    def parse(self, response):

        urls = response.css("a.product-card__container::attr(href)").extract()

        for url in urls:
            
            
            yield scrapy.Request(url =url, callback = self.parse_details)


        base_url = "https://www.kosmetik4less.de/en/makeup-revolution?page={}"

        for i in range(2,16):

            next_page_url = base_url.format(i)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
            
    def parse_details(self, response):
        item = Kosmetik4LessBotItem()
        item['img'] = response.css("img.product-image::attr(src)").extract_first()
        item['price'] = response.css('span.h1::text').extract_first()
        item['name'] = response.css("h1::text").extract_first()
        yield item
        

        
        
        
        
