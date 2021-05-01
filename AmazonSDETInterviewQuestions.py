from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import pandas as pd
import csv
def write_to_csv(qnlist):
    with open('Amazon SDET Questions.csv', mode='a+', encoding='utf-8') as qns:
        jobs_writer = csv.writer(qns, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_MINIMAL)
        jobs_writer.writerow([qnlist])


driver = webdriver.Chrome(r'D:\Software\chromedriver_win32\chromedriver.exe')
driver.get('https://www.geeksforgeeks.org/')
driver.maximize_window()
sleep(3)
driver.find_element_by_xpath("//input[@name = 'search']").send_keys("Amazon SDET Interview Questions")
driver.find_element_by_xpath("//button[@class='gsc-search-button gsc-search-button-v2']").click()
sleep(2)
url = driver.current_url
print(url)
hrefList = []
actualList = []

sleep(5)
all_links = driver.find_elements_by_class_name("gs-title")
for e in all_links:
    hrefList.append(e.get_attribute('href'))

for href in hrefList:
    if href is not None:
        actualList.append(href)
questions = []
p=[]
for link in actualList:
    driver.get(link)
    sleep(10)
    texts = []
    text1 = driver.find_elements_by_tag_name('p')
    plen = len(text1)
    print(plen)
    for each in text1:
        #print(each.text)
        texts.append(each.text)
    write_to_csv(texts)

#
#
# driver.get("https://practice.geeksforgeeks.org/explore/?company%5B%5D=Amazon&problemType=full&page=1")
# driver.maximize_window()
#
# sleep(2)

driver.quit()