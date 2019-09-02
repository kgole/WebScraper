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
print(URLList)
tuples = []
tuple = {}
for linkCrawl in URLList:
    source = requests.get(linkCrawl)
    plainText = source.text
    soup2 = BeautifulSoup(plainText, 'lxml')
    Unlimitedtalk = 0
    UnlimitedSMS = 0
    #Loop for Smartphone titles
    for eachTitle in soup2.find_all('h1', {'class':'p-confi-cc-smartphone_selection-details-headline'}):

        device_name = eachTitle.text
        #print("Device name:- "+device_name)
        tuple["device_name"] = device_name
        #Loop for Memory
    for eachTitle in soup2.find_all('span', {'class': 'p-confi-memory_picker-size'}):
        device_storage = eachTitle.text.strip(' GB')
        #print("Storage:- "+device_storage)
        tuple["device_storage"] = device_storage
        #Loop for Plan Name
    for eachTitle in soup2.find_all('div', {'class': 'c-panel-headline', 'itemprop': 'name'}):
        plan_name = eachTitle.text.strip('smartmobil.de')
        #print("Plan Name:- "+plan_name)
        tuple["plan_name"] = plan_name
        plan_data = plan_name.strip('LTE ')
        pdata_final = plan_data.strip(' GB')
        tuple["plan_data"] = pdata_final
        #Loop for Monthly Price
    for eachTitle in soup2.find_all('span', {'class': 'c-price-before_decimal'}):
        totalPrice = eachTitle.text
        Monthly_price = totalPrice+".99"
        #print(Monthly_price)
        tuple["Monthly_price"] = Monthly_price

        #Loop for Unlimited Talk
    for eachTitle in soup2.find_all('li', {'class': 'e-tarifbox-bulletpoints-phone'}):
        if "300" in eachTitle.text:
            Unlimitedtalk = False
            UnlimitedSMS = False
            tuple["Unlimited_talk"] = Unlimitedtalk
            tuple["Unlimited_SMS"] = UnlimitedSMS
        else:
            Unlimitedtalk = False
            UnlimitedSMS = True
            tuple["Unlimited_talk"] = Unlimitedtalk
            tuple["Unlimited_SMS"] = UnlimitedSMS

    tuples.append(tuple)
    #print(tuple)


print(tuples)
filename = 'abc.csv'
with open(filename, 'w') as f:
    w = csv.DictWriter(f,['device_name','device_storage','plan_name','plan_data','Monthly_price','Unlimited_talk', 'Unlimited_SMS'])
    w.writeheader()
    for quote in tuples:
        w.writerow(quote)