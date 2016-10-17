# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs
from firebase import firebase
import requests

class CrcprojectPipeline(object):

    ref=firebase.FirebaseApplication('https://blood-plus.firebaseio.com/', None)
    i=0
    def __init__(self):
        self.file = codecs.open('items.json', 'w', encoding='utf-8')


        

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"     
        self.file.write(line)
        #postId=self.ref.post('Event',json_data)
        requests.put("https://blood-plus.firebaseio.com/Event/"+item['datePub']+".json",line)
        #self.ref.post('Event/'+str(postId)+'/'+str(self.i)+"/title",item["title"])

        return item

