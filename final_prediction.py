# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 15:18:43 2017

@author: zmx
"""
import pandas as pd
from sklearn import svm 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression

def normalize(x, coefficient):
    normalized_res=(x-x.min())/(x.max()-x.min())*coefficient
    normalized_res = normalized_res.astype("int")
    return normalized_res

def clean_data(data):
    models=[]
#    data=data.dropna(subset=['D_rate'], how='all')
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
#    data['year']=normalize(data['year'])
    data['mileage']=normalize(data['mileage'],2010)
    data['model']=normalize(data['model'],2000)
    data['D_rate']=normalize(data['D_rate'],2000)
    return data

def train_and_predict(train, test, param_list):
    #svm_pre = svm.SVC(probability=True)
    LR_pre = LogisticRegression(C=15, penalty='l2', solver='liblinear')
    SVM_pre = svm.SVC(C=12,kernel='rbf',gamma='auto')
    CART_pre = tree.DecisionTreeClassifier(criterion="gini", max_depth=28)
    GNB_pre = GaussianNB(priors=None)
    MNB_pre = MultinomialNB(alpha=0.01)
    BNB_pre = BernoulliNB(alpha=0.2)
    RFR_pre = RandomForestRegressor(n_estimators=500)
    RFC_pre = RandomForestClassifier(criterion="entropy",n_estimators=300)
    KNN_pre = KNeighborsClassifier(10)
    LG_pre = LinearRegression()

    model_list=[]
    model_list.append(SVM_pre)
    model_list.append(CART_pre)
    model_list.append(GNB_pre)
    model_list.append(MNB_pre)
    model_list.append(BNB_pre)
    model_list.append(RFR_pre)
    model_list.append(RFC_pre)
    model_list.append(KNN_pre)
    model_list.append(LG_pre)
    model_list.append(LR_pre)

    for obj in model_list:
        result=[]
        obj.fit(train[param_list], train['D_rate'])
        result=obj.score(test[param_list], test['D_rate'])
        temp = str(obj).split('(')
        a = temp[0]
        print("The result of " + str(a) + ":")
        print(result)
    print("________________________________________")

if __name__ == "__main__":
    name="merge"
    data=pd.read_csv(name+".csv")
    data = data[pd.notnull(data['D_rate'])]
    cleaned_data=clean_data(data)
    cleaned_data['PC']=normalize(cleaned_data['PC'], 2250)
    train, test = train_test_split(cleaned_data, test_size=0.3)
    print("The result of full model:")
    param_list1=["mileage","year","model","PC"]            
    train_and_predict(train,test,param_list1)
    print("The result of non-sentiment_analysis:")
    ns_train = train[['year','mileage','brand','model','D_rate']]
    ns_test = test[['year','mileage','brand','model','D_rate']]
    param_list2=["mileage","year","model"]
    train_and_predict(ns_train, ns_test, param_list2)
    