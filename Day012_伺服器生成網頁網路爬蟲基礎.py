# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:07:31 2021

@author: nick
"""


from bs4 import BeautifulSoup
import requests, json

print('-------------------印出樂透開獎號碼-------------------')
url = "http://www.taiwanlottery.com.tw"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")

number = soup.find_all('div', {"class":"contents_box02"})

balls_number = number[2].find_all("div", {"class":"ball_tx ball_yellow"})

storage = []
for i in range(6):
    storage.append(balls_number[i].text)

convert_int_number = list(map(int, storage))
special_number = number[2].find_all("div", {"class":"ball_red"})

print('一般號碼: ', convert_int_number)
print('特別號碼: ', special_number)

print('-------------------印出康是美門市-------------------')

url = 'https://www.cosmed.com.tw/api/getStore.aspx?t=store&c=&d=&s='

resp = requests.get(url)
result = json.loads(resp.text)

for i in result['data']:
    if i['ZipCodeName1'] == '新竹市':
        print(i['StoreID'], ' ', i['StoreNM'])