

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import PIL.ImageGrab


driver=webdriver.Chrome()
driver.maximize_window()
from selenium.webdriver.common.by import By

import pandas

import time
data=pandas.read_excel('Untitled spreadsheet.xlsx')
data1=[]
data2=[]
data3=[]
data4=[]


    

for i in data['a'].to_list():
    data1.append(i)
    print(i)

for j in data['url'].to_list():
    data2.append(j)


for l in range(5809):
    
    


    

    try:
        driver.get(data2[l])
    except:
        continue

    time.sleep(2)
    im = PIL.ImageGrab.grab()
    
    im.save('{}.png'.format(data1[l]))
    

    
            
                
        


    



