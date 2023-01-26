from scrapy.http import FormRequest

from .default_quotes_spider import DefaultQuoteSpider


class LoginQuoteSpider(DefaultQuoteSpider):
    """Spider for crawling quotes from 'quotes.toscrape.com/login/'"""
    name = 'login_quotes'

    def start_requests(self):
        return (
            FormRequest(
                'http://quotes.toscrape.com/login',
                formdata={'username': 'user', 'password': 'password'},
                callback=self.parse
            ),
        )
