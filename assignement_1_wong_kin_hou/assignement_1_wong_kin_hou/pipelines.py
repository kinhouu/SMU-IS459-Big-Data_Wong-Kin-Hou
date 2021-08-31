# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class Assignement1WongKinHouPipeline:
    # Create Connection
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        # Create Database
        db = self.conn['assignment_1_wong_kin_hou']
        self.collection = db['PC_Game_thread']

    def process_item(self, item, spider):
        # Required to store data in dictionary format in MongoDB
        self.collection.insert(dict(item))
        return item
