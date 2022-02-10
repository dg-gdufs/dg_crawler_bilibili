'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-02-10 12:51:08
LastEditors: Renhetian
LastEditTime: 2022-02-10 13:24:28
'''

from config.host_config import OUT_DEFAULT_HOME
from crawler.items import *
from utils.check_util import CheckUtil

class DownloadPipeline:

    def __init__(self) -> None:
        CheckUtil.check_path(OUT_DEFAULT_HOME)
    
    def process_item(self, item, spider):
        with open(OUT_DEFAULT_HOME + '/{}-{}.png'.format(item['id'], item['text']), 'wb') as file:
            file.write(item['content'])
        
        del item['content']
        spider.send_log(1, "表情存储成功 ==> id:<{}>".format(item['id']))
        return item