import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
from time import sleep

URL = "https://www.smartmobil.de/handys"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')


URLList = []
for link in soup.find_all('a', attrs={'class': 'c-button'}):
    eachLink = link.get('href')
    fullURL = "https://www.smartmobil.de"+str(eachLink)
    URLList.append(fullURL)

del URLList[0:2]
#print(URLList)

for linkCrawl in URLList:
    source = requests.get(linkCrawl)
    plainText = source.text
    soup2 = BeautifulSoup(plainText, 'lxml')
    #Loop for Smartphone titles
    for eachTitle in soup2.find_all('h1', {'class':'p-confi-cc-smartphone_selection-details-headline'}):
        device_name = eachTitle.text
        print(device_name)
    #Loop for Memory
    for eachTitle in soup2.find_all('span', {'class': 'p-confi-memory_picker-size'}):
        device_storage = eachTitle.text.strip(' GB')
        print(device_storage)
    #Loop for Plan Name
    for eachTitle in soup2.find_all('div', {'class': 'c-panel-headline', 'itemprop': 'name'}):
        plan_name = eachTitle.text.strip('smartmobil.de')
        print(plan_name)
        plan_data = plan_name.strip('LTE ')
        print(plan_data.strip(' GB'))
    #Loop for Monthly Price

