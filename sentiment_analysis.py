# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:01:36 2017

@author: zmx
"""
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
def sentiment_analysis(brand):
    comments = []
    filename = brand + "_comment.csv"
    with open(filename, 'r') as inf:
        spamreader = csv.reader(inf)
        for row in spamreader:
            comments.append(str(row))
    print("Sentiment Analysis for " + brand + ":")
    for comment in comments:
#        print(comment)
        ss = sid.polarity_scores(comment)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]))
            

if __name__ == "__main__":
    filenames = ["BMW", "Ford", "Honda", "Lexus", "Mazda", "Toyota", "Audi", "Chevrolet", "Jeep", "Mercedes-Benz", "Dodge"]
#    filenames = ["Dodge", "Nissan"]    
    for filename in filenames:
        sentiment_analysis(filename)
        
    