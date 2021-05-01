import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5")

soup = BeautifulSoup(page.content, 'html.parser')
question_preview = soup.find(id='question_preview')
questions = question_preview.find_all('li')

x = [item.find('strong').get_text().replace('"', '').encode('utf-8') for item in questions]

final_questions = pd.DataFrame(
    {
        'DS': x
    })


print(final_questions)
final_questions.to_csv('DS Questions.csv')