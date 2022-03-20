'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-28 14:40:13
LastEditors: Renhetian
LastEditTime: 2022-02-10 13:10:03
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

class EmoteItem(scrapy.Item):
    id = scrapy.Field()
    package_id = scrapy.Field()
    text = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()

class UserInfoItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    face_url = scrapy.Field()
    sign = scrapy.Field()
    level = scrapy.Field()
    medal_name = scrapy.Field()
    medal_level = scrapy.Field()
    # vip为2就是大会员，1是曾经是大会员（？
    vip = scrapy.Field()
    official = scrapy.Field()
    following = scrapy.Field()
    follower = scrapy.Field()
    up = scrapy.Field()
