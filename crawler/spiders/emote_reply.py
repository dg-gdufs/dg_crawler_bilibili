'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-02-10 12:44:56
LastEditors: Renhetian
LastEditTime: 2022-02-10 13:33:02
'''

from crawler.spiders import BaseSpider
from crawler.items import *
from utils.date_util import DateUtil
from scrapy.http.request import Request

class EmoteSpider(BaseSpider):
    name = 'emote'
    url = 'https://api.bilibili.com/x/emote/package?business=reply&ids={}'
    custom_settings = {
        'ITEM_PIPELINES': {
            'crawler.pipelines.download_pipeline.DownloadPipeline': 300
        }
    }

    def start_requests(self):
        for i in range(1,4):
            yield Request(self.url.format(str(i)))
        for i in range(5,360):
            yield Request(self.url.format(str(i)))

    def parse(self, response):
        js = response.json().get('data',{}).get('packages',[{}])[0].get('emote',[])
        for i in js:
            item = EmoteItem()
            item['id'] = i.get('id')
            item['package_id'] = i.get('package_id')
            item['text'] = i.get('text')
            item['type'] = i.get('type')
            item['url'] = i.get('url')
            yield Request(item['url'], callback=self.parse_content, meta={'item': item})

    def parse_content(self, response):
        item = response.meta['item']
        item['content'] = response.body
        yield item