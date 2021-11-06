# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FactCheckItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    date_published = scrapy.Field()
    rating = scrapy.Field()
    author_name = scrapy.Field()
    category = scrapy.Field()
    claim = scrapy.Field()
    tags = scrapy.Field()
