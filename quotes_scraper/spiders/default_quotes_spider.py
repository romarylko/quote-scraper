import scrapy
from scrapy_redis.spiders import RedisSpider

from ..items import QuoteItem


class DefaultQuoteSpider(RedisSpider):
    """Spider for crawling quotes from 'quotes.toscrape.com/'"""
    name = 'default_quotes'

    def start_requests(self):
        for url in ('http://quotes.toscrape.com',):
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').get()
            item['author'] = quote.css('small.author::text').get()
            item['tags'] = quote.css('a.tag::text').getall()
            yield item

        if response.css('li.next'):
            next_link = response.css('li.next a::attr(href)').get()
            yield response.follow(response.urljoin(next_link), callback=self.parse)
