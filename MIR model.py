# -*- coding: utf-8 -*-
"""
X.Wang
"""

from AlgorithmPackage import *
from FunctionalPackage import *



#%% loop for everydays bond MIR

curvedatadir = '2.1 Curve Datas/'
bonddatadir = '2.2 Bond Datas'
curvelist = os.listdir(curvedatadir)
bondlist=os.listdir(bonddatadir)
for i in zip(curvelist,bondlist):
    # Load benchamark curve and bond data
    print('Loading '+i[0][:10]+' Data') 
    curve=csvDataReadP10(file=os.path.join(curvedatadir,i[0]),index_col=None)    
    bond=csvDataReadP10(file=os.path.join(bonddatadir,i[1]),index_col='SecurityCode')
    # MIR and MIR index and MIR regions boudaries 
    data=BondResultQ5(curve,bond,col=['Maturity','YTM'],type='CorporateBond',alloutfile='2.3 MIR Result/'+i[1][0:10]+'_CorporateBond.csv') #,outfile='3.2中票债券衍生/'+i[1][0:10]+'_模型结果输出.csv'

#%% Merge data
AllTimeResult=ResultCollectionByP73(inputdatadir='2.3 MIR Result/',outputdatadir='2.4 All Time Results/',sortcol=['SecurityCode',  'Date'])
    
#%% Plot some Corporate Bond MIR 

col=['Date', 'SecurityCode',  'Maturity',
        'YTM', 'BondRiskIndex', 'MIR', 
       'Government_Bond', 'Lv1|Lv2', 'Lv2|Lv3', 'Lv3|Lv4', 'Lv4|Lv5',
       'Lv5|Lv6', 'Lv6|Lv7', 'Lv7|Lv8', 'Lv8|Lv9', 'Lv9|Lv10', 'Lv10|Lv11',
       'Lv11|Lv12', 'Lv12|Lv13', 'Lv13|Lv14', 'Lv14|Lv15',
       'Spread(YTM-Government_Bond)', 'Spread(Lv1|Lv2-Government_Bond)',
       'Spread(Lv2|Lv3-Government_Bond)', 'Spread(Lv3|Lv4-Government_Bond)',
       'Spread(Lv4|Lv5-Government_Bond)', 'Spread(Lv5|Lv6-Government_Bond)',
       'Spread(Lv6|Lv7-Government_Bond)', 'Spread(Lv7|Lv8-Government_Bond)',
       'Spread(Lv8|Lv9-Government_Bond)', 'Spread(Lv9|Lv10-Government_Bond)',
       'Spread(Lv10|Lv11-Government_Bond)',
       'Spread(Lv11|Lv12-Government_Bond)',
       'Spread(Lv12|Lv13-Government_Bond)',
       'Spread(Lv13|Lv14-Government_Bond)',
       'Spread(Lv14|Lv15-Government_Bond)']

Data=AllTimeResult.loc[:,col]
SecuritySet=set(Data.loc[:,'SecurityCode'])

#riskindex plot

k=15 #select k corporate bonds
for j in list(SecuritySet)[:k]:
    data=Data.loc[Data.loc[:,'SecurityCode']==j]
    if len(data)==0:
        continue
    data.index=data.Date

    plt.figure(figsize=(12, 9))    
    plt.plot(data.iloc[:,21],'r+')
    col=list(data.columns[-14:])
    for i in col:
        plt.plot(data.loc[:,i])
    plt.legend()
    keydate=list(range(0,len(data),5))+[len(data)-1]
    plt.xticks(keydate,list(data.index[[keydate]]),rotation=30)
    plt.title('Corporate Bond '+j)
    plt.xlabel('Date')
    plt.ylabel('Yield Spread')
    plt.grid(True,axis='both')
    plt.show()

#%% Plot Default bond riskindex and MIR

#RiskIndex
DefaultSecuritySet=['143879.SH', '143697.SH', '143443.SH','136520.SH','136439.SH','122267.SH', '136351.SH','136684.SH', '136791.SH','112505.SZ','136742.SH', '136371.SH','122492.SH', '122483.SH']
for j in list(DefaultSecuritySet):
    data=Data.loc[Data.loc[:,'SecurityCode']==j]
    if len(data)==0:
        continue
    data.index=data.Date
    plt.figure(figsize=(8, 4))    
    plt.plot(data.iloc[:,4],'r-')
    plt.legend()
    keydate=list(range(0,len(data),5))+[len(data)-1]
    plt.xticks(keydate,list(data.index[[keydate]]),rotation=30)
    plt.title('Corporate Bond '+j)
    plt.ylim((data.iloc[:,4].min()-1,data.iloc[:,4].max()+1))
    plt.xlabel('Date')
    plt.ylabel('Risk Index')
    plt.grid(True,axis='both')
    plt.show()

#MIR and MIR regions
for j in list(DefaultSecuritySet):
    data=Data.loc[Data.loc[:,'SecurityCode']==j]
    if len(data)==0:
        continue
    data.index=data.Date

    plt.figure(figsize=(12, 9))    
    plt.plot(data.iloc[:,21],'r+')
    col=list(data.columns[-14:])
    for i in col:
        plt.plot(data.loc[:,i])
    plt.legend()
    keydate=list(range(0,len(data),5))+[len(data)-1]
    plt.xticks(keydate,list(data.index[[keydate]]),rotation=30)
    plt.title('Corporate Bond '+j)
    plt.xlabel('Date')
    plt.ylabel('Yield Spread')
    plt.grid(True,axis='both')
    plt.show()

