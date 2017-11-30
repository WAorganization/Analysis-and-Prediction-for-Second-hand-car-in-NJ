# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:11:20 2017

@author: zmx
"""
import requests, csv
from bs4 import BeautifulSoup
import unicodedata
from time import sleep
# send a get request to the web page
count=1
#with open('suv_csv.csv', "a") as out_f:
#    writer = csv.writer(out_f)
#    writer.writerow(["title", "price","engine","transmission","drivetrain","mileage","location"])
brand_name = "BMW"
base_url = "http://autos.nj.com/search/make-" +brand_name+"/location-07030/body-SUV/range-12500/page-"
end_url = "/vcond-Used"
page_url=base_url +str(count)+ end_url
fileprefix = "njauto_"
def parse(string):
    string=unicodedata.normalize('NFKD', string).encode('ascii','ignore')
    return string.replace("\n", "")
while page_url!=None:
    page_url=base_url+str(count)+ end_url
    page = requests.get(page_url)    
    count+=1
    print count
    if page.status_code!=200:
        page_url=None
    else:       
        soup = BeautifulSoup(page.content, 'html.parser')  
        
        rows=[]
        # the content we need
        print("*******")
        p=soup.select("#results")
        print len(p)
        for count in range(len(p)):
            print("**************************")
            div=p[count]
            p_title=div.select(".title")
            #print p_title
            p_price=div.select(".main-price-title")
            p_info=div.select(".properties-list-inner .hidden-mobile")
            p_info2=div.select(".properties-list-inner .r-card-visible-item")
            print("**************************")
            j=0
            k=0
            for i in range(len(p_title)):
                title = parse(p_title[i].get_text())
                price = parse(p_price[i].get_text()).strip()
                engine = parse(p_info[j].get_text())
                transmission = parse(p_info[j+1].get_text())
                drivetrain = parse(p_info[j+2].get_text())
                mileage = parse(p_info2[k].get_text()).replace("Mileage", "").strip()
                location = parse(p_info2[k+1].get_text()).replace("Location", "").replace(" ","")
                rows.append((title,price,engine,transmission,drivetrain,mileage,location))
                j=j+3
                k=k+2
        sleep(1)
        ouf = fileprefix + brand_name + ".csv"
        with open(ouf, "a") as out_f:
            writer = csv.writer(out_f)
            writer.writerows(rows)

