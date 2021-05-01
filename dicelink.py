from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import pandas as pd
driver = webdriver.Chrome(r'D:\Software\chromedriver_win32\chromedriver.exe')
driver.get('https://www.dice.com/')
driver.maximize_window()
sleep(3)
driver.find_element_by_xpath("//input[@placeholder='Job title, skills or company']").send_keys("SDET")
driver.find_element_by_xpath("//input[@placeholder='Location (zip, city, state)']").send_keys("Orlando")
driver.find_element_by_id("submitSearch-button").click()
url = driver.current_url
print(url)
totalJobs = 0
links = []
driver.get(url)
driver.maximize_window()
sleep(3)
jobs = Select(driver.find_element_by_id("pageSize_2"))
jobs.select_by_visible_text("100")
sleep(7)
# all_jobs = driver.find_elements_by_tag_name("dhi-search-card")
# # print(all_jobs)
# for job in all_jobs:
#     totalJobs += 1
#     result_html = job.get_attribute("innerHTML")
#     soup = BeautifulSoup(result_html, 'html.parser')
#     # print(soup.prettify())
#     # Parse and collect list of links in hrefs
#     for link in soup.findAll('a', class_='card-title-link bold'):
#         links.append(link.get('href'))
# for link in links:
#     print(link)
df = pd.DataFrame(columns=["Title", "Location", "Company", "Description"])
try:
    while True:
        all_jobs = driver.find_elements_by_tag_name("dhi-search-card")
        # print(all_jobs)
        for job in all_jobs:
            totalJobs += 1
            result_html = job.get_attribute("innerHTML")
            soup = BeautifulSoup(result_html, 'html.parser')
            # print(soup.prettify())
            title = soup.find('a', class_='card-title-link bold').text
            # print(title)
            location = soup.find('span', id='searchResultLocation').text
            # print(location)
            company = soup.find('a', class_='ng-star-inserted').text
            # print(company)
            # Parse and collect list of links in hrefs
            df = df.append({"Title": title, 'Location': location, 'Company': company})
            for link in soup.findAll('a', class_='card-title-link bold'):
                links.append(link.get('href'))

        driver.find_element_by_xpath("//a[contains(text(),'»')]").click()
        print("Clicked")
        sleep(3)
except:
    for link in links:
        #print(link)
        driver.get(link)
        # sleep(3)
        # jobdesc_xpath = "//body/div/div[@id='bd']/div/div/div[5]/div[1]"
        # job_descs = driver.find_element_by_xpath(jobdesc_xpath).text
        # df.append({'Description': job_descs})

    driver.quit()

df = df.to_csv("dice.csv", index=False)