# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class snapshotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # table=scrapy.Field()
    name=scrapy.Field()
    fullName=scrapy.Field()
    pageUrl=scrapy.Field()
    description=scrapy.Field()
    doubanRate=scrapy.Field()
    imdbRate=scrapy.Field()

class pageItem(scrapy.Item):
    page=scrapy.Field()
    

class filmItem(scrapy.Item):
    name=scrapy.Field()
    enName=scrapy.Field()
    picUrl=scrapy.Field()
    fullName=scrapy.Field()
    details=scrapy.Field()
    downloadUrl=scrapy.Field()
    description=scrapy.Field()
    doubanRate=scrapy.Field()
    imdbRate=scrapy.Field()
    year=scrapy.Field()
