
from bs4 import BeautifulSoup
import pandas
import requests
import time
import urllib.request
from selenium import webdriver






url='https://h-metrics.com/project/onedollarinvest.net/?fbclid=IwAR0c0j2nfACNpx8EsP-grhaQV17VvX-_YgAlYfzNyPp9KOb3RfhSb-6GYlQ'

res=urllib.request.urlopen(url)

soup=BeautifulSoup(res,'lxml')
rows=soup.find_all('tr',class_="item curp show-monitor-det")
data=[]
for row in rows:
    all_row=row.text.replace('\n','').split('   ')
    data.append(all_row)
for dat in data:

    reso=dat[0]
    wbsite=dat[10].replace(' ','')
    added=dat
    
    print(wbsite)
    
