#Calculate the Average of the Data AQI data sets

import pandas as pd
import matplotlib

def Average_data_2013():
    '''Function to Calculate the Average of 24 hours as given as 1 day. Data is availabe on per hour
    PM 2.5'''
    average = [] #Final list Which Stores the PM Value.
    temp_i=0  # Counter

    for rows in pd.read_csv('Data/AQI/aqi2013.csv',chunksize=24): #Reads the CSV_File Per year
        add_var=0 #Variable to Add all the Hourly Data Declared
        avg=0.0 #Initilize to Calculate the Final Avg
        data=[] #Creating the List to Store the PM2.5 data Only
        df=pd.DataFrame(data=rows) #Creating the DataFrame.

        for index,rows in df.iterrows():  #Looping through the rows in the DF dataframe
            data.append(rows['PM2.5']) # Selecting the PM2.5 and Storing in the Data List
        for i in data: #Looping through the data List
            if type(i) is float or type(i) is int: #Checking the Type
                add_var=add_var+i #Calculating the Total Value of Variable add_var
            elif  type(i) is str: #Checking it is string
                if i!='NoData' and i!='PwrFail' and i != '---' and i!= 'InVld':
                    temp= float(i) #converting the Data to Flaot
                    add_var= add_var + temp #Adding the Coverted Value temp in add_var
        avg=add_var/24  #Finally We are Calculating the Average
        temp_i=temp_i+1 #Increasing the Counter To Take Next Segment of the Data.
        average.append(avg) #Appending the List Finally
    return average



def Average_data_2014():
    '''Function to Calculate the Average of 24 hours as given as 1 day. Data is availabe on per hour
    PM 2.5'''
    average = [] #Final list Which Stores the PM Value.
    temp_i=0  # Counter

    for rows in pd.read_csv('Data/AQI/aqi2014.csv',chunksize=24): #Reads the CSV_File Per year
        add_var=0 #Variable to Add all the Hourly Data Declared
        avg=0.0 #Initilize to Calculate the Final Avg
        data=[] #Creating the List to Store the PM2.5 data Only
        df=pd.DataFrame(data=rows) #Creating the DataFrame.

        for index,row in df.iterrows():  #Looping through the rows in the DF dataframe
            data.append(row['PM2.5']) # Selecting the PM2.5 and Storing in the Data List
        for i in data: #Looping through the data List
            if type(i) is float or type(i) is int: #Checking the Type
                add_var=add_var+i #Calculating the Total Value of Variable add_var
            elif  type(i) is str: #Checking it is string
                if i!='NoData' and i!='PwrFail' and i != '---' and i!= 'InVld':
                    temp= float(i) #converting the Data to Flaot
                    add_var= add_var + temp #Adding the Coverted Value temp in add_var
        avg=add_var/24  #Finally We are Calculating the Average
        temp_i=temp_i+1 #Increasing the Counter To Take Next Segment of the Data.
        average.append(avg) #Appending the List Finally
    return average


def Average_data_2015():
    '''Function to Calculate the Average of 24 hours as given as 1 day. Data is availabe on per hour
    PM 2.5'''
    average = [] #Final list Which Stores the PM Value.
    temp_i=0  # Counter

    for rows in pd.read_csv('Data/AQI/aqi2015.csv',chunksize=24): #Reads the CSV_File Per year
        add_var=0 #Variable to Add all the Hourly Data Declared
        avg=0.0 #Initilize to Calculate the Final Avg
        data=[] #Creating the List to Store the PM2.5 data Only
        df=pd.DataFrame(data=rows) #Creating the DataFrame.

        for index,row in df.iterrows():  #Looping through the rows in the DF dataframe
            data.append(row['PM2.5']) # Selecting the PM2.5 and Storing in the Data List
        for i in data: #Looping through the data List
            if type(i) is float or type(i) is int: #Checking the Type
                add_var=add_var+i #Calculating the Total Value of Variable add_var
            elif  type(i) is str: #Checking it is string
                if i!='NoData' and i!='PwrFail' and i != '---' and i!= 'InVld':
                    temp= float(i) #converting the Data to Flaot
                    add_var= add_var + temp #Adding the Coverted Value temp in add_var
        avg=add_var/24  #Finally We are Calculating the Average
        temp_i=temp_i+1 #Increasing the Counter To Take Next Segment of the Data.
        average.append(avg) #Appending the List Finally
    return average



