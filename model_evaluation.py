# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:39:48 2019

@author: alexius
"""

 
import pandas as pd
from sklearn.linear_model import LogisticRegression    
from sklearn.svm import SVC,LinearSVC
from sklearn.tree import DecisionTreeClassifier  
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

#%%
filename = 'datas/bankloan.xls'
data = pd.read_excel(filename)

#%% model fitting degree

a=LogisticRegression()
b=LinearSVC(dual=False,penalty='l1',C=1) 
# C is Penalty parameterof the error term.

c=SVC()
d=DecisionTreeClassifier(criterion='entropy')
e=RandomForestClassifier()
f=GaussianNB()
g=KNeighborsClassifier()
lis=[a,b,c,d,e,f,g]

y=data.iloc[:,-1]
x=data.iloc[:,:-1]

'''Q=pd.DataFrame([])
for i in lis:
    model = i
    model.fit(x,y)     
    T=pd.DataFrame([model.score(x, y)],columns=['fitting degree'],index=[str(i).split('(')[0]])
    Q=pd.concat([Q,T],axis=0)


print(Q)

#%% model predict 
# data split - 90% for training data 10% for test #### here were are manually splitting the data using slicing but can also use train_test split method

test_proportion=1/10

K=50 #50 times 

R1=pd.DataFrame([])
R2=pd.DataFrame([])
for i in range(1,K+1): 
    print('%sst data split'%i)
    testdata=data.sample(frac=test_proportion) # randomly split 10% datas by sample()
    traindata=pd.concat([data,testdata]).drop_duplicates(keep=False) # use drop_dupliicates() to get the rest of 90% data
    tr_X=traindata.iloc[:,:-1]
    tr_Y=traindata.iloc[:,-1]
    t_X=testdata.iloc[:,:-1]
    t_Y=testdata.iloc[:,-1]
    T1=pd.DataFrame([])  #dataframe([]) defines variable as empty dataframe
    Q1=pd.DataFrame([])
    T2=pd.DataFrame([])
    Q2=pd.DataFrame([])
    for x in lis:
        model = x
        model.fit(tr_X,tr_Y)     
        T1=pd.DataFrame([model.score(tr_X, tr_Y)],columns=['%s times'%i],index=[str(x).split('(')[0]])
        Q1=pd.concat([Q1,T1],axis=0)
        T2=pd.DataFrame([model.score(t_X, t_Y)],columns=['%s times'%i],index=[str(x).split('(')[0]])
        Q2=pd.concat([Q2,T2],axis=0)
        print('##。。。。。。model %s finished data trainning##'%str(x).split('(')[0])
    R1=pd.concat([R1,Q1],axis=1)
    R2=pd.concat([R2,Q2],axis=1)
    R1=R1.T.mean()
    R2=R2.T.mean()   
print(R1) #fitting
print(R2) #prediction'''

#%% Homework
    
#1 try to use train_test_split to split data  instead of above, understand its principle
    
#2 try to use cross_val_score to get the prediction-scores, understand its principle

#3 try to use roc_curve to choose your final model, understand its principle

# number 1: train_test_split to split data
from sklearn.model_selection import train_test_split 

K=50 #50 times 

R1=pd.DataFrame([])
R2=pd.DataFrame([])
for i in range(1,K+1): 
    print('%sst data split'%i)
    
    x_tr,x_t,y_tr,y_t = train_test_split(x,y,test_size = 1/10)

    T1=pd.DataFrame([])  #dataframe([]) defines variable as empty dataframe
    Q1=pd.DataFrame([])
    T2=pd.DataFrame([])
    Q2=pd.DataFrame([])
    for j in lis:
        model = j
        model.fit(x_tr,y_tr)     
        T1=pd.DataFrame([model.score(x_tr, y_tr)],columns=['%s times'%i],index=[str(j).split('(')[0]])
        Q1=pd.concat([Q1,T1],axis=0)
        T2=pd.DataFrame([model.score(x_t, y_t)],columns=['%s times'%i],index=[str(j).split('(')[0]])
        Q2=pd.concat([Q2,T2],axis=0)
        print('##。。。。。。model %s finished data trainning##'%str(j).split('(')[0])
    R1=pd.concat([R1,Q1],axis=1)
    R2=pd.concat([R2,Q2],axis=1)
    R1=R1.T.mean()
    R2=R2.T.mean()   
print(R1) #fitting
print(R2) #predictionz'''

#number 2 cross validation
from sklearn.model_selection import cross_val_score

'''K=5        
for i in range(1,K+1): '''
Q3=pd.DataFrame([])
T3=pd.DataFrame([])
R3=pd.DataFrame([])
for m in lis:
       model = m
       scores = cross_val_score(m,x,y,cv = 5, scoring="accuracy") #cv is the number of folds
       print (scores)
       T3=pd.DataFrame([scores],index=[str(m).split('(')[0]])
       Q3 = pd.concat([Q3,T3],axis=0)
R3=pd.concat([R3,Q3])       
R3=R3.T.mean()  #model with highest score performs best
print (R3) 

#number 3 roc_curve   
import sklearn.metrics as metrics
# calculate the fpr and tpr for all thresholds of the classification

for l   in  (a,d,e,f,g):
        probs = l.predict_proba(x_t)
        #only want the 'positive' probabilities (probabilty the customer defaults)
        preds = probs[:,1] 
        fpr, tpr, threshold = metrics.roc_curve(y_t, preds)
        roc_auc = metrics.auc(fpr, tpr)
        
        # method I: plt
        import matplotlib.pyplot as plt
        plt.title(str(l).split('(')[0])
        plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
        plt.legend(loc = 'lower right')
        plt.plot([0, 1], [0, 1],'r--')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.ylabel('True Positive Rate')
        plt.xlabel('False Positive Rate')
        plt.show() #highest auc is the best''''
        
        
        
        
    
           
   
    

    
    



