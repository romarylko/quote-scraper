import scrapy

from scrapy_redis.spiders import RedisSpider

from ..items import QuoteItem


class AjaxQuoteSpider(RedisSpider):
    """Spider for crawling quotes from 'quotes.toscrape.com/filter.aspx/'"""
    name = 'ajax_quotes'

    def start_requests(self):
        for url in ('http://quotes.toscrape.com/search.aspx',):
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        authors = [author.replace('\n', '').strip() for author in
                   response.css('select[name*=author] option::text').getall() if '-' not in author]
        viewstate = response.css('input[name="__VIEWSTATE"]::attr(value)').get()

        for author in authors:
            yield scrapy.FormRequest.from_response(
                response=response,
                formdata={'author': author, '__VIEWSTATE': viewstate},
                callback=self.parse_author,
            )

    def parse_author(self, response):
        author = response.css('option[selected]::text').get().replace('\n', '').strip()
        tags = [tag.replace('\n', '').strip() for tag in
                response.css('select[name*=tag] option::text').getall() if '-' not in tag]
        viewstate = response.css('input[name="__VIEWSTATE"]::attr(value)').get()

        for tag in tags:
            yield scrapy.FormRequest.from_response(
                response=response,
                formdata={'author': author, 'tag': tag, '__VIEWSTATE': viewstate},
                callback=self.parse_quote,
            )

    def parse_quote(self, response):
        quote = QuoteItem()
        quote['author'] = response.css('span.author::text').get()
        quote['text'] = response.css('span.content::text').get()
        quote['tags'] = response.css('span.tag::text').getall()
        yield quote
