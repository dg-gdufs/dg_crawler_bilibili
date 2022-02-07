'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-28 16:58:07
LastEditors: Renhetian
LastEditTime: 2022-02-07 23:41:25
'''

import os

command = 'scrapy crawl video_reply -a oid={} -o {}.json'
oid_list = [
    '978659748',
    '936194873',
    '338677252',
    '296219126',
    '253699099',
    '211177715',
    '338402240',
    '850780743',
]

# python scripts/video_reply.py
if __name__ == "__main__":
    for i in oid_list:
        print(command.format(str(i),str(i)))
        os.system(command.format(str(i),str(i)))