import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#url = "https://www.smartmobil.de/ajax/handys"
#driver = webdriver.PhantomJS()
#driver.get(url)
#html = driver.page_source.encode('utf-8')
#page_num = 0

#while driver.find_elements_by_css_selector('.ajax_load_groups ajax_show_more'):
#    driver.find_element_by_css_selector('.ajax_load_groups ajax_show_more').click()
#    page_num += 1
#    print("getting page number "+str(page_num))
#    time.sleep(1)

#html = driver.page_source.encode('utf-8')

URL = "https://www.smartmobil.de/ajax/handys"
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

    for eachTitle in soup2.find_all('h1', {'class':'p-confi-cc-smartphone_selection-details-headline'}):
        for eachMemory in soup2.find_all('span', {'class': 'p-confi-memory_picker-size'}):
            for eachPlan in soup2.find_all('div', {'class': 'c-panel-headline', 'itemprop': 'name'}):
                for eachPrice in soup2.find_all('span', {'class': 'c-price-before_decimal'}):
                    for eachUNL in soup2.find_all('li', {'class': 'e-tarifbox-bulletpoints-phone'}):
                    #Loop for Smartphone titles
                        device_name = eachTitle.text
                        #print("Device name:- "+device_name)
                    #Loop for Memory
                        device_storage = eachMemory.text.strip(' GB')
                        #print("Storage:- "+device_storage)
                    #Loop for Plan Name
                        plan_name = eachPlan.text.strip('smartmobil.de')
                        #print("Plan Name:- "+plan_name)
                        plan_data = plan_name.strip('LTE ')
                        pdata_final = plan_data.strip(' GB')
                    #Loop for Monthly Price
                        totalPrice = eachPrice.text
                        Monthly_price = totalPrice+".99"
                    #Loop for Unlimited Talk
                        if "300" in eachUNL.text:
                            Unlimitedtalk = False
                            UnlimitedSMS = False
                        else:
                            Unlimitedtalk = False
                            UnlimitedSMS = True
    #print(device_name+device_storage+plan_name+pdata_final+Monthly_price)
    tuple["device_name"] = device_name
    tuple["device_storage"] = device_storage
    tuple["plan_name"] = plan_name
    tuple["plan_data"] = pdata_final
    tuple["Monthly_price"] = Monthly_price
    tuple["Unlimited_talk"] = Unlimitedtalk
    tuple["Unlimited_SMS"] = UnlimitedSMS
    tuples.append(tuple)
    print(tuple)

#print(tuples)
filename = 'SmartMobilPlans.csv'
with open(filename, 'w') as f:
    w = csv.DictWriter(f, ['device_name', 'device_storage', 'plan_name', 'plan_data', 'Monthly_price', 'Unlimited_talk', 'Unlimited_SMS'])
    w.writeheader()
    for quote in tuples:
        w.writerow(quote)