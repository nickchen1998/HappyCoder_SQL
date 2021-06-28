# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:08:28 2021

@author: nick
"""


from selenium import webdriver
from bs4 import BeautifulSoup as soup
import pandas as pd
import time


def get_data(result):
    while True:
        #判斷是否為第一頁
        if len(result) == 0:
            page_content = driver.page_source
            index_result = soup(page_content, 'lxml')
            case_title = index_result.find_all(class_='title')

            for i in range(len(case_title)):
                result.append([])
                result[i].append(case_title[i].find('a').text)
                result[i].append(index_result.find_all(class_='budget')[i].text)
                result[i].append(index_result.find_all(class_='update')[i].text)
                result[i].append(index_result.find_all(class_='casedesc')[i].text)

        #從第二頁開始要進行的
        else:
            #判斷是否為最後一頁，因最後一頁沒有下一頁按鈕，若嘗試去 fidn_element_by_class_name 會產生錯誤因此使用例外判斷是否為最後一頁
            try:
                #製作點擊下一頁標籤的程式
                nextpage_btn = driver.find_element_by_class_name('goNext')
                nextpage_btn.click()
                #等待畫面讀取完畢
                time.sleep(3)
                page_content = driver.page_source
                index_result = soup(page_content, 'lxml')
                case_title = index_result.find_all(class_='title')      

                for i in range(len(case_title)):
                    result.append([])
                    result[len(result)-1].append(case_title[i].find('a').text)
                    result[len(result)-1].append(index_result.find_all(class_='budget')[i].text)
                    result[len(result)-1].append(index_result.find_all(class_='update')[i].text)
                    result[len(result)-1].append(index_result.find_all(class_='casedesc')[i].text)
            except:
                break

    return(result)

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.tasker.com.tw/casepage-index.html?srh=KWCC30MMTA7MM')

result = []
get_data(result)

#將瀏覽器關閉避免資源浪費
driver.quit()

#開始利用 pandas 進行資料處理
#製作欄標籤
columns = ['提案標題', '提案預算', '提案時間', '提案說明']

#製作列標籤
indexs = []
for i in range(len(result)):
    indexs.append("第 {} 筆".format(i+1))

df = pd.DataFrame(result, columns=columns, index=indexs)