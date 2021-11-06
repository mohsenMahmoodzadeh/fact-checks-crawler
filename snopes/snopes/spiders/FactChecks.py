import scrapy


class FactchecksSpider(scrapy.Spider):
    name = 'FactChecks'
    allowed_domains = ['http://www.snopes.com/fact-check']
    start_urls = ['http://http://www.snopes.com/fact-check/']

    def parse(self, response):
        pass
