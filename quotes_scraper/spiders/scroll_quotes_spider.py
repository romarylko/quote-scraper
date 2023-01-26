import json

import scrapy
from scrapy_redis.spiders import RedisSpider

from ..items import QuoteItem


class ScrollQuoteSpider(RedisSpider):
    """Spider for crawling quotes from 'quotes.toscrape.com/scroll/'"""
    name = 'scroll_quotes'

    def start_requests(self):
        for url in ('http://quotes.toscrape.com/api/quotes',):
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        for quote in data.get('quotes'):
            item = QuoteItem()
            item['text'] = quote.get('text')
            item['author'] = quote.get('author').get('name')
            item['tags'] = quote.get('tags')
            yield item

        if data.get('has_next'):
            next_link = f'http://quotes.toscrape.com/api/quotes?page={data.get("page") + 1}'
            yield response.follow(next_link, callback=self.parse)
