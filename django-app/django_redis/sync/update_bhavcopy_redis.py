try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
from django.conf import settings
from datetime import date
import sys
import redis
import json
import csv
import requests
from zipfile import ZipFile 
from urllib.request import Request, urlopen
import datetime

def sync_csvdata_from_BSE():
    
    ''' Extract  bhav copy csv file by requests from BSE'''
    today = date.today()
    now = datetime.datetime.now()

    print("Today's date:", type(today))
    print("now ",now.hour)
    
    DateMonthYear = today.strftime("%d/%m/%Y")
    print("DateMonthYear",(DateMonthYear))
    day = (DateMonthYear.split("/")[0])
    month = (DateMonthYear.split("/")[1])
    year = (DateMonthYear.split("/")[2])[2:]
    print("day",day,month,year)
    if now.hour > 18:
        url = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ'+str(day)+str(month)+str(year)+'_CSV.ZIP'
        response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"}, timeout=50)
        print("response",response)
        if response.status_code == 200:
            print("okay")
            with open("Bhavcopy.zip", "wb") as code:
                code.write(response.content)
            with ZipFile("Bhavcopy.zip", 'r') as zip:
                zip.printdir() 

            # extracting all the files 
                print('Extracting all the files now...') 
                zip.extractall()      

                redis_instance = redis.Redis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT)
                redis_instance.flushall()
                jsonDatatoRedis = []
                with open("EQ"+str(day)+str(month)+str(year)+".CSV","r") as file:
                    csvreader = csv.DictReader(file)
                    print(file)
                    for line in csvreader:
                        # print(line)
                        jsonDatatoRedis.append(line)
                    print(len(jsonDatatoRedis))
                for jsonline in jsonDatatoRedis:
                    name = jsonline['SC_NAME']
                    redis_instance.hmset (name,{ "open": (jsonline['OPEN']), "high": (jsonline['HIGH']), "low": (jsonline['LOW']), "close" :(jsonline['CLOSE'])})
        else:
            print("Response is forbidden as today's file is not yet generated")