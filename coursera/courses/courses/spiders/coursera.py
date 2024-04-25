import scrapy


class CourseraSpider(scrapy.Spider):
    name = "coursera"
    allowed_domains = ["www.coursera.org"]
    start_urls = ["https://www.coursera.org/browse?languages=pt"]

    def parse(self, response):
        self.log("Hello World! Scrapy Project")
