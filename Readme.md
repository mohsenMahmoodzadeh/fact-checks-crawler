# Fact Checks Crawler
This crawler is developed in Python and Scrapy for crawling [Snopes Fact checks](https://www.snopes.com/fact-check/). The mentioned before url contains some rumors and questionable claims of the day. The extracted informations are:
- title
- url
- publish date
- rating: The result of whether the rumor is valid or not.
- author name
- category
- claim: A statement or an assertion about the rumor that something is the case, typically without providing evidence or proof.
- content: The body of the rumor(or claim).

## Environment
- Python: 3.9.1
- Scrapy: 2.5.1

## Setup Guide
Clone the repository:
> git clone https://github.com/mohsenMahmoodzadeh/Fact-Checks-Crawler.git

Install the dependencies:
> pip install -r requirements.txt

## Usage Guide
After cloning the repository and install the dependencies, run the command below to crawl the website mentioned above :
> scrapy crawl FactChecks

If you want to store the results of crawling process in a file(a *.json file for example), then use the following command:
> scrapy crawl FactChecks -o <output_file_name>.json

The other acceptable output formats in the scrapy are listed [here](https://docs.scrapy.org/en/latest/topics/feed-exports.html). 