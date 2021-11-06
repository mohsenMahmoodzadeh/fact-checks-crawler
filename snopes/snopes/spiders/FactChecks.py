import scrapy


class FactchecksSpider(scrapy.Spider):
    name = 'FactChecks'
    allowed_domains = ['http://www.snopes.com']
    start_urls = ['http://http://www.snopes.com/fact-check/']
    url_set = set({"https://www.snopes.com/fact-check/"})
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0"
    }

    def parse(self, response):
        pass
