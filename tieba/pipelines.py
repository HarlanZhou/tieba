# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class TiebaPipeline(object):
    def __init__(self):
        self.file = codecs.open('record.csv', 'w')
        
         
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii = False) + ",\n"#中文按照unicode
        self.file.write(content.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.file.close()#关闭文件
