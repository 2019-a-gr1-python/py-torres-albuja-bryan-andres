# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class ValidarComic(object):
    def process_item(self, item, spider):
        if('Comic Book' not in item['tipo']):
            raise DropItem()

        return item

class ValidarAntiguedad(object):
    def process_item(self, item, spider):
        numero_comic = item['nombre'].split('#')

        if(int(numero_comic[1]) > 50):
            item['nombre'] = 'Serie continua'

            raise DropItem()

        return item

class MarcarComoNuevaSerie(object):
    def process_item(self, item, spider):
        if item['nombre'] != 'Serie continua' and item['tipo'] != 'Graphic Novel':
            print('\nItem encontrado:')
            print('Nombre: ', item['nombre'])
            print('Tipo: ', item['tipo'])
            print('Detalle: ', item['link_detalle'])
            print('\n')

        return item
        