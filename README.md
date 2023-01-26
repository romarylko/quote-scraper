# Quotes scraper

## Features
- 7 spiders for crawling quotes from http://toscrape.com/
- Daily running spiders at 11am and 11pm
- DRF API for crawled quotes
- Redis as a caching layer

## List of spiders
- default_quotes 
- scroll_quotes 
- js_quotes 
- table_quotes 
- random_quotes 
- login_quotes 
- ajax_quotes 

## Requirements

1. [Docker](https://docs.docker.com/install/)
2. [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

Set SPLASH_ULR in .env file with your ip address:

```text
SPLASH_URL='http://YOUR_IP_ADDRESS:8050'
```

## How to run it?
1. Build the application:
```sh
docker-compose build
```

2. Run the application:
```sh
docker-compose up -d
```

## How to run a specific spider?
```sh
docker-compose exec app scrapy crawl spider_name
```

## How to run tests?
```sh
python manage.py test quotes
```