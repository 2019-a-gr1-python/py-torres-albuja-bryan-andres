# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ProyectoScrapyItem(scrapy.Item):
    nombre = scrapy.Field()
    tipo = scrapy.Field()
    link_detalle = scrapy.Field()
    fecha_lanzamiento = scrapy.Field()
    # file_urls = scrapy.Field()
    # files = scrapy.Field()
