# -*- coding: utf-8 -*-
import scrapy
from proyecto_scrapy.items import ProyectoScrapyItem

class SpiderItemsSpider(scrapy.Spider):
    name = 'spider_items'
    start_urls = ['http://www.neilgaiman.com/works/Comics/']

    def parse(self, response):
        
        lista_comics = response.css('#inside-content > .one-work')

        for comics in lista_comics:
            titulo = comics.css('.one-work-caption > a::text').extract_first()
            imagenURL = comics.css('.one-work-img > a > img::attr(src)').extract_first()
            imagen = response.urljoin(imagenURL)

            item_comic = ProyectoScrapyItem()
            item_comic['titulo'] = titulo
            item_comic['file_urls'] = [imagen]

            print(item_comic['titulo'])
            print(item_comic['file_urls'])

            yield item_comic
