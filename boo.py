from bs4 import BeautifulSoup

data = []
link_text = "https://www.quora.com/topic/All-India-Anna-Dravida-Munnetra-Kazhagam-AIADMK-Indian-political-party"
soup = BeautifulSoup(link_text)

# for a in soup.find_all('a', href=True, text=True):
#     data.append(a['href'])
#     print(a['href'])

# print(data)