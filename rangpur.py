from re import A
from statistics import mode
from unicodedata import category
from pyparsing import White
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
import pandas 
import csv
import random
from openpyxl import Workbook
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl.styles import Font, Color, Alignment, Border, Side
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder
from openpyxl.utils import get_column_letter
from selenium.webdriver.common.by import By
import os
import urllib
import math
import sys
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
from tkinter import simpledialog
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome( chrome_options=options)
options.add_argument("--headless")

j=0


d=[] 
url='https://www.lifepharmacy.com/products?categories=makeup'


driver.get(url)
while 1<2:
    
    
    try:
        driver.find_element(By.XPATH,'//button[@class="btn btn-outline-darker btn-load-more"]').click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,2000);")
    except:
        break
    
    


    
alllinks=driver.find_elements(By.XPATH,'//h3[@class="product-title"]')

    
for sup in alllinks:
    urls=sup.find_element(By.TAG_NAME,'a').get_attribute('href')
       
    d.append(urls)
            
print(len(d))
s=0
for ur in d:
    s=s+1
    data=[]

    driver.get(ur)
    time.sleep(4)
    try:
        title=driver.find_element(By.XPATH,'//h1[@class="product-title"]').text
    except:
        title=' '
    try:
        price=driver.find_element(By.XPATH,'//b[@class="new-price"]').text
    except:
        price=' '
    try:
        img=driver.find_element(By.XPATH,'//img[@id="product-zoom"]').get_attribute('src')
    except:
        img=' '
    try:
        brand=driver.find_element(By.XPATH,'//span[@class="d-inline-block mr-3"]').text.split(':')[-1]
    except:
        brand=' '
    try:
        sku=driver.find_element(By.XPATH,'//div[@class="product-cat"]').text.split('SKU:')[-1]
    except:
        sku=' '
    try:
        cate=driver.find_element(By.XPATH,'//div[@class="product-cat w-100 text-truncate"]').text.split(':')[-1]
    except:
        cate=' '
    try:
        des=driver.find_element(By.XPATH,'//div[@class="product-desc-content"]').text
    except:
        des=' '
    
    print(s)
    
    print('..........................................................................')
    data.append([title,img,brand,sku,cate,price,des,s])
    df=pandas.DataFrame(data,columns=['TITLE','IMG_URL','BRAND','SKU','CATEGORY','PRICE','DESCRIPTION',' '])
    
    df.to_csv('lifepharmacy.csv',mode='a',index=False,header=False)