import scrapy


class CarsSpider(scrapy.Spider):
    name = "cars"
    allowed_domains = ["www.olx.com.br"]
    start_urls = ["https://www.olx.com.br/estado-am?q=carros"]

    def parse(self, response):
        pass
