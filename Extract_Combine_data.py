from Average import Average_data_2013,Average_data_2014,Average_data_2015,Average_data_2016,Average_data_2017,Average_data_2018
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv

def meta_data(month,year):
    file_html=open('Data/Html_Data/{}/{}.html'.format(year,month),'rb')
    plain_text=file_html.read()

    tempD=[]
    FinalD=[]

    soup=BeautifulSoup(plain_text,"html.parser")
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a=tr.get_text()
                tempD.append(a)
    #To calculate the number of rows in the List
    rows=len(tempD)/15
    for times in range(round(rows)):
        newtempD=[]
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        FinalD.append(newtempD)
    length=len(FinalD)
    FinalD.pop(length - 1)
    FinalD.pop(0)
    for a in range(len(FinalD)):
        FinalD[a].pop(6)
        FinalD[a].pop(13)
        FinalD[a].pop(12)
        FinalD[a].pop(11)
        FinalD[a].pop(10)
        FinalD[a].pop(9)
        FinalD[a].pop(0)

    return FinalD

def combine_data(year, cs):
    for a in pd.read_csv('Data/Real_data/real_' + str(year) + '.csv', chunksize=cs):
        df=pd.DataFrame(data=a)
        mylist=df.values.tolist()
    return mylist




if __name__=="__main__":
    if not os.path.exists("Data/Real_Data"):
        os.makedirs("Data/Real_Data") #Creating the New Directory named {Real-data}
    counter = 0
    lis1=[Average_data_2013(),Average_data_2014(),Average_data_2015(),Average_data_2016(),Average_data_2017(),Average_data_2018()]
    for year in range(2013,2019):
        final_data=[]
        with open('Data/Real_data/real_'+ str(year)+ '.csv', 'w') as csvfile:
            wr=csv.writer(csvfile,dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in range(1,13):
                temp=meta_data(month,year)
                final_data=final_data+temp #Final Data is Extracted in the List {final_data}.
        pm = []
        pm = lis1[counter]
        counter += 1
        # pm = getattr(sys.modules[__name__],"Average_Data_{}".format(year))()
        # if len(pm) == 364:
        #     pm.insert(364, '-')

        #Adding the PM at the eight Index
        for i in range(len(final_data) - 1):
            # final[i].insert(0, i + 1)
            final_data[i].insert(8, pm[i])

       #Droping the missing Values from the Table.
        with open('Data/Real_data/real_'+ str(year) + '.csv', 'a') as csvfile:
            wr=csv.writer(csvfile,dialect='excel')
            for row in final_data:
                flag=0
                for ele in row:
                     if ele == "" or ele == "-":
                         flag=1
                if flag!=1:
                    wr.writerow(row)

    data_2013=combine_data(2013,600)
    data_2014=combine_data(2014,600)
    data_2015=combine_data(2015,600)
    data_2016=combine_data(2015,600)
    data_2017=combine_data(2015,600)
    data_2018=combine_data(2015,600)

    total = data_2013 + data_2014 + data_2015 + data_2016 + data_2017 + data_2018

    with open('Data/Real_data/Real_Combine.csv', 'w') as csvfile:
       wr=csv.writer(csvfile,dialect='excel')
       wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
       wr.writerows(total)



# df=pd.read_csv('Data/Real-Data/Real_Combine.csv')

































































