# Fact Checks Crawler
This crawler is developed in Python + Scrapy for crawling [Snopes Fact checks](https://www.snopes.com/fact-check/). The mentioned before url contains some rumors and questionable claims of the day.

***Note: Updates to the Snopes website may break this code. We don't guarantee that the scraper will continue to work in the future, but feel free to post an issue if you run into a problem.***

## Environment
- Python: 3.7.0
- Scrapy: 2.5.1

## Installation Guide
- Clone the repository:
```
git clone https://github.com/mohsenMahmoodzadeh/fact-checks-crawler.git
```

- Create a virtual environment (to avoid conflicts):
```
virtualenv -p python3.7 fcscraper

# this may vary depending on your shell
. fcscraper/bin/activate 
```

- Install the dependencies:
```
pip install -r requirements.txt
```

## Usage Guide
After cloning the repository and install the dependencies, run the command below to crawl the website mentioned above :
```
scrapy crawl FactChecks
```
If you want to store the results of crawling process in a file(a facts.json file for example), then use the following command:
```
scrapy crawl FactChecks -o facts.json
```
The other acceptable output formats in the scrapy are listed [here](https://docs.scrapy.org/en/latest/topics/feed-exports.html).

## Data Scheme
The extracted information are:
- title
- url
- publish date
- rating: The result of whether the rumor is valid or not.
- author name
- category
- claim: A statement or an assertion about the rumor that something is the case, typically without providing evidence or proof.
- content: The body of the rumor(or claim).

## Future Works

- Accelerate the process of crawling with fine-tuning the parameters in [settings.py](https://github.com/mohsenMahmoodzadeh/Fact-Checks-Crawler/blob/master/snopes/snopes/settings.py)

- Improve the scalability and flexibility of the crawler with suitable usage of pipelines (in [pipelines.py](https://github.com/mohsenMahmoodzadeh/Fact-Checks-Crawler/blob/master/snopes/snopes/pipelines.py)) and middlewares (in [middlewares.py](https://github.com/mohsenMahmoodzadeh/Fact-Checks-Crawler/blob/master/snopes/snopes/middlewares.py))

## Contributing
Fixes and improvements are more than welcome, so raise an issue or send a PR!