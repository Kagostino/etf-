import csv
with open(r'C:\Users\User\Desktop\HW01 all.csv', newline='') as csvfile:

    rows = csv.DictReader(csvfile)
    A=[]
    for row in rows:
        A.append(row['Symbol'])

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
for x in A:
    #先呼叫chromdedriver
    main_driver = webdriver.Chrome(r"C:\Users\User\Desktop\chromedriver.exe")  # 注意你們放CHROMEDRIVER的位置
    #告訴chromedriver 等下要找的element 如果沒有找到，要等10秒讓他們生完
    main_driver.implicitly_wait(10)
    #打開目標網頁
    main_driver.get('https://finance.yahoo.com/')
    
    #找到該頁面的input欄位element
    input_ele = main_driver.find_element_by_xpath('//*[@id="fin-srch-assist"]/input')
    #在該欄位element中輸入公司兩個字
    input_ele.send_keys(x)
    #找到輸入旁的按鈕
    
    time.sleep(2)
    btn_ele = main_driver.find_element_by_xpath('//*[@id="search-button"]')

    #按下按鈕
    btn_ele.click()

    try:
        price=main_driver.find_element_by_xpath('//*[@id="quote-nav"]/ul/li[4]/a/span')
        price.click()
         
        date_click=main_driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/span[2]/span/input')
        date_click.click()
        year_5=main_driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/span[2]/div/div[1]/span[7]/span')
        year_5.click()
        
    
        done=main_driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/span[2]/div/div[3]/button[1]')
        done.click()
        apply=main_driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button')
        apply.click()
        
        download=main_driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span')
        download.click()
    except:
        price=main_driver.find_element_by_xpath('//*[@id="quote-nav"]/ul/li[5]/a/span')
        price.click()
         
        date_click=main_driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/span[2]/span/input')
        date_click.click()
        year_5=main_driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/span[2]/div/div[1]/span[7]/span')
        year_5.click()
        
        
        done=main_driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/span[2]/div/div[3]/button[1]')
        done.click()
        apply=main_driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button')
        apply.click()
        
        download=main_driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span')
        download.click()
        
    
    time.sleep(2)
    main_driver.quit()
