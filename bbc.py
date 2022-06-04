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
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome( chrome_options=options)
options.add_argument("--headless")
driver.maximize_window()

for j in range(1,61):
    print(j)
    

    url='https://pl.aliexpress.com/category/200217614/hair-extensions.html?trafficChannel=main&catName=hair-extensions&CatId=200217614&ltype=wholesale&SortType=default&page={}'.format(j)
    driver.get(url)

    
    

    driver.execute_script("window.scrollTo(0,800);")
    time.sleep(0.1)
    driver.execute_script("window.scrollTo(900,1700);")
    time.sleep(.1)
    driver.execute_script("window.scrollTo(1800,2400);")
    time.sleep(.1)
    driver.execute_script("window.scrollTo(2500,3200);")
    time.sleep(.1)
    driver.execute_script("window.scrollTo(3300,4500);")
    time.sleep(.1)
   
    divs=driver.find_elements(By.XPATH,'//a[@class="_3t7zg _2f4Ho"]')
    data=[]
    
    
    for sup in divs:
        link=sup.get_attribute('href')
        data.append([link])
        
    print(len(data))
    
    print('...................................................................')
               
    df=pd.DataFrame(data,columns=['product link'])
    df.to_csv('aliexpress-Przedłużanie włosów i peruki.csv', mode='a',header=False,index=False)