from scrapy import Spider
# from indeed.items import IndeedItem
from scrapy.selector import Selector
from selenium import webdriver
from scrapy.http import TextResponse
import scrapy


class IndeedSpider(Spider):
    name = 'indeed'

    allowed_domains = ["http://www.dice.com/"]

    s1 = 'https://www.dice.com/jobs/q-data_scientist-limit-30-l-New_York%2C_NY-radius-30-startPage-1-limit-30-jobs?searchid=291607343849'

    start_urls = [s1]

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):

        self.driver.get(response.url)
        urls = []

        for i in range(1, 20):

            response = TextResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8')
            self.driver.implicitly_wait(10)

            for j in range(1, 31):
                result = response.xpath('//*[@class="col-md-9"]/div[1]/div[' + str(j) + ']/h3/a/@href')
                urls.extend(result)

            next_page = self.driver.find_element_by_xpath('//*[@title="Go to next page"]')
            next_page.click()