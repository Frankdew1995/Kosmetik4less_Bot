# -*- coding: utf-8 -*-
import scrapy
from Kosmetik4less_Bot.items import Kosmetik4LessBotItem


class CatriceSpider(scrapy.Spider):
    name = 'Catrice'
    allowed_domains = ['kosmetik4less.de']
    start_urls = ['https://www.kosmetik4less.de/en/catrice']

    def parse(self, response):

        item = Kosmetik4LessBotItem()
        for product in response.css("div.product-card__image.desktop"):
            item['img'] = product.css("img.lazyload::attr(data-src)").extract_first()
            item['name'] = product.css("img.lazyload::attr(alt)")[0].extract()
            yield item

        base_url = "https://www.kosmetik4less.de/en/catrice?page={}"

        for i in range(2, 21):
            next_page_url = base_url.format(i)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

        urls = response.css("a.product-card__container::attr(href)").extract()

        for url in urls:
            yield scrapy.Request(url, callback= self.parse_details)


    def parse_details(self,response):

        item =Kosmetik4LessBotItem()
        item["UPC"] = response.css("p.vertical-middle::text").extract_first()
        yield item

