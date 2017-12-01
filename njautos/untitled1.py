#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:56:10 2017

@author: Memo
"""

import pandas as pd
import numpy as np
name_list=['clean_njauto_Audi','clean_njauto_Benz','clean_njauto_BMW','clean_njauto_Chevrolet','clean_njauto_Dodge','clean_njauto_Ford','clean_njauto_Honda','clean_njauto_Jeep','clean_njauto_Lexus','clean_njauto_Mazda','clean_njauto_Nissan','clean_njauto_Toyota']

'''
lis=[]
for name in name_list:
    data=pd.read_csv(name+".csv",header=None)
    
    data.columns=['UC','year','brand','model','price','mileage']
    for i in range(len(data['UC'])):
        if str(data['year'][i])+' '+data['brand'][i]+' '+data['model'][i] not in lis:
            lis.append(str(data['year'][i])+' '+data['brand'][i]+' '+data['model'][i])
print lis
x=pd.DataFrame(lis)
x[1]=0
x.to_csv
c={}


for i in range(len(x)):
    c[x.loc[i][0]]=x.loc[i][1]    
'''
nlis=pd.read_csv("name_list.csv",header=None)
c={}
for i in range(len(nlis)):
    c[nlis.loc[i][1]]=nlis.loc[i][2]

#name_list=['clean_njauto_Acura']
for name in name_list:
    lis=[]
    data=pd.read_csv(name+".csv",header=None)
    data.columns=['UC','year','brand','model','price','mileage']
    for i in range(len(data['UC'])):
        lis.append(c[str(data['year'][i])+' '+data['brand'][i]+' '+data['model'][i]])
    
    data['Oprice']=lis
    #header=['UC','year','brand','model','price','mileage','Oprice']
    data.to_csv(name+".csv")

#print lis
