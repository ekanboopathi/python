from bs4 import BeautifulSoup
import urllib.request

html = 'https://www.quora.com/topic/All-India-Anna-Dravida-Munnetra-Kazhagam-AIADMK-Indian-political-party'
soup = BeautifulSoup(html)
page = urllib.request.urlopen(html)



for a in soup.find_all(class_='question_link', href=True):
    print(f"Found the URL: {a}")
