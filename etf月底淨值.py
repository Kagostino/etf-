import csv
import pandas as pd
with open(r'C:\Users\User\Desktop\date.csv', newline='') as csvfile:

    rows = csv.DictReader(csvfile)
    A=[]
    for row in rows:
        A.append(row['Date'].replace("-", "/", 2))
with open(r'C:\Users\User\Desktop\HW01 all.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    B=[]
    for row in rows:
        B.append(row['Symbol'])
for x in B:
    try:
        file='C:\\Users\\User\\Desktop\\ETF\\'+x+'.csv'          
        last=[]
        close=[]
        with open(file, newline='') as csvfile:
            rows = csv.DictReader(csvfile)  
        
            for row in rows:
                if row['Date'].replace("-", "/", 2) in A:
                    last.append(row['Date'].replace("-", "/", 2))
                    close.append(row['Close'])          
        s1 = pd.Series(last)
        s2 = pd.Series(close)
        df = pd.DataFrame({'Date':s1,'close':s2})
        df.to_csv(file)
    except:
        pass #因為有一個prn檔案有問題

