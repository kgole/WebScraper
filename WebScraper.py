import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
from time import sleep

URL = "https://www.smartmobil.de/handys"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'lxml')


URLList = []
for link in soup.find_all('a', attrs={'class': 'c-button'}):
    link2 = link.get('href')
    fullURL = "https://www.smartmobil.de"+str(link2)
    URLList.append(fullURL)

del URLList[0:2]
print(URLList)
