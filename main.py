from bs4 import BeautifulSoup
import urllib.request 
import pandas as pd
import re
ip=input("Enter Comparison:").replace(" ","+").strip()
url = f"https://www.quora.com/search?q={ip}"
print(url)
page = urllib.request.urlopen(url) # conntect to website

soup = BeautifulSoup(page, 'html.parser')

# question = []
# data = soup.find_all(class_='question_link')

# # for i in data:
# #     # print(i.get_text())

# boo = soup.find_all(class_='Answer')

# for j in boo:
#     # print(j.get_text())
#     question.append(j.get_text())

# df = pd.DataFrame()
# df['question'] = question
# # print(df)
# df.to_csv('questions.csv')

# Question href value
questionhref = soup.find_all(class_='question_link')

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Extracting URLs from the attribute href in the <a> tags.
for tag in questionhref:
    qsurl = f"https://www.quora.com{tag.get('href')}"
    print(f"question:{qsurl}")
    pg = urllib.request.urlopen(qsurl)
    sp = BeautifulSoup(pg, 'html.parser')
    answerdata = sp.find_all(class_='ui_qtext_rendered_qtext')
    data = remove_html_tags(str(answerdata))
    print(data)






