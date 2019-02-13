# -*- coding: utf-8 -*-

# Scrapy settings for dygod project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dygod'
SPIDER_MODULES = ['dygod.spiders']
NEWSPIDER_MODULE = 'dygod.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dygod (http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

## mongodb settings

MONGO_HOST='mongodb://127.0.0.1:27017/'
MONGO_DB="films"
SNAPSHOT_COLL='snapshots'
FILM_COLL='details'


## redis Settings.

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}




# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html

SPIDER_MIDDLEWARES = {
   'dygod.middlewares.DygodSpiderMiddleware': 543,
   # 'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': True,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'dygod.middlewares.DygodDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {

   'dygod.pipelines.DygodPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 400,
}


USER_AGENT_LIST = ['zspider/0.9-dev http://feedback.redkolibri.com/',
                    'Xaldon_WebSpider/2.0.b1',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Mozilla/5.0 (compatible; Speedy Spider; http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Speedy Spider (Entireweb; Beta/1.3; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.2; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.1; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.0; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Beta/1.0; www.entireweb.com)',
                    'Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Speedy Spider (http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (http://www.entireweb.com)',
                    'Sosospider+(+http://help.soso.com/webspider.htm)',
                    'sogou spider',
                    'Nusearch Spider (www.nusearch.com)',
                    'nuSearch Spider (compatible; MSIE 4.01; Windows NT)',
                    'lmspider (lmspider@scansoft.com)',
                    'lmspider lmspider@scansoft.com',
                    'ldspider (http://code.google.com/p/ldspider/wiki/Robots)',
                    'iaskspider/2.0(+http://iask.com/help/help_index.html)',
                    'iaskspider',
                    'hl_ftien_spider_v1.1',
                    'hl_ftien_spider',
                    'FyberSpider (+http://www.fybersearch.com/fyberspider.php)',
                    'FyberSpider',
                    'everyfeed-spider/2.0 (http://www.everyfeed.com)',
                    'envolk[ITS]spider/1.6 (+http://www.envolk.com/envolkspider.html)',
                    'envolk[ITS]spider/1.6 ( http://www.envolk.com/envolkspider.html)',
                    'Baiduspider+(+http://www.baidu.com/search/spider_jp.html)',
                    'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
                    'BaiDuSpider',
                    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com',
                   ]



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


## redis configs

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Default requests serializer is pickle, but it can be changed to any module
# with loads and dumps functions. Note that pickle is not compatible between
# python versions.
# Caveat: In python 3.x, the serializer must return strings keys and support
# bytes as values. Because of this reason the json or msgpack module will not
# work by default. In python 2.x there is no such issue and you can use
# 'json' or 'msgpack' as serializers.
#SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"

# Don't cleanup redis queues, allows to pause/resume crawls.
#SCHEDULER_PERSIST = True

# Schedule requests using a priority queue. (default)
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'

# Alternative queues.
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# Max idle time to prevent the spider from being closed when distributed crawling.
# This only works if queue class is SpiderQueue or SpiderStack,
# and may also block the same time when your spider start at the first time (because the queue is empty).
#SCHEDULER_IDLE_BEFORE_CLOSE = 10

# Store scraped item in redis for post-processing.

# The item pipeline serializes and stores the items in this redis key.
#REDIS_ITEMS_KEY = '%(spider)s:items'

# The items serializer is by default ScrapyJSONEncoder. You can use any
# importable path to a callable object.
#REDIS_ITEMS_SERIALIZER = 'json.dumps'

# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

