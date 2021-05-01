from bs4 import BeautifulSoup
import requests
from numpy import iterable
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import pandas as pd
import csv
try:
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
    df = pd.DataFrame(columns=['AmazonSDETQuestions'])

    sleep(5)
    all_links = driver.find_elements_by_class_name("gs-title")
    for e in all_links:
        hrefList.append(e.get_attribute('href'))

    for href in hrefList:
        if href is not None:
            actualList.append(href)
    actualSet=set(actualList)
    actualList1=list(actualSet)
    questions = []
    for link in actualList1:
        print(link)
        driver.get(link)
        page = requests.get(driver.current_url)
        sleep(5)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(class_="entry-title")
        question_preview = soup.find(class_='entry-content').text
        #questions = question_preview.find_all('p')
        # for item in questions:
        #     x = item.text.replace('\r', '\n').encode('utf-8')
        #     df = df.append({'AmazonSDETQuestions': item}, ignore_index=True)
        file1 = open("AmazonReview.txt", "a", encoding="utf-8")

        # \n is placed to indicate EOL (End of Line)
        file1.write(title.text)
        # for item in questions:
        file1.writelines(question_preview)
        file1.close()  # to change file access modes
except:
    driver.quit()

# print(df)
# df.to_csv('Amazon SDET Questions2.csv')
