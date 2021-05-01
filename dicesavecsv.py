from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import csv
from selenium.webdriver.common.by import By
import pandas as pd
jobdesc = []
postdate = []
driver = webdriver.Chrome(r'D:\Software\chromedriver_win32\chromedriver.exe')
driver.get('https://www.dice.com/jobs/detail/sdet-isoftech-inc/10114734/6679458?searchlink=search%2F%3Fq%3DSDET%26location%3DOrlando%2C%2520FL%2C%2520USA%26latitude%3D28.5383355%26longitude%3D-81.3792365%26countryCode%3DUS%26locationPrecision%3DCity%26adminDistrictCode%3DFL%26radius%3D30%26radiusUnit%3Dmi%26page%3D1%26pageSize%3D20%26language%3Den&searchId=5b4a19d1-dcff-47cf-9b77-2ed163e877c8')
jobTitle = driver.find_element_by_xpath("//h1[@id='jt']").text
print(jobTitle)
jobCompany = driver.find_element_by_xpath("//li[@class='employer hiringOrganization']/a/span[@id='hiringOrganizationName']").text
print(jobCompany)
jobLocation = driver.find_element_by_xpath("//li[@class='location']").text
print(jobLocation)
post_dates = driver.find_element_by_xpath("//ul[@class='list-inline details']/li[3]/span").text
postdate.append(post_dates)
print(post_dates)

jobdesc_xpath = "//body/div/div[@id='bd']/div/div/div[5]/div[1]"
job_descs = driver.find_element_by_xpath(jobdesc_xpath).text
jobdesc.append(job_descs)
print(jobdesc)
job_data = pd.DataFrame({'Job Title': jobTitle,
'Date': postdate,
'Company Name': jobCompany,
'Location': jobLocation,
'Description': jobdesc,
})
print(job_data.info())
job_data.head()