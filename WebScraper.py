import csv

import requests
from bs4 import BeautifulSoup, SoupStrainer

URL = "https://www.smartmobil.de/handys"
r = requests.get(URL)
#print(r.content)

soup = BeautifulSoup(r.content, 'lxml')
#print(soup.prettify())

for link in soup.find_all('a', attrs={'class': 'c-button'}):
    print(link.get('href'))




#for link in links:
#    if "Samsung" in link.text:
#        print (link)