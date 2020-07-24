import os
import time
import requests
import sys


def retrieve_html():
    '''This function is used to retrieve the Download the Data in the Html_Data folder'''

    for year in range(2013, 2019): # Looping through year
        for month in range(1, 13): # Looping through the months
            if (month < 10): # Code for the months less than 10
                url = 'http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month, year)
            else:
                url = 'http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month,year)
            texts = requests.get(url) #This code Sends the Request to the Webpage.
            text_utf = texts.text.encode('utf=8') #Converts the Text to utf code.

            if not os.path.exists("Data/Html_Data/{}".format(year)): #Checking for the Particular path
                os.makedirs("Data/Html_Data/{}".format(year)) #Creating the Directory Named Html_Data
            with open("Data/Html_Data/{}/{}.html".format(year, month), "wb") as output: #Creating the Html file
                output.write(text_utf) #Writing The Content To htlml file

        sys.stdout.flush()


if __name__ == "__main__":
    start_time = time.time()
    retrieve_html() # Calling the Function
    stop_time = time.time()
    print("Time taken {}".format(stop_time - start_time))