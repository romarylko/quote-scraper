import os
import sys

import django

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'djscrapy.settings'
django.setup()

BOT_NAME = 'quotes_scraper'

SPIDER_MODULES = ['quotes_scraper.spiders']
NEWSPIDER_MODULE = 'quotes_scraper.spiders'

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 8

DOWNLOAD_DELAY = .5
DOWNLOAD_TIMEOUT = 30

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPLASH_URL = os.getenv('SPLASH_URL', 'http://localhost:8050')

ITEM_PIPELINES = {
    'quotes_scraper.pipelines.SaveQuotePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# LOG_FILE = "logs.log"

FEEDS = {
    'quotes_scraper/feeds/%(name)s/%(batch_time)s.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': None,
        'indent': 3,
        'item_export_kwargs': {
            'export_empty_fields': True,
        },
    },
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 15
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
SCHEDULER_PERSIST = True
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_ITEMS_KEY = '%(spider)s:items'
REDIS_START_URLS_KEY = '%(name)s:start_urls'
