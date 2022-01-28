'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-28 16:52:30
LastEditors: Renhetian
LastEditTime: 2022-01-28 16:57:32
'''

from scrapy.http.request import Request
from crawler.spiders.video_reply import VideoReplySpider


class UserVideoReply(VideoReplySpider):
    name = 'user_video_reply'

    def start_requests(self):
        pass