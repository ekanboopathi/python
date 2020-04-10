from bs4 import BeautifulSoup
from csv import writer
import urllib.request
import re
import pandas as pd


url = "http://www.quora.com/topic/All-India-Anna-Dravida-Munnetra-Kazhagam-AIADMK-Indian-political-party"
page = urllib.request.urlopen(url) # conntect to website

soup = BeautifulSoup(page, 'html.parser')

question = []
boo= soup.find_all(class_='ui_qtext_rendered_qtext')

for b in boo:
    print(b.get_text())
