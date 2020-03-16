# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:04:59 2019

@author: alexius
"""
 
import pandas as pd
from sklearn.linear_model import LogisticRegression as LR  #Logistic model from sklearn
#%% supervised learning 


####!!!!task 1 roughly, there are three types machine learning models, supervised learning、 unsupervised learning and semi-supervised learning, try find the difference online
#In supervised learning, it can be either regression or classification, which depends on y, in the following, we only consider classified models, try regression ones by yourself


#setp1 - data preprocessing, we leave this part behind.
#The following data is well prepared, or standard input data, including input variable x and result y 
filename = 'datas/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8].as_matrix()
y = data.iloc[:,8].as_matrix()

#setp2 - training model
lr = LR()  
lr.fit(x, y) 

#setp3 - output and model evaluation 
z = lr.predict(x)
print ("lr accuracy", lr.score(x,y) )

#try to read about logistic regression and understand the following
pl = lr.predict_proba(x)
lr.predict_log_proba(x)
#Log of probability estimates.The returned estimates for all classes are ordered by the label of classes
#%% DecisionTree
from sklearn.tree import DecisionTreeClassifier as DT
dt = DT(criterion="entropy")
dt.fit(x,y)
dt.predict(x)
pde = dt.predict_proba(x)
print("DTE accuracy", dt.score(x,y) ) 

dt = DT(criterion="gini")
dt.fit(x,y)
dt.predict(x)
pdg = dt.predict_proba(x)
print("DTG accuracy", dt.score(x,y) ) 
# z = dt.predict([[40,	1,	15,14,	55,	5.5,	0.856075,	2.16892]])



####!!!task 2 there are two criterions on dcisiontree model, gini and entropy, try to understand the difference 

####!!!task 3 try these two dcisiontree models on banloan default problem 


from sklearn.naive_bayes import GaussianNB as GB
gb = GB()
gb.fit(x,y)
gb.predict(x)
pgb = gb.predict_proba(x)
print("NB accuracy", gb.score(x,y) ) 

from sklearn.svm import SVC 
svc = SVC()
svc.fit(x,y)
svc.predict(x)
print("svc accuracy", svc.score(x,y) )