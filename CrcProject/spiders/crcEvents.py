#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from CrcProject.items import CrcprojectItem 
from scrapy import Selector
import re


class CrcEventSpider(scrapy.Spider):

    name = "CrcEvent"
    allowed_domains = ["icrc.org"]
    start_urls = [
        "https://www.icrc.org/en/resource-centre/result?context=q%253Dcorporate%25252Ftree%25253A%252522Top%25252Ftopic%25252FAbout%252Bthe%252BICRC%25252FThe%252BMovement%252522%2526b%253D14%2526s%253Dlastmodifieddate%2526sa%253D0%2526hf%253D7%2526logic%253Dinternet-eng&b=0&s=lastmodifieddate&sa=0",
    ]
   

    def elem_ev_generator(self,response):
        for element in  response.xpath('//li[@class="result clearfix"]'):
            yield element
          

    def parse(self, response):
        for element in  self.elem_ev_generator(response):
            item = CrcprojectItem()
            img=element.xpath('a/div[@class="media-object"]/img/@src').extract()
            if(len(img)>0):
                item['imgUrl'] =response.urljoin(img[0])
            else:
                item['imgUrl'] =''
            item['title'] =(element.xpath('a/h3[@class="h6 small-margin-bottom"]/text()').extract()[0]).replace("\n","")
            item['datePub']=element.xpath('a/div/div[@class="result__sub"]/time/text()').extract()[0]
            url = response.urljoin(element.xpath('a/@href').extract()[0])
            request=scrapy.Request(url, callback=self.parse_article_contents)
            request.meta['event']=item
            yield request

    def parse_article_contents(self,response):
        item=response.meta['event']
        tableofContent=response.xpath('//p/text()').extract()
        finalContent=""
        for content in tableofContent:
            finalContent=finalContent+" "+re.sub(' +',' ',content)

        item['content'] =finalContent.replace("\n", "")
        yield item