'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-28 14:45:08
LastEditors: Renhetian
LastEditTime: 2022-01-28 14:46:34
'''

from crawler.spiders import BaseSpider
from crawler.items import *
from utils.date_util import DateUtil
from scrapy.http.request import Request


class VideoReplySpider(BaseSpider):
    name = 'video_reply'
    start_urls = ['https://www.baidu.com/']