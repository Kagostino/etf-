import pandas as pd 
import csv
A=[]
with open(r'C:\Users\User\Desktop\HW01 all.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    B=[]
    for row in rows:
        B.append(row['Symbol'])

for x in B:
    try:
        file='C:\\Users\\User\\Desktop\\ETF\\'+x+'.csv'
        data = pd.read_csv(file,encoding='utf-8-sig')
        data
        s1=pd.Series(data['Date'])
        s2=pd.Series(data['Adj Close'])
        df = pd.DataFrame({'Date':s1,'close':s2})
        df.index.names = [x]
        A.append(df)
    except:
        pass
#_PRN額外處理
file='C:\\Users\\User\\Desktop\\ETF\\_PRN.csv'
data = pd.read_csv(file,encoding='utf-8-sig')
s1=pd.Series(data['Date'])
s2=pd.Series(data['Adj Close'])
df = pd.DataFrame({'Date':s1,'close':s2})
df.index.names = ['PRN']
A.append(df)

print(A)
