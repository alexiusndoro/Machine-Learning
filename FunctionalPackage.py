
# coding: utf-8
from AlgorithmPackage import *



#%% Global variable

global newclasssymbol
newclasssymbol=['Lv1|Lv2','Lv2|Lv3','Lv3|Lv4','Lv4|Lv5',\
               'Lv5|Lv6','Lv6|Lv7','Lv7|Lv8','Lv8|Lv9','Lv9|Lv10','Lv10|Lv11',\
               'Lv11|Lv12','Lv12|Lv13','Lv13|Lv14',\
               'Lv14|Lv15'] 

#%%

#data read 
def csvDataReadP10(file="3.1 Curve Datas/2019-04-30_curvedata.csv",index_col=None):
    datapath=codecs.open(file,'r','utf-8')
    data=pd.read_csv(datapath,index_col=index_col) 
    return(data)

  

#%%

#MIR benchmark Curve construction
    
def curveAllBenchmarkQ41(curve):
    yield_curve=pd.concat([curve.iloc[:,:3],curve.iloc[:,4:]],axis=1)

    S=yield_curve.iloc[:,2] 

    G3=yield_curve.loc[:,'AAA']  
    G1=pow(S*S*G3,1/3)   
    G2=pow(S*G3*G3,1/3)   
    #投资级
    I1=yield_curve.loc[:,'AA+']  
    I2=yield_curve.loc[:,'AA']  
    I4=yield_curve.loc[:,'AA-']  
    I3=pow(I2*I4,1/2)  
    S1=I4*I4/I3  
 
    S2=S1+2  
    S3=S2+2  
    S4=S3+2  
 
    J1=S4+4  
    J2=J1+6  
    J3=J2+8 
    J4=J3+10  
            
    curve_allbenmark=pd.DataFrame()
    curve_allbenmark['Lv1']=G1
    curve_allbenmark['Lv2']=G2
    curve_allbenmark['Lv3']=G3
        
    curve_allbenmark['Lv4']=I1
    curve_allbenmark['Lv5']=I2  
    curve_allbenmark['Lv6']=I3
    curve_allbenmark['Lv7']=I4
    
    
    curve_allbenmark['Lv8']=S1     
    curve_allbenmark['Lv9']=S2
    curve_allbenmark['Lv10']=S3
    curve_allbenmark['Lv11']=S4
 
    curve_allbenmark['Lv12']=J1
    curve_allbenmark['Lv13']=J2 
    curve_allbenmark['Lv14']=J3   
    curve_allbenmark['Lv15']=J4
    curve_allbenmark=pd.concat([yield_curve.iloc[:,:-4],curve_allbenmark],axis=1)    
    return(curve_allbenmark)   

#MIR region boundaries construction
def curveAllBoundaryQ42(curve):
    curve_allbenmark=curveAllBenchmarkQ41(curve)
    curve_allbound=pd.DataFrame()
    for i,j in zip(newclasssymbol,range(3,18)):
        curve_allbound[i]=(curve_allbenmark.iloc[:,j]+curve_allbenmark.iloc[:,j+1])/2
    curve_allbound=pd.concat([curve_allbenmark.iloc[:,:3],curve_allbound],axis=1)   
    return(curve_allbound)


    
#%%

#benchmark(Government bond ect) YTM with the same maturity of bond
def bondReturnWithStandardReturnP50(bond,curve,maturitycol=['Maturity','YTM','CloseReturn'],durationcol=['Duration','Government_Bond','SemiGovernment_Bond']):
    bond_maturity=bond.loc[:,maturitycol]
    curve_duration=curve.loc[:,durationcol]
    X_bond_maturity=np.array(bond_maturity.loc[:,maturitycol[0]]).reshape(-1,1)     
    X_curve_duration=np.array(curve_duration.loc[:,durationcol[0]]).reshape(-1,1)  
    standardall_maturity=pd.DataFrame()
    for i in curve_duration.columns[1:]:
        Y_curve_duration=np.array(curve_duration.loc[:,i]) 
        model=NuSVR(nu=0.1) 
        model.fit(X_curve_duration,Y_curve_duration)
        standard_maturity=pd.DataFrame(model.predict(X_bond_maturity),index=bond_maturity.index,columns=[i])
        standardall_maturity=pd.concat([standardall_maturity,standard_maturity],axis=1)           
    all_maturity=pd.concat([bond_maturity,standardall_maturity],axis=1)
    return(all_maturity)
 
#Spread of benchmark(Government bond ect) YTM with the same maturity of bond
def bondReturnWithStandardSpreadP51(bond,curve,maturitycol=['Maturity','YTM','CloseReturn'],durationcol=['Duration','Government_Bond','SemiGovernment_Bond']):    
    all_return= bondReturnWithStandardReturnP50(bond,curve,maturitycol=maturitycol,durationcol=durationcol) 
    all_spread=pd.DataFrame([],index=bond.index)
    for i in maturitycol[1:]:
        for j in durationcol[1:]:
            all_spread['Spread('+i+'-'+j+')']=all_return.loc[:,i]-all_return.loc[:,j]  
    all_spread=pd.concat([all_return.iloc[:,0],all_spread],axis=1)
    return(all_spread)
    
    

