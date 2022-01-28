'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-28 16:58:07
LastEditors: Renhetian
LastEditTime: 2022-01-28 17:31:31
'''

import os

command = 'scrapy crawl video_reply -a oid={} -o {}.json'
oid_list = [
    '423296628',
    '586332404',
    '543771521',
    '458538559',
    '373561162',
    '331263647',
    '628839901',
    '78976165',
    '36570401',
    '20205649',
    '17027625',
    '8507227',
    '8506545',
    '8113240',
    '7248433',
    '3905487',
    '3905428',
    '3521416',
    '3485833',
    '3478616',
    '3396823',
    '1999286',
    '1966343',
    '936918',
    '936916',
    '936732',
    '468560',
    '465235',
    '465230',
    '465224',
    '465222',
    '203614',
    '55300',
    '2313',
]

# python scripts/video_reply.py
if __name__ == "__main__":
    for i in oid_list:
        print(command.format(str(i),str(i)))
        os.system(command.format(str(i),str(i)))