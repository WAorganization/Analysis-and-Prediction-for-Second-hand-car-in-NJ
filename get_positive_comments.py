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
        ncol=len(next(spamreader)) # Read first line and count columns
        inf.seek(0)
        for row in spamreader:
            comments.append(str(row))
#    print("Sentiment Analysis for " + brand + ":")
    print("Positive comments of " + brand + " is:")
    for comment in comments:
        ss = sid.polarity_scores(comment)
#        p_rate= ss['neg']/ss['pos']   
        po_num=ss['pos']*ncol
        print(int(round(po_num)))
#        for k in sorted(ss):
#            print('{0}: {1}, '.format(k, ss[k]))
            
if __name__ == "__main__":
    filenames = ["BMW", "Ford", "Honda", "Lexus", "Mazda", "Toyota", "Audi", \
                 "Chevrolet", "Jeep", "Mercedes-Benz", "Dodge", "Nissan", "Acura"]
    for filename in filenames:
        sentiment_analysis(filename)

        
    