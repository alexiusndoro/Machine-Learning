# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 00:52:32 2019

@author: alexius
"""

 
import pandas as pd
from sklearn.linear_model import LogisticRegression as LR  #Logistic model from sklearn

#%% Logistic model for default

filename = 'datas/bankloan.xls'
data = pd.read_excel(filename)
#this is a bank loan data, inculding all clients' personal information and default record.
#print(data.iloc[:,:8]) #:8 means all columns until column 8 

x = data.iloc[:,:8].as_matrix() #define variable x

# we label 1 as default,0 otherwise.
y = data.iloc[:,8].as_matrix() #define variable y
lr = LR()  #use logistic model
lr.fit(x, y)  #training model
lr.predict(x)  #model predict
result_comparison=pd.concat([data.iloc[:,8],pd.DataFrame(lr.predict(x))],axis=1)
















print ("accuracy" ,lr.score(x,y)) #accuracy rate 

'''from sklearn.metrics import confusion_matrix
y_pr=lr.predict(x)
y_tr=y
conf = confusion_matrix(y_tr, y_pr)'''
#%%  feature selection

# The accuracy is 80%, the feature we training the model may affect the result
data.iloc[:,:8].columns


#we believe the feature 'address' is unrelated to personal default, what about others?
#in the following, we use a algorithm to select the best related feature

rlr = RLR()  
rlr.fit(x, y)
print (rlr.get_support())  #me Get a mask, or integer index, of the features selected
 
print ('related feature are: %s' % list(data.iloc[:,:8].columns[rlr.get_support()]))
x = data[data.iloc[:,:8].columns[rlr.get_support()]].as_matrix()  #use related feature as training data

lr = LR()  
lr.fit(x, y)  
print("accuracy", lr.score(x, y))  # a little bit improved
