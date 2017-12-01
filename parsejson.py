# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:46:31 2017

@author: zmx
"""
import json, csv
import unicodedata

def parse(string):
    string=unicodedata.normalize('NFKD', string).encode('ascii','ignore')
    return string
def parsejson(filename):
    inf = filename + ".json"
    ouf = filename + "_comment.csv";
    t=json.load(open(inf,"r"))
    result = []
    for i in range(len(t)):
#        print(t[i]['text'])
        result.append(parse(t[i]['text']).replace("RT", "").replace("&amp", ""))
    with open(ouf,'wb') as resultFile:
        wr = csv.writer(resultFile)     
        wr.writerow(result)

if __name__ == "__main__":
    filenames = ["BMW", "Ford", "Honda", "Lexus", "Mazda", "Toyota", "Audi", \
                 "Chevrolet", "Jeep", "Mercedes-Benz", "Nissan", "Dodge"] 
    for filename in filenames:
        parsejson(filename)


    
