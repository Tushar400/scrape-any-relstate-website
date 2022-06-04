
from selenium import webdriver

import undetected_chromedriver as uc

import pandas as pd

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome( chrome_options=options)
options.add_argument("--headless")
driver.maximize_window()
data1=[]
data2=[]
data3=[]
data4=[]
data5=[]


data=pd.read_csv('kkkkkkk.csv')
for i in data['Marke'].to_list():
    data1.append(i)
for j in data['Plz'].to_list():
    data2.append(j)
for k in data['Ort'].to_list():
    data3.append(k)
for h in data['ID'].to_list():
    data5.append(h)

for l in range(16702)[9664:10664]:
    try:
        value=data1[l]+data2[l]+data3[l]
    except:
        value=' '
    driver.get('https://www.google.com')
    da=[]
    
    driver.find_element(By.XPATH,'//input[@class="gLFyf gsfi"]').send_keys(value)
    driver.find_element(By.XPATH,'//input[@class="gNO89b"]').submit()
    try:
        
        
        links=driver.find_element(By.XPATH,'//div[@class="v7W49e"]').find_elements(By.TAG_NAME,'a')
        for link in links:
            
        
            m=link.get_attribute('href')
            ur=m.split('/')[2]
            
        
        
            if 'aboalarm.de' in ur:
                print(m)
                
                print(data5[l])
                da.append([m,data5[l]])
            df2=pd.DataFrame(da,columns=['DATE',' '])
        df2.to_csv('v.csv',index=False,header=False,mode='a')
                
    except:
        continue       
        
      
        
    
    
    #print('......................................')   
    










        


  
    