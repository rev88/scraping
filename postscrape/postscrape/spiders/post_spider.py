import scrapy
import csv
from selenium import webdriver
class postSpider(scrapy.Spider):
    name = "posts"
    start_urls = ['https://www.dice.com/jobs?q=SDET&location=Orlando&radius=30&radiusUnit=mi&page=1&pageSize=20']

    # Initalize the webdriver
    def __init__(self):
        self.driver = webdriver.Chrome(r'D:\Software\chromedriver_win32\chromedriver.exe')

    # Parse through each Start URLs
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Parse function: Scrape the webpage and store it
    def parse(self, response):
        self.driver.get(response.url)
        # Output filename
        filename = "angular_data.txt"
        with open(filename, 'wb') as f:
            f.write(response.body)
            # writer = csv.writer(f)
            # # Selector for all the names from the link with class 'ng-binding'
            # names = self.driver.find_elements_by_class_name("card-title-link bold viewed")
            # for name in names:
            #     title = name.text
            #     writer.writerow([title])
        self.log('Saved file %s' % filename)
