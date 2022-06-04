from statistics import mode
from unicodedata import category
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
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
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException




 

options = webdriver.ChromeOptions()

options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome( options=options)
options.add_argument("--headless")
driver.maximize_window()



for j in range(1,51):
    print(j)

    url='https://books.toscrape.com/catalogue/page-{}.html'.format(j)
    driver.get(url)


    aaa=driver.find_elements(By.XPATH,'//div[@class="image_container"]')
    dd=[]
    for da in range(int(len(aaa))):
        
        
    
        aaa=driver.find_elements(By.XPATH,'//div[@class="image_container"]')
        aaa[da].click()
        time.sleep(1)
        title=driver.find_element(By.XPATH,'//div[@class="col-sm-6 product_main"]/h1').text
        price=driver.find_element(By.XPATH,'//p[@class="price_color"]').text.replace('£','')
        stock=driver.find_element(By.XPATH,'//p[@class="instock availability"]').text.strip()
        rat=driver.find_element(By.XPATH,'//div[@class="col-sm-6 product_main"]').find_elements(By.TAG_NAME,'p')
        d=[]
        for i in rat:
            r=i.get_attribute('class').split(' ')[-1]
            d.append(r)
        ratting=r

        upc=driver.find_element(By.XPATH,'//table[@class="table table-striped"]').find_element(By.TAG_NAME,'td').text
        cate=driver.find_element(By.XPATH,'//ul[@class="breadcrumb"]/li[3]').text
        print(title)
        print(price)
        print(stock)
        print(ratting)
        print(upc)
        print(cate)
        print('...........................')
        driver.back()
        #driver.execute_script("window.scrollTo(0,400);")
        time.sleep(1)
        dd.append([title,price,stock,ratting,upc,cate])
        df=pd.DataFrame(dd,columns=['TITLE','PRICE','IN STOCK','RATTING','UPC','CATEGORY'])
    df.to_csv('book_toscrape.csv',index=False,mode='a',header=False)
        
