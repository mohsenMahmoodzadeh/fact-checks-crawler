import scrapy
import re
import json
from ..items import FactCheckItem

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
    
    def parse_fact_details(self, response):
        links_in_content = response.css(".single-body a::attr(href)").extract()
        for link in links_in_content:
            if link.startswith("https://www.snopes.com/fact-check/") and (link not in self.url_set):
                self.url_set.add(link)
                yield scrapy.Request(
                    url=link, headers=FactchecksSpider.headers, callback=self.parse_fact_details
                )
    
        raw_claim = response.css("body > div.container.my-3 > div > div.col-12.col-lg-8.mb-3 > main > article > div:nth-child(4) > div.claim-text.card-body::text").extract_first()
        claim = ''
        if raw_claim:
            claim = self.remove_special_chars(raw_claim)

        content = ''
        content_body_list = response.css(".single-body").extract()
        if len(content_body_list):
            content_body = content_body_list[0]
            content = self.remove_html_tags(content_body)
        
        title_raw_text = response.css("body > div.container.my-3 > div > div.col-12.col-lg-8.mb-3 > main > article > header > h1::text").extract_first()
        title = self.remove_special_chars(title_raw_text)

        author_raw_name = response.css("body > div.container.my-3 > div > div.col-12.col-lg-8.mb-3 > main > article > header > ul.list-unstyled.authors.list-unstyled.d-flex.flex-wrap.comma-separated > li > a::text").extract_first()
        author_name = self.remove_special_chars(author_raw_name)

        date_published = response.css("body > div.container.my-3 > div > div.col-12.col-lg-8.mb-3 > main > article > header > ul.list-unstyled.dates.list-unstyled.d-flex.flex-wrap.comma-separated-md > li > time::text").extract_first()

        rating = response.css("body > div.container.my-3 > div > div.col-12.col-lg-8.mb-3 > main > article > div:nth-child(5) > div.card-body > div > div.media-body.d-flex.flex-column.align-self-center > span::text").extract_first()

        url = response.xpath("/html/head/meta[10]/@content").extract_first()
        
        category_raw_name = response.css("body > div.container.my-3 > div > div.col-12.col-lg-8.mb-3 > main > article > nav > div:nth-child(3) > a::text").extract_first()
        category = self.remove_special_chars(category_raw_name)

        tags = response.css("body > div.container.my-3 > div > div.col-12.col-lg-8.mb-3 > main > article > footer > div > a > div > div::text").extract()
        tags = [self.remove_special_chars(t) for t in tags]
        

        item = FactCheckItem()

        item["title"] = title
        item["author_name"] = author_name
        item["date_published"] = date_published
        item["rating"] = rating
        if url:
            item["url"] = url
        if claim:
            item["claim"] = claim
        if content:
            item["content"] = content
        if category:
            item["category"] = category
        if len(tags) != 0:
            item["tags"] = tags

        yield item

    def remove_special_chars(self, string):
        result = re.sub(r'\n', "", str(string))
        result = re.sub(r'\t', "", str(result))

        return result

    def remove_html_tags(self, text):
        clean_script = re.compile('<script[^>]*>[\s\S​]*?</script>')
        clean_image_caption = re.compile('<figcaption[^>]*>[\s\S​]*?</figcaption>')
        clean_iframe = re.compile('<iframe[^>]*>[\s\S​]*?</iframe>')
        clean_all_tags = re.compile('<.*?>')


        text = re.sub(clean_script, '', text)


        text = re.sub(clean_image_caption, '', text)
        text = re.sub(clean_iframe, '', text)
        text = re.sub("[\n]+", " ", text)
        text = re.sub("[\t]+", "", text)


        text = re.sub("[\xa0]+", " ", text)
        return re.sub(clean_all_tags, '', text)
