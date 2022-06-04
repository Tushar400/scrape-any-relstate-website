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
import pandas
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
from tkinter import simpledialog
from bs4 import BeautifulSoup
driver=webdriver.Chrome()
for i in range(1,26):
    try:

        url='https://www.privateproperty.co.za/to-rent/gauteng/centurion/centurion-east/957?page={}'.format(i)
        driver.get(url)
        try:
            driver.find_element(By.XPATH,'//button[@class="privacy-toast-message__button privacy-toast-message__button--allow-all-cookies"]').click()
        except:
            pass

        divs=driver.find_elements(By.XPATH,'//a[@class="listingResult row "]')

        
        l1=[]

        for div in divs:
            link=div.get_attribute('href')
            l1.append(link)
        
        for li1 in l1:
            data=[]
            na=[] 
            try:

                driver.get(li1)
                numbers=driver.find_element(By.XPATH,'//button[@class="showTelNos eventShowNumber"]').click()
                time.sleep(2)
                nam=driver.find_elements(By.XPATH,'//div[@class="telNo"]')
                for n in nam:
                    na.append(n.text)
                try:
                    num1=na[0].replace('Work','')
                except:
                    num1=' '
                try:
                    num2=na[1].replace('Cell','')
                except:
                    num2=' '
                
                    num2=' '
                try:
                    name=driver.find_element(By.XPATH,'//a[@class="contactName"]').text
                except:
                    try:
                        name=driver.find_element(By.XPATH,'//div[@class="contactName"]').text
                    except:
                        name=' '

                try:
                    title=driver.find_element(By.XPATH,'//div[@class="details-header nav-wrapper"]').text
                    
                except:
                    title=' '
                
            except:
                driver.refresh()    
            data.append([title,li1,name,num1,num2,i])
            df=pandas.DataFrame(data,columns=[' ',' ',' MAIL',' ',' ',' '])    
            
                
            df.to_csv('privateproperty.csv',index=False,mode='a',header=False)
        print(i)
        print('...............................')
        
    except:
        driver.refresh()    