def Average_data_2016():
    '''Function to Calculate the Average of 24 hours as given as 1 day. Data is availabe on per hour
    PM 2.5'''
    average = [] #Final list Which Stores the PM Value.
    temp_i=0  # Counter

    for rows in pd.read_csv('Data/AQI/aqi2016.csv',chunksize=24): #Reads the CSV_File Per year
        add_var=0 #Variable to Add all the Hourly Data Declared
        avg=0.0 #Initilize to Calculate the Final Avg
        data=[] #Creating the List to Store the PM2.5 data Only
        df=pd.DataFrame(data=rows) #Creating the DataFrame.

        for index,row in df.iterrows():  #Looping through the rows in the DF dataframe
            data.append(row['PM2.5']) # Selecting the PM2.5 and Storing in the Data List
        for i in data: #Looping through the data List
            if type(i) is float or type(i) is int: #Checking the Type
                add_var=add_var+i #Calculating the Total Value of Variable add_var
            elif  type(i) is str: #Checking it is string
                if i!='NoData' and i!='PwrFail' and i != '---' and i!= 'InVld':
                    temp= float(i) #converting the Data to Flaot
                    add_var= add_var + temp #Adding the Coverted Value temp in add_var
        avg=add_var/24  #Finally We are Calculating the Average
        temp_i=temp_i+1 #Increasing the Counter To Take Next Segment of the Data.
        average.append(avg) #Appending the List Finally
    return average


def Average_data_2017():
    '''Function to Calculate the Average of 24 hours as given as 1 day. Data is availabe on per hour
    PM 2.5'''
    average = [] #Final list Which Stores the PM Value.
    temp_i=0  # Counter

    for rows in pd.read_csv('Data/AQI/aqi2017.csv',chunksize=24): #Reads the CSV_File Per year
        add_var=0 #Variable to Add all the Hourly Data Declared
        avg=0.0 #Initilize to Calculate the Final Avg
        data=[] #Creating the List to Store the PM2.5 data Only
        df=pd.DataFrame(data=rows) #Creating the DataFrame.

        for index,row in df.iterrows():  #Looping through the rows in the DF dataframe
            data.append(row['PM2.5']) # Selecting the PM2.5 and Storing in the Data List
        for i in data: #Looping through the data List
            if type(i) is float or type(i) is int: #Checking the Type
                add_var=add_var+i #Calculating the Total Value of Variable add_var
            elif  type(i) is str: #Checking it is string
                if i!='NoData' and i!='PwrFail' and i != '---' and i!= 'InVld':
                    temp= float(i) #converting the Data to Flaot
                    add_var= add_var + temp #Adding the Coverted Value temp in add_var
        avg=add_var/24  #Finally We are Calculating the Average
        temp_i=temp_i+1 #Increasing the Counter To Take Next Segment of the Data.
        average.append(avg) #Appending the List Finally
    return average




def Average_data_2018():
    '''Function to Calculate the Average of 24 hours as given as 1 day. Data is availabe on per hour
    PM 2.5'''
    average = [] #Final list Which Stores the PM Value.
    temp_i=0  # Counter

    for rows in pd.read_csv('Data/AQI/aqi2018.csv',chunksize=24): #Reads the CSV_File Per year
        add_var=0 #Variable to Add all the Hourly Data Declared
        avg=0.0 #Initilize to Calculate the Final Avg
        data=[] #Creating the List to Store the PM2.5 data Only
        df=pd.DataFrame(data=rows) #Creating the DataFrame.

        for index,row in df.iterrows():  #Looping through the rows in the DF dataframe
            data.append(row['PM2.5']) # Selecting the PM2.5 and Storing in the Data List
        for i in data: #Looping through the data List
            if type(i) is float or type(i) is int: #Checking the Type
                add_var=add_var+i #Calculating the Total Value of Variable add_var
            elif  type(i) is str: #Checking if it is string
                if i!='NoData' and i!='PwrFail' and i != '---' and i!= 'InVld':
                    temp= float(i) #converting the Data to Flaot
                    add_var= add_var + temp #Adding the Coverted Value temp in add_var
        avg=add_var/24  #Finally We are Calculating the Average
        temp_i=temp_i+1 #Increasing the Counter To Take Next Segment of the Data.
        average.append(avg) #Appending the List Finally
    return average


if __name__ == "__main__":
   print(Average_data_2013())
   print("-"*60)
   print(Average_data_2014())
   print("-" * 60)
   print(Average_data_2015())
   print("-" * 60)
   print(Average_data_2016())
   print("-" * 60)
   print(Average_data_2017())
   print("-" * 60)
   print(Average_data_2018())














