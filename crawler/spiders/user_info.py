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

class UserInfoSpider(BaseSpider):
    name = 'user_info'
    url1 = 'https://api.bilibili.com/x/space/acc/info?mid={}'
    url2 = 'https://api.bilibili.com/x/relation/stat?vmid={}'
    url3 = 'https://api.bilibili.com/x/ugcpay-rank/elec/month/up?up_mid={}'

    def start_requests(self):
        return Request(self.url1.format(self.mid), callback=self.parse_info)

    def parse_info(self, response):
        js = response.json().get('data')
        if not js:
            return
        
        item = UserInfoItem()
        item['id'] = js.get('mid')
        item['name'] = js.get('name')
        item['sex'] = js.get('sex')
        item['face_url'] = js.get('face')
        item['sign'] = js.get('sign')
        item['level'] = js.get('level')
        item['medal_name'] = js.get('medal',{}).get('medal_name')
        item['medal_level'] = js.get('medal',{}).get('level')
        item['vip'] = js.get('vip',{}).get('type')
        item['official'] = js.get('official',{}).get('title')

        return Request(self.url2.format(item['id']), meta={'item': item}, callback=self.parse_stat)

    def parse_stat(self, response):
        item = response.meta['item']
        js = response.json().get('data')
        if js:
            item['following'] = js.get('following')
            item['follower'] = js.get('follower')
        return Request(self.url3.format(item['id']), meta={'item': item}, callback=self.parse_up)
        
    def parse_up(self, response):
        item = response.meta['item']
        item['up'] = response.json().get('data',{}).get('total_count')
        return item
