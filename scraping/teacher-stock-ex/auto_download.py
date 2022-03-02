import requests
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier , plot_tree
import random
import math
# dates = [20200201, 20200101, 20191201]
start=20211001
month = int(np.mod(np.floor(start / 100), 100))
year = int(np.floor(start / 10000))
TIME=[]
LONG=13
for i in range(LONG):
    ss = year * 10000 + month * 100 + 1
    TIME.append(ss)
    month-=1
    if month==0:
        year-=1
        month=12
TIME=TIME[::-1]


stockNo = [1734]


url_template = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}"
s=0
for stockNos in stockNo:
    p=0
    s+=1
    for date in TIME:
        url = url_template.format(date, stockNos)
        # file_name = "{}_{}.csv".format(stockNo, date)

        data = pd.read_html(requests.get(url).text)[0]
        time.sleep(3+abs(np.random.rand(1)))
        if p==0:
            AA = np.array(data)
        else:
            AA = np.vstack((AA,np.array(data)))
        p+=1
        Name = data.columns[0][0][13:-7]
        print(s,' ',stockNos,'',Name,int(date/10000),'年',int(np.mod(date/100,100)),'月','OK')

    # for i in range(len(AA[0,:])):
    #     if i==0:
    #         title=data.columns[i][1]
    #     else:
    #         title = np.hstack((title,data.columns[i][1]))

    AA1=(AA[1:,4]-AA[1:,5])/AA[:-1,6]*100
    AA2 = (AA[1:, 6] - AA[:-1, 6]) / AA[:-1, 6] * 100
    AA3= (AA[1:, 6] - AA[:-1, 6])
    for i in range(len(AA1)):
        AA1[i]=np.round(AA1[i],2)
        AA2[i] = np.round(AA2[i], 2)
    AA1=np.array(AA1).reshape(-1,1)
    AA2 = np.array(AA2).reshape(-1, 1)
    AA=np.hstack((AA[1:,:],AA1,AA2))
    AA=AA[::-1]
    index=np.array([0,3,4,5,6,7,10,9,1,2,8])
    for i in range(len(AA[0,:])):
        if i ==0:
            NEWAA=np.array(AA[:,0]).reshape(-1,1)
        else:
            NEWAA = np.hstack((NEWAA,np.array(AA[:,index[i] ]).reshape(-1,1)))

    title=np.hstack(('交易','開盤','最高','最低','收盤','漲跌','漲跌.1','振幅','成交股數','成交金額','成交筆數'))
    QQ=np.zeros(len(AA[0,:]))
    ALL=np.vstack((title,QQ,QQ,NEWAA))
    pd.DataFrame(ALL).to_excel( '數據/'+Name+'.xlsx',sheet_name='Sheet1', index=False, header=False)
    NAME='數據/'+Name+'.xlsx'
    # NAME = '數據/愛普.xlsx'
    NAME=NAME[3:]
    time.sleep(20)
