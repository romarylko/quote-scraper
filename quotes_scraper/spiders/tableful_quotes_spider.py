import re

import scrapy
from scrapy_redis.spiders import RedisSpider

from ..items import QuoteItem


class TableQuoteSpider(RedisSpider):
    """Spider for crawling quotes from 'quotes.toscrape.com/tableful/'"""
    name = 'table_quotes'

    def start_requests(self):
        for url in ('http://quotes.toscrape.com/tableful/',):
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        for tag_link in response.css('td[style*="padding-left: 50px;"] a::attr(href)').getall():
            url = response.urljoin(url=tag_link)
            yield response.follow(url=url, callback=self.parse_quote)

    def parse_quote(self, response):
        tag_list = []
        data_list = []

        for row in response.css('tr'):
            tags = row.css('td[style*="padding-bottom: 2em;"] a::text').getall()
            data = row.css('td[style*="padding-top: 2em;"]::text').get()
            if tags:
                tag_list.append(tags)
            if data:
                data_list.append(data)
        quotes = zip(data_list, tag_list)

        for quote in quotes:
            item = QuoteItem()
            data, tags = quote
            text = re.findall(r'“.+”', data)
            author = re.findall(r'Author: (.+)', data)
            item['text'] = text[0] if author else None
            item['author'] = author[0] if author else None
            item['tags'] = tags
            yield item
