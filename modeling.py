# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 17:31:03 2017

@author: zmx
"""
import pandas as pd
from sklearn import svm 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

def clean_data(data):
    d_rate=[]
    models=[]
    data=data.dropna(subset=['D_rate'], how='all')
    for i in data['D_rate']:
        d_rate.append(int(i*10))
    data['D_rate']=d_rate
    
    model_dict={}
    model_idx=0
    for i in data['model']:
        if i not in model_dict.values():
            model_dict[model_idx]=i
            model_idx=model_idx+1
    
    for s in data['model']:
        for index, model_name in model_dict.iteritems():
            if model_name == s:
                models.append(index)
    data['model']=models
    return data

def train_and_predict(train, test):
    LR_pre = LogisticRegression(C=1000.0, random_state=0)
    #svm_pre = svm.SVC(probability=True)
    svm_pre = svm.SVC(C=0.05)
    CART_pre = tree.DecisionTreeClassifier(criterion="gini", max_depth=32)
    GNB_pre = GaussianNB()
    MNB_pre = MultinomialNB(alpha=0.01)
    RFR_pre = RandomForestRegressor(n_estimators=500)
    RFC_pre = RandomForestClassifier(criterion="entropy",n_estimators=300)
    
    svm_pre.fit(train[['UC','year', 'model']], train['D_rate']) 
    LR_pre.fit(train[['UC','year','model']], train['D_rate'])
    CART_pre.fit(train[['UC','year','model']], train['D_rate']) 
    GNB_pre.fit(train[['UC','year','model']], train['D_rate']) 
    RFC_pre.fit(train[['UC','year','model']], train['D_rate'])
    RFR_pre.fit(train[['UC','year','model']], train['D_rate'])
    MNB_pre.fit(train[['UC','year','model']], train['D_rate'])
    a=svm_pre.score(test[['UC','year','model']], test['D_rate'])
    b=LR_pre.score(test[['UC','year','model']], test['D_rate'])
    c=CART_pre.score(test[['UC','year','model']], test['D_rate'])
    d=GNB_pre.score(test[['UC','year','model']], test['D_rate'])
    e=RFC_pre.score(test[['UC','year','model']], test['D_rate'])
    f=MNB_pre.score(test[['UC','year','model']], test['D_rate'])
    g=RFR_pre.score(test[['UC','year','model']], test['D_rate'])
    print("The result of support vector machine:")
    print(a)
    print("The result of Logistic regression:")
    print(b)
    print("The result of Decision Tree:")
    print(c)
    print("The result of Gaussian Naive Bayes:")
    print(d)
    print("The result of Random Forest Classifier:")
    print(e)
    print("The result of multinomial naive Bayes:")
    print(f)
    print("The result of Random Forest Regressor:")
    print(g)
    print("________________________________________")

if __name__ == "__main__":
    name_list=['clean_njauto_Acura','clean_njauto_Audi','clean_njauto_Benz','clean_njauto_BMW','clean_njauto_Chevrolet','clean_njauto_Dodge','clean_njauto_Ford','clean_njauto_Honda','clean_njauto_Jeep','clean_njauto_Lexus','clean_njauto_Mazda','clean_njauto_Nissan','clean_njauto_Toyota']
#    model_list=["svm_pre","LR_pre","CART_pre","GNB_pre","RFC_pre","RFR_pre","MNB_pre"]
    for name in name_list:
        data=pd.read_csv(name+".csv")
        cleaned_data=clean_data(data)
        train, test = train_test_split(cleaned_data, test_size=0.3)
        print("The prediction of " + name+ " :")            
        train_and_predict(train,test)
        