#MIR and MIR index result
def mIRIndexAndRatingQ52(bond,bond_withboundary,col=['Maturity','YTM'],symbol=True):
    bond_withboundaryIn=bond_withboundary[(bond_withboundary['YTM']-bond_withboundary['Lv14|Lv15'])<=0]
    bond_withboundaryOut=bond_withboundary[(bond_withboundary['YTM']-bond_withboundary['Lv14|Lv15'])>0]  
    bond_diffboundaryIn=pd.DataFrame()  
    for i in range(len(bond_withboundaryIn.columns)-3):
        bond_diffboundaryIn[i]=(bond_withboundaryIn.iloc[:,1]-bond_withboundaryIn.iloc[:,i+2])/(bond_withboundaryIn.iloc[:,i+3]-bond_withboundaryIn.iloc[:,i+2])
    bond_indexIn=pd.DataFrame()
    bond_indexIn['RiskIndex2']=(bond_diffboundaryIn[bond_diffboundaryIn>=0]).min(axis=1)
    bond_indexIn['RiskIndex1']=bond_diffboundaryIn[bond_diffboundaryIn>=0].idxmin(axis=1)  
    bond_indexIn['BondRiskIndex']=bond_indexIn['RiskIndex1']+bond_indexIn['RiskIndex2']
    bond_indexOut=pd.DataFrame([],index=bond_withboundaryOut.index)
    bond_indexOut['BondRiskIndex']=15
    bond_index=pd.concat([bond_indexIn.iloc[:,2:3],bond_indexOut],axis=0)

    bond_index['MIR']=bond_index['BondRiskIndex']   
    bond_index.loc[bond_index['MIR'].isnull(),'MIR']=-1
    bond_index['MIR']=bond_index['MIR'].astype(int)+1
    bond_index.loc[bond_index['MIR']>14,'MIR']=15
    bond_index.loc[bond_index['BondRiskIndex'].isnull(),'BondRiskIndex']=0     
    bond_index=bond_index.reindex(bond_withboundary.index) 
    if symbol==True:
        bond_index['MIRsymbol']=bond_index['MIR'].map(lambda x: 'Lv'+str(x) )    
    return(bond_index)    
    

   
#all results, including MIR MIRindex, benchmark YTMs, benchmark YTMs spread
def BondResultQ5(curve,bond,col=['Maturity','YTM'],type='CorporateBond',alloutfile='2018-xx-xx__CorporateBond.csv'): #,outfile='日期_债券衍生数据.csv'
    curve_allboundary=curveAllBoundaryQ42(curve)
    col_curve=['Duration']+list(curve_allboundary.columns[-15:])
    print('## All bonds region boundary and region boundary spread results inculded##')       
    bond_withboundary=bondReturnWithStandardReturnP50(bond,curve_allboundary,maturitycol=['Maturity','YTM'],durationcol=col_curve)
    bond_withboundaryspread=bondReturnWithStandardSpreadP51(bond_withboundary,curve,maturitycol=bond_withboundary.columns.delete(2),durationcol=['Duration','Government_Bond'])
    print('## All bonds MIR result inculded##')         
    bond_indexandrating=mIRIndexAndRatingQ52(bond,bond_withboundary,col=['Maturity','YTM'],symbol=True)  
    bond_string=bond.copy()   
    bond_string['BondType']=type 
    bond_allresult=pd.concat([bond_string,bond_indexandrating,bond_withboundary.iloc[:,2:],bond_withboundaryspread.iloc[:,1:]],axis=1) 
    bond_allresult=bond_allresult.reset_index().set_index('Date').reset_index()
    bond_allresult.to_csv(alloutfile,encoding='utf_8_sig',index=None)
    return(bond_allresult)    



#%% Merge data
  
  
    

def ResultCollectionByP73(inputdatadir='2.3 MIR Result/',outputdatadir='2.4 All Time Results/',sortcol=['SecurityCode',  'Date']):
    start=time.time()
    inputdatalist=os.listdir(inputdatadir)  
    TempFile = 'Temp0_'+inputdatadir[3:-1]+'.csv'
    for i in inputdatalist: 
        inputdatapath = os.path.join(inputdatadir,i) 
        inputdatapath=codecs.open(inputdatapath,'r','utf-8')
        bond_input=pd.read_csv(inputdatapath,index_col=None)
        print('## Load and save %s'%i)        
        if i==inputdatalist[0]:
            bond_input.to_csv(TempFile,encoding='utf_8_sig',index=False,mode='w')
        else:
            bond_input.to_csv(TempFile,encoding='utf_8_sig',index=False,header=False,mode='a+')   
    print('## Read merged data')            
    temppath=codecs.open(TempFile,'r','utf-8')      
    bond_alltime=pd.read_csv(temppath,index_col=None)
    #reset index and sort data by securityCodes
    bond_alltime=bond_alltime.sort_values(by=sortcol,ascending=True)
    bond_alltime=bond_alltime.reset_index(drop=True)
    #define outputfile name 
    dataMax=bond_alltime['Date'].max()
    dataMin=bond_alltime['Date'].min()
    outputdata=dataMin+'~'+dataMax+inputdatadir[3:-3]+'AllTimeResults.csv'      
    bond_alltime.to_csv(outputdatadir+outputdata,encoding='utf_8_sig',index=None) 
    end=time.time()    
    print('！！！！！！！！Finish in %s ########'%(end-start))   
    return(bond_alltime)
    
    






    





       