from selenium import webdriver
from time import sleep
import csv
import pandas as pd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'D:\Software\chromedriver_win32\chromedriver.exe')
title = []
company=[]
location=[]
jobdesc = []
postdate = []
driver.get('https://www.dice.com/')
driver.maximize_window()
sleep(3)
driver.find_element_by_xpath("//input[@placeholder='Job title, skills or company']").send_keys("SDET")
driver.find_element_by_xpath("//input[@placeholder='Location (zip, city, state)']").send_keys("Orlando")
driver.find_element_by_id("submitSearch-button").click()
url = driver.current_url
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
# for link in links:
#     print(link.text)
sleep(3)
# driver.find_element_by_xpath("//html[1]/body[1]/dhi-js-dice-client[1]/div[1]/dhi-search-page-container[1]/dhi-search-page[1]/div[1]/dhi-search-page-results[1]/div[1]/div[3]/js-search-display[1]/div[1]/div[2]/dhi-search-cards-widget[1]/div[1]/dhi-search-card[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h5[1]/a[1]").click()
driver.find_element_by_xpath("//dhi-search-card[1]//div[1]//div[1]//div[1]//div[2]//div[1]//h5[1]//a[1]").click()
url = driver.current_url
print(url)
jobTitle = driver.find_element_by_xpath("//h1[@id='jt']").text
print(jobTitle)
jobCompany = driver.find_element_by_xpath("//li[@class='employer hiringOrganization']/a/span[@id='hiringOrganizationName']").text
company.append(jobCompany)
print(jobCompany)
jobLocation = driver.find_element_by_xpath("//li[@class='location']").text
location.append(jobLocation)
print(jobLocation)
post_dates = driver.find_element_by_xpath("//ul[@class='list-inline details']/li[3]/span").text
postdate.append(post_dates)
print(post_dates)


jobdesc_xpath = "//body/div/div[@id='bd']/div/div/div[5]/div[1]"
job_descs = driver.find_element_by_xpath(jobdesc_xpath).text
jobdesc.append(job_descs)
print(jobdesc)
driver.back()

# driver.find_element_by_xpath("/html[1]/body[1]/dhi-js-dice-client[1]/div[1]/dhi-search-page-container[1]/dhi-search-page[1]/div[1]/dhi-search-page-results[1]/div[1]/div[3]/js-search-display[1]/div[1]/div[2]/dhi-search-cards-widget[1]/div[1]/dhi-search-card[2]/div[1]/div[1]/div[1]/div[2]/div[1]/h5[1]/a[1]").click()
# # driver.find_element_by_xpath("//dhi-search-card[2]//div[1]//div[1]//div[1]//div[2]//div[1]//h5[1]//a[1]").click()
# url = driver.current_url
# print(url)
# jobTitle = driver.find_element_by_xpath("//h1[@id='jt']").text
# print(jobTitle)
# jobCompany = driver.find_element_by_xpath("//li[@class='employer hiringOrganization']/a/span[@id='hiringOrganizationName']").text
# company.append(jobCompany)
# print(jobCompany)
# jobLocation = driver.find_element_by_xpath("//li[@class='location']").text
# location.append(jobLocation)
# print(jobLocation)
# post_dates = driver.find_element_by_xpath("//ul[@class='list-inline details']/li[3]/span").text
# postdate.append(post_dates)
# print(post_dates)
#
#
# jobdesc_xpath = "//body/div/div[@id='bd']/div/div/div[5]/div[1]"
# job_descs = driver.find_element_by_xpath(jobdesc_xpath).text
# jobdesc.append(job_descs)
# print(jobdesc)
job_data = pd.DataFrame({'Job Title': jobTitle,
'Date': postdate,
'Company Name': jobCompany,
'Location': jobLocation,
'Description': jobdesc,
})
job_data.to_csv("dice.csv")
print(job_data.info())
job_data.head()
print(job_data)

sleep(7)
driver.quit()