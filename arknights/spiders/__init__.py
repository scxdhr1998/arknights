# -*- coding:utf-8 -*-
import json
import re

import scrapy
from redis import StrictRedis

from arknights.items import ArknightsItem


class Arknights(scrapy.Spider):
    name = "arknights"
    start_urls = "https://ak.hypergryph.com/user/home"

    def __init__(self):
        self.redis = StrictRedis(host='localhost', port=6379)
        self.userUid = 942402043

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls, method='GET', callback=self.parse, dont_filter=True)

    def parse(self, response):
        userdata = response.xpath('//input[@class="index_input__JggqB"]').extract()
        username = re.search(r'(?<=value=").*?(?=")', userdata[2]).group(0)
        userUid = re.search(r'(?<=value=").*?(?=")', userdata[3]).group(0)
        cookie = eval(self.redis.hget(self.userUid, self.userUid).decode())
        for i in range(1, 4):
            yield scrapy.Request(url="https://ak.hypergryph.com/user/api/inquiry/gacha?page=" + str(i),
                                 cookies=cookie,
                                 method='GET', callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        data = json.loads(response.text)
        cards = data['data']['list']
        for card in cards:
            item = ArknightsItem()
            item['ts'] = card['ts']
            item['chars'] = card['chars']
            yield item

