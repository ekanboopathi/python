from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


url = "https://www.quora.com/topic/Vellore-Institute-of-Technology-Vellore"
page = urllib.request.urlopen(url) # conntect to website

soup = BeautifulSoup(page, 'html.parser')

question = []
data = soup.find_all(class_='question_link')

for i in data:
    print(i.get_text())
    question.append(i.get_text())

Answer = []
boo = soup.find_all(class_='Answer')

for j in boo:
    if "<a href" in j:
        
    print(j.get_text())
    Answer.append(j.get_text())

# df = pd.DataFrame()
# df['question'] = question
# print(df)
# df.to_csv('questions.csv')