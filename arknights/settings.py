# -*- coding: utf-8 -*-

# Scrapy settings for arknights project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'arknights'

SPIDER_MODULES = ['arknights.spiders']
NEWSPIDER_MODULE = 'arknights.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'arknights (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'arknights.middlewares.ArknightsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'arknights.downloadermiddlewares.middlewares.RemoteChromeMiddleware': 543,
}
# headers = {
#    'cookie': '_uab_collina=160706731608821027475838;'
#              ' csrf_token=gSNWi-EQuxuxEoq6DarFeJL6;'
#              ' _ga=GA1.2.145414709.1607067316;'
#              ' _gid=GA1.2.180588982.1607067316;'
#              ' acw_tc=77a7dc1716070769369115079ea7de0f63776c75bf8ed2df0ece221235;'
#              ' HG_ACCOUNT=' + HG_ACCONT + ';'
#              ' _gat=1;'
#              ' u_asec=099%23KAFEmYEKEc5EhGTLEEEEEpEQz0yFZ6VTSXyoG6zcSXvqW6VJSrw7Z6V1D3QTEEjtBKlVjYFET%2FdEsyaStcYTEHIwZbqEjOT2qHGbkfMs%2BwD4kLJqmCXdpwIb06Mqm%2FN4kLjoxYPVWwISqwERvkxd0xEGctgMXREYqLzakjDuzZdY0He6ma2GkL0opQgyy%2FoboaSaAYFExGExbvedCwUQrjDt9yBXHaxdcEPcbdhdcw7B%2BUZVNOeVbLNtay%2FoPwoScblczVZBNs1D3oCPnyIVba47aOCxbyXZNGucbocB6RXZ1uQTEEMFluula3PoE7EIlllbCP8MreabE7EUlllPeliSlllllulJt37IJ9llWLaStEaollle33iS13slluUdt37InNQTEE7EERpCDEFET3llsR4%3D'
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'arknights.pipelines.ArknightsPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
