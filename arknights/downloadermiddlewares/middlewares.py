import json
import re
import time

import requests
import scrapy
from redis import StrictRedis


class RemoteChromeMiddleware(object):

    def __init__(self):
        self.remote_chrome_interface_proxy = 'http://192.168.200.7:3000/chrome'
        self.remote_chrome_read_timeout = 300
        self.redis = StrictRedis(host='localhost', port=6379)
        self.userUid = 942402043

    # def process_request(self, request, spider):
    #
    #     return scrapy.http.Request(url=request.url,cookies=cookie,dont_filter=True)

    def process_response(self, request, response, spider):
        new_url = "https://ak.hypergryph.com/user/home" if 'redirectTo' in request.url else request.url
        if '登录' in response.text:
            if self.redis.hget(self.userUid, self.userUid):
                cookie = eval(self.redis.hget(self.userUid, self.userUid).decode())
                return scrapy.http.Request(new_url, dont_filter=True,
                                           cookies=cookie, method='GET')
            else:
                new_cookie = self._get_cookies(request.url, request.headers['User-Agent'].decode())
                expires = int(new_cookie.pop("expires"))
                self.redis.hset(self.userUid, self.userUid, json.dumps(new_cookie))
                self.redis.expireat(self.userUid, expires-3600)
                return scrapy.http.Request(new_url, dont_filter=True,
                                           cookies=new_cookie, method='GET')
        return response

    def _get_cookies(self, url, ua):
        result = requests.post(
            self.remote_chrome_interface_proxy,
            json={
                'url': url,
                'ua': ua,
                'timeout': self.remote_chrome_read_timeout,
            },
            timeout=self.remote_chrome_read_timeout,
        )
        if result.status_code == 200:
            chrome_cookies = json.loads(result.text)['cookies']
            chrome_cookies = self._format_cookie(chrome_cookies)
            return chrome_cookies

    @staticmethod
    def _format_cookie(cookies):
        cookie_str = dict()
        for cookie in cookies:
            if cookie['name'] in 'HG_ACCOUNT':
                cookie_str.update({"expires": cookie['expires']})
            c = {cookie['name']: cookie['value']}
            cookie_str.update(c)

        return cookie_str
