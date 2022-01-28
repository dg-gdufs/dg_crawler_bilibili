'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-28 14:40:13
LastEditors: Renhetian
LastEditTime: 2022-01-28 15:44:05
'''
# encoding: utf-8

import scrapy


class AckItem(scrapy.Item):
    '''
    丢弃item
    '''
    res = scrapy.Field()

class ReplyItem(scrapy.Item):
    rpid = scrapy.Field()
    oid = scrapy.Field()
    mid = scrapy.Field()
    uname = scrapy.Field()
    level = scrapy.Field()
    content = scrapy.Field()
    ctime = scrapy.Field()
    like = scrapy.Field()
    rcount = scrapy.Field()
    replies = scrapy.Field()
