'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-28 14:45:08
LastEditors: Renhetian
LastEditTime: 2022-01-28 16:35:55
'''

from crawler.spiders import BaseSpider
from crawler.items import *
from utils.date_util import DateUtil
from scrapy.http.request import Request


class VideoReplySpider(BaseSpider):
    name = 'video_reply'
    reply_url = 'https://api.bilibili.com/x/v2/reply/main?type=1&oid={}&mode={}&next={}'
    reply_reply_url = 'https://api.bilibili.com/x/v2/reply/reply?pn={}&type=1&oid={}&root={}'
    
    def start_requests(self):
        meta = {'oid': self.oid, 'mode': 1, 'next': 0}
        yield Request(self.reply_url.format(self.oid, 1, 0), callback=self.parse_reply, meta=meta)

    def parse_reply(self, response):
        js = response.json()

        for i in js.get('data',{}).get('replies',[]):
            item = ReplyItem()
            item['rpid'] = i.get('rpid')
            item['oid'] = i.get('oid')
            item['mid'] = i.get('mid')
            item['uname'] = i.get('member',{}).get('uname')
            item['level'] = i.get('member',{}).get('level_info',{}).get('current_level')
            item['content'] = i.get('content',{}).get('message')
            item['ctime'] = i.get('ctime')
            item['like'] = i.get('like')
            item['rcount'] = i.get('rcount')
            item['replies'] = []
            self.send_log(1, "评论获取成功 ==> rpid:<{}>".format(item['rpid']))

            response.meta['item'] = item
            response.meta['root'] = item['rpid']
            response.meta['pn'] = 1
            yield Request(self.reply_reply_url.format(1, response.meta['oid'], response.meta['root']), 
                            callback=self.parse_reply_reply, 
                            meta=response.meta)

        response.meta['next'] = js.get('data',{}).get('cursor',{}).get('next')
        if response.meta['next'] != 0:
            yield Request(self.reply_url.format(response.meta['oid'], response.meta['mode'], response.meta['next']), 
                            callback=self.parse_reply, 
                            meta=response.meta)

    def parse_reply_reply(self, response):
        js = response.json()

        if js.get('data',{}).get('replies'):
            for i in js['data']['replies']:
                item = {}
                item['rpid'] = i.get('rpid')
                item['mid'] = i.get('mid')
                item['uname'] = i.get('member',{}).get('uname')
                item['level'] = i.get('member',{}).get('level_info',{}).get('current_level')
                item['content'] = i.get('content',{}).get('message')
                item['ctime'] = i.get('ctime')
                item['like'] = i.get('like')
                response.meta['item']['replies'].append(item)
                self.send_log(1, "评论获取成功 ==> rpid:<{}>".format(item['rpid']))
            
            response.meta['pn'] += 1
            yield Request(self.reply_reply_url.format(response.meta['pn'], response.meta['oid'], response.meta['root']), 
                            callback=self.parse_reply_reply, 
                            meta=response.meta)
        else:
            yield response.meta['item']
