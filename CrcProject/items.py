# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrcprojectItem(scrapy.Item):

    imgUrl = scrapy.Field()
    title = scrapy.Field()
    content=scrapy.Field()
    datePub=scrapy.Field()

