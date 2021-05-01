from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
# source = requests.get("https://www.dice.com/").text
# soup = BeautifulSoup(source, 'html.parser')
driver = webdriver.Chrome(r'D:\Software\chromedriver_win32\chromedriver.exe')
driver.get('https://www.dice.com/')
driver.maximize_window()
sleep(3)
driver.find_element_by_xpath("//input[@placeholder='Job title, skills or company']").send_keys("SDET")
driver.find_element_by_xpath("//input[@placeholder='Location (zip, city, state)']").send_keys("Orlando")
driver.find_element_by_id("submitSearch-button").click()
url = driver.current_url
# print(url)
totalJobs = 0
# source = requests.get(url)
# sleep(10)
# soup = BeautifulSoup(source.content, 'html.parser')
# print(soup.prettify())
titles = []
companies=[]
locations=[]
jobdescs = []
postdates = []
links = []
driver.get(url)
driver.maximize_window()
sleep(5)
jobs = Select(driver.find_element_by_id("pageSize_2"))
jobs.select_by_visible_text("100")
sleep(5)
# df = pd.DataFrame(columns=["Title", "Location", "Company", "Description"])
try:
    while True:
        all_jobs = driver.find_elements_by_tag_name("dhi-search-card")
        # print(all_jobs)
        for job in all_jobs:
            totalJobs += 1
            result_html = job.get_attribute("innerHTML")
            soup = BeautifulSoup(result_html, 'html.parser')
            # print(soup.prettify())
            # Parse and collect list of links in hrefs
            # print(soup.prettify())
            # Parse and collect list of links in hrefs
            title = soup.find('a', class_='card-title-link bold').text
            titles.append(title)
            # print(title)
            location = soup.find('span', id='searchResultLocation').text
            locations.append(location)
            # print(location)
            company = soup.find('a', class_='ng-star-inserted').text
            companies.append(company)
            # print(company)
            EmployeeType = soup.find('span', attrs={'data-cy': 'search-result-employment-type'}).text
            # print(EmployeeType)
            # jobdesc = soup.find('div', class_='card-description').text.replace('\n', ' ')
            # print(jobdesc)
            for link in soup.findAll('a', class_='card-title-link bold'):
                links.append(link.get('href'))
            # df = df.append({"Title": title, 'Location': location, 'Company': company, 'Description': jobdesc},
                           # ignore_index=True)
        driver.find_element_by_xpath("//a[contains(text(),'»')]").click()
        # print("Clicked")
        sleep(3)
except:
    for link in links:
        #print(link)
        driver.get(link)
        sleep(5)
        jobdes = driver.find_element_by_xpath("//div[@id='jobdescSec']").text
        jobdescs.append(jobdes)
        print(jobdes)
    driver.close()
job_data = pd.DataFrame({'Job Title': titles,
'Company Name': companies,
'Location': locations,
'Description': jobdescs,
})
for item in jobdescs:
    print(item)

job_data.to_csv("dice.csv", index=False)

print("Total jobs Collected = ", totalJobs)