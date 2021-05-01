from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import requests
import pandas as pd
driver = webdriver.Chrome(r'D:\Software\chromedriver_win32\chromedriver.exe')
# driver.get('https://practice.geeksforgeeks.org/explore/?company%5B%5D=Amazon&problemType=full&page=1&sortBy=newest')
driver.get('https://practice.geeksforgeeks.org/explore/?company%5B%5D=Amazon&problemType=functional&page=1&sortBy=newest')
driver.maximize_window()
sleep(10)
elements = []
sleep(5)
dict={}
# load = driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
df = pd.DataFrame(columns=["Title","Problem"])

all_links = driver.find_elements_by_xpath("//a[contains(@href, 'problems')]")

print(len(all_links))
for e in all_links:
   elements.append(e.get_attribute('href'))
for link in elements:
    driver.get(link)
    page = requests.get(driver.current_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    question_title = soup.find('span',class_='problem-tab__name').text
    print(question_title)
    problem_statement = soup.find('div',class_='problem-statement').text
    print(problem_statement)
    df = df.append({"Title": question_title, "Problem": problem_statement}, ignore_index=True)

df = df.to_csv("AmGeekFnal.csv", index=False)
    # file1 = open("myfile.txt", "a",encoding="utf-8")
    #
    # # \n is placed to indicate EOL (End of Line)
    # file1.write(question_title)
    # file1.write(problem_statement)
    # file1.close()  # to change file access modes
    # dict.update({question_title:problem_statement})

# print(dict.keys())
# print(dict.values())
# with open('result.json', 'w') as fp:
#      json.dumps(dict, fp)
# df = pd.DataFrame(columns=["Title","Problem"])
#
# df = df.append({"Title": question_title, "Problem": problem_statement}, ignore_index=True)
#
# df = df.to_csv("AmGeek.csv", index=False)
driver.quit()
