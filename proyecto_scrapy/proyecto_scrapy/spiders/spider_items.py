# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose
from proyecto_scrapy.items import ProyectoScrapyItem

class SpiderItemsSpider(scrapy.Spider):
    name = 'spider_items'
    start_urls = ['https://www.dccomics.com/comics']

    def parse(self, response):
        
        lista_comics = response.css('.slide__content')

        for comics in lista_comics:
            # nombre = comics.css('.views-field.views-field-title > .field-content > a::text').extract_first()
            # tipo = comics.css('.content-type::text').extract_first()
            # detalleURL = comics.css('.views-field.views-field-title > .field-content > a::attr(href)').extract_first()
            # link_detalle = detalleURL.urljoin(detalleURL)
            # fecha_lanzamiento = comics.css('div > div > .date-display-single::text').extract_first()
            # imagenURL = comics.css('a > img::attr(src)').extract_first()
            # imagen = response.urljoin(imagenURL)

            # item_comic = ProyectoScrapyItem()
            # item_comic['nombre'] = nombre
            # item_comic['tipo'] = tipo
            # item_comic['link_detalle'] = link_detalle
            # item_comic['fecha_lanzamiento'] = fecha_lanzamiento
            # item_comic['file_urls'] = [imagen]

            # print(item_comic['nombre'])
            # print(item_comic['tipo'])
            # print(item_comic['link_detalle'])
            # print(item_comic['fecha_lanzamiento'])
            # print(item_comic['file_urls'])

            # yield item_comic

            comic_loader = ItemLoader(
                item = ProyectoScrapyItem(),
                selector = comics
            )

            comic_loader.default_output_processor = TakeFirst()

            nombre = comic_loader.add_css('nombre', '.views-field.views-field-title > .field-content > a::text')
            tipo = comic_loader.add_css('tipo', '.content-type::text')
            link_detalle = comic_loader.add_css('link_detalle', '.views-field.views-field-title > .field-content > a::attr(href)')
            fecha_lanzamiento = comic_loader.add_css('fecha_lanzamiento', 'div > div > .date-display-single::text')
            # imagenURL = comic_loader.add_css('file_urls', 'a > img::attr(src)')
            # imagen = response.urljoin(imagenURL)

            yield comic_loader.load_item()
