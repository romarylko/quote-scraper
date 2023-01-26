import os

from celery import shared_task


@shared_task
def parse_quotes_task():
    os.system('scrapy crawl default_quotes')
