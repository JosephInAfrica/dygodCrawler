# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo
from items import filmItem,snapshotItem
# 这里
class DygodPipeline(object):
    # collection_name='film_items'

    # @classmethod 
    # def from_crawler(cls,crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE','items')
    #     )

    def __init__(self):
        self.snapshot_coll=pymongo.MongoClient(host=settings['MONGO_HOST'])[settings['MONGO_DB']][settings['SNAPSHOT_COLL']]
        self.film_coll=pymongo.MongoClient(host=settings['MONGO_HOST'])[settings['MONGO_DB']][settings['FILM_COLL']]

        # self.mongo_db=self.mongo_client[settings['MONGO_DB']]
        # self.coll=self.mongo_db[settings['MONGO_COLL']]



    def process_item(self,item,spider):
        if type(item)==snapshotItem:
            itemToSave=dict(name=item['name'],pageUrl=item['pageUrl'])
            self.snapshot_coll.insert(itemToSave)
        elif type(item)==filmItem:

            itemToSave=dict(name=item['name'],picUrl=item['picUrl'],downloadUrl=item['downloadUrl'],details=item['details'])
            self.film_coll.insert(itemToSave)
        return item