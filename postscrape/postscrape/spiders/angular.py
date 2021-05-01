import scrapy
import csv
from selenium import webdriver
from time import sleep


class AngularSpider(scrapy.Spider):
    driver = webdriver.Chrome(r'D:\Software\chromedriver_win32\chromedriver.exe')

    driver.get('https://www.dice.com/')
    driver.maximize_window()
    sleep(3)
    driver.find_element_by_xpath("//input[@placeholder='Job title, skills or company']").send_keys("SDET")
    driver.find_element_by_xpath("//input[@placeholder='Location (zip, city, state)']").send_keys("Orlando")
    driver.find_element_by_id("submitSearch-button").click()
    myurl = driver.current_url
    name = 'angular_spider'
    start_urls = [myurl]

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
        filename = "angular_data.csv"
        with open(filename, 'a+') as f:
            writer = csv.writer(f)
            # Selector for all the names from the link with class 'ng-binding'
            names = self.driver.find_elements_by_css_selector("a.ng-binding")
            for name in names:
                title = name.text
                writer.writerow([title])
        self.log('Saved file %s' % filename)
