# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import  pymongo

class BooksPipeline(object):
    collection_name = 'Books_Information'
    def process_item(self, item, spider):
        return item

class MongoDbPipeline(object):
        collection_name = 'Books_Information'

        def open_spider(self,spider):
            self.client = pymongo.MongoClient("mongodb+srv://6QcR7kHMST3Dwuds2Fw6x:test1124@bookscluster-opdpc.mongodb.net/BooksCluster?retryWrites=true&w=majority")
            self.db = self.client['BOOKS']

        def close_spider(self,spider):
            self.client.close()

        def process_item(self,item,spider):
            self.db[self.collection_name].insert(item)
