from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json
import os
from bs4 import BeautifulSoup
import requests
import pprint

url=[]
url2=[]
u=[]
n=[]
city=["墨爾本","雪梨","凱恩斯","達爾文","布里斯本","黃金海岸","堪培拉","柏斯","荷巴特","阿德雷德"]

url.append("https://www.tripadvisor.com.tw/Attractions-g255100-Activities-a_allAttractions.true-Melbourne_Victoria.html")
url2.append("https://www.tripadvisor.com.tw/Attractions-g255100-Activities-oa")
u.append("-Melbourne_Victoria.html")
n.append(62)
#<墨爾本>k的迴圈次數(1,62)
url.append("https://www.tripadvisor.com.tw/Attractions-g255060-Activities-a_allAttractions.true-Sydney_New_South_Wales.html")
url2.append("https://www.tripadvisor.com.tw/Attractions-g255060-Activities-oa")
u.append("-Sydney_New_South_Wales.html")
n.append(74)
#<雪梨>k的迴圈次數(1,74)
url.append("https://www.tripadvisor.com.tw/Attractions-g255069-Activities-a_allAttractions.true-Cairns_Cairns_Region_Queensland.html")
url2.append("https://www.tripadvisor.com.tw/Attractions-g255069-Activities-oa")
u.append("-Cairns_Cairns_Region_Queensland.html")
n.append(15)
#<凱恩斯>k的迴圈為(1,15)
url.append("https://www.tripadvisor.com.tw/Attractions-g255066-Activities-a_allAttractions.true-Darwin_Top_End_Northern_Territory.html")
url2.append("https://www.tripadvisor.com.tw/Attractions-g255066-Activities-oa")
u.append("-Darwin_Top_End_Northern_Territory.html")
n.append(11)
#<達爾文>k的迴圈為(1,11)
url.append("https://www.tripadvisor.com.tw/Attractions-g255068-Activities-a_allAttractions.true-Brisbane_Brisbane_Region_Queensland.html")
url2.append("https://www.tripadvisor.com.tw/Attractions-g255068-Activities-oa")
u.append("-Brisbane_Brisbane_Region_Queensland.html")
n.append(35)
#<布里斯本>k的迴圈為(1,35)
url.append("https://www.tripadvisor.com.tw/Attractions-g255337-Activities-a_allAttractions.true-Gold_Coast_Queensland.html")
url2.append("https://www.tripadvisor.com.tw/Attractions-g255337-Activities-oa")
u.append("-Gold_Coast_Queensland.html")
n.append(32)
#<黃金海岸>k的迴圈為(1,32)
url.append("https://www.tripadvisor.com.tw/Attractions-g255057-Activities-a_allAttractions.true-Canberra_Australian_Capital_Territory.html")
url2.append("https://www.tripadvisor.com.tw/Attractions-g255057-Activities-oa")
u.append("-Canberra_Australian_Capital_Territory.html")
n.append(15)
#<堪培拉>k的迴圈為(1,15)
url.append("https://www.tripadvisor.com.tw/Attractions-g255103-Activities-a_allAttractions.true-Perth_Greater_Perth_Western_Australia.html")
url2.append("https://www.tripadvisor.com.tw/Attractions-g255103-Activities-oa")
u.append("-Perth_Greater_Perth_Western_Australia.html")
n.append(21)
#<柏斯>k的迴圈為(1,21)
url.append("https://www.tripadvisor.com.tw/Attractions-g255097-Activities-a_allAttractions.true-Hobart_Greater_Hobart_Tasmania.html")
url2.append("https://www.tripadvisor.com.tw/Attractions-g255097-Activities-oa")
u.append("-Hobart_Greater_Hobart_Tasmania.html")
n.append(14)
#<荷巴特>k的迴圈為(1,14)
url.append("https://www.tripadvisor.com.tw/Attractions-g255093-Activities-a_allAttractions.true-Adelaide_Greater_Adelaide_South_Australia.html")
url2.append("https://www.tripadvisor.com.tw/Attractions-g255093-Activities-oa")
u.append("-Adelaide_Greater_Adelaide_South_Australia.html")
n.append(22)
#<阿德雷德>k的迴圈為(1,22)

A="https://www.tripadvisor.com.tw"


listData=[]
name=[]
c=[]
for j in range(0,10):
    response=requests.get(url[j])
    soup=BeautifulSoup(response.text, 'lxml')
    for i in range(1,40):
        for a in soup.select('div._3W_31Rvp._1nUIPWja.w0-2E2Bi._3F-njzen._2b3s5IMB > section:nth-child('+str(i)+') > div > span > div > div > div._392swiRT > div._3JZh_6Iu > div > div > a:nth-child(1)'):
            listData.append(A+a['href'])
            name.append(a.get_text())
	c.append(city[j])
    for k in range(1,n[j]):
        x=k*30
        response=requests.get(url2[j]+str(x)+u[j])
        soup=BeautifulSoup(response.text, 'lxml')
        for i in range(1,40):
            for a in soup.select('div._3W_31Rvp._1nUIPWja.w0-2E2Bi._3F-njzen._2b3s5IMB > section:nth-child('+str(i)+') > div > span > div > div > div._392swiRT > div._3JZh_6Iu > div > div > a:nth-child(1)'):
                listData.append(A+a['href'])
                name.append(a.get_text())
	    c.append(city[j])

options = webdriver.ChromeOptions()
# options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
options.add_argument("--start-maximized")         #最大化視窗
options.add_argument("--incognito")               #開啟無痕模式
options.add_argument("--disable-popup-blocking ") #禁用彈出攔截

driver = webdriver.Chrome( options = options )
address=[]

for i in listData:
    driver.get(i)
    trash=driver.find_elements(By.CSS_SELECTOR,'div._3RhXfkpP._36DzNAEh')
    if len(trash) > 0:
        for element in trash:
            place = element.find_element(By.CSS_SELECTOR, "div.LjCWTZdN > span:nth-child(2)")
            p=place.text
            address.append(p)
    else:
        address.append('X')
print(address)

import pandas as pd

dic={'name':name,'address':address,'city':city}
df = pd.DataFrame(dic)
df.to_csv('view.csv')