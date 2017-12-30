# -*- coding: utf-8 -*-
import scrapy
from Kosmetik4less_Bot.items import Kosmetik4LessBotItem


class CatriceSpider(scrapy.Spider):
    name = 'Revolution'
    allowed_domains = ['kosmetik4less.de']
    start_urls = ['https://www.kosmetik4less.de/en/makeup-revolution']

    def parse(self, response):
        item = Kosmetik4LessBotItem()
        item['name'] = response.css("p.product-card__name::text")[0].extract()
        item['img'] = response.css("a.product-card__container img ::attr(data-src)").extract_first()
        yield item
        base_url = "https://www.kosmetik4less.de/en/makeup-revolution?page={}"
#         next_page_url = response.css("li.page-item > a.page-link::attr(href)")[4].extract()
        for i in range(2,16):
            next_page_url = base_url.format(i)
            yield scrapy.Request(url = next_page_url,callback=self.parse)


