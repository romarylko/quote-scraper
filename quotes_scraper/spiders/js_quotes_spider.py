import scrapy

from scrapy_splash import SplashRequest

from ..items import QuoteItem


class JsQuoteSpider(scrapy.Spider):
    """Spider for crawling quotes from 'quotes.toscrape.com/js/'"""
    name = 'js_quotes'

    def start_requests(self):
        for url in ('http://quotes.toscrape.com/js/',):
            yield SplashRequest(url, callback=self.parse)

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').get()
            item['author'] = quote.css('small.author::text').get()
            item['tags'] = quote.css('a.tag::text').getall()
            yield item

        if response.css('li.next'):
            next_link = response.css('li.next a::attr(href)').get()
            yield SplashRequest(response.urljoin(next_link), callback=self.parse)

