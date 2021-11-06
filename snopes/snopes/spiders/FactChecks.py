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
        links = response.css("body > div > div > div > main > div > div > article > a::attr(href)").extract()
        next_page = response.css(".page-link::attr(href)").extract()
        for link in links:
            link = response.urljoin(link)
            if link not in self.url_set:
                self.url_set.add(link)
                yield scrapy.Request(
                    url=link, headers=self.headers, callback=self.parse_fact_details
                )
        if len(next_page) == 1: # First page has one URL in next_page which is url of next page
            next_page = next_page[0]
        elif len(next_page) == 2: # Page 2 and subsequent pages have 2 URLs for next_page: one URL for previous page and another URL for next page
            next_page = next_page[1]
        if next_page:
            if next_page not in self.url_set:
                self.url_set.add(next_page)
                yield scrapy.Request(
                    url=next_page, headers=self.headers, callback=self.parse
                )
