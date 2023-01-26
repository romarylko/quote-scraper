import scrapy
from scrapy_redis.spiders import RedisSpider

from ..items import QuoteItem


class RandomQuoteSpider(RedisSpider):
    """Spider for crawling quotes from 'quotes.toscrape.com/random/'"""
    name = 'random_quotes'

    def start_requests(self):
        for url in ('http://quotes.toscrape.com/random',):
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').get()
            item['author'] = quote.css('small.author::text').get()
            item['tags'] = quote.css('a.tag::text').getall()
            yield item

        while True:
            yield response.follow(
                url=response.url,
                callback=self.parse,
                dont_filter=True
            )
