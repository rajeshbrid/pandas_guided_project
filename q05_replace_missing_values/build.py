# %load q05_replace_missing_values/build.py
import pandas as pd
import numpy as np
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.pandas_guided_project.q04_mapping.build import q04_mapping

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'

def q05_replace_missing_values(path1,path2):
    df1 = pd.read_excel(path1)
    df1['total']=df1['Jan']+df1['Feb']+df1['Mar']
    df1.loc[len(df1),:]=df1.sum()
    df2 = pd.read_csv(path2)
    
    abbr_dict = dict(zip(df2.iloc[:,[1,6]]['United States of America'],df2.iloc[:,[1,6]]['Unnamed: 6']))
    
    df1.iloc[:,6]  = df1['state'].map(abbr_dict)
    df1.iloc[6,6]  = 'MS'
    df1.iloc[10,6] = 'TN'
    
    return df1

#print(q05_replace_missing_values(path1,path2).shape)
# q05_replace_missing_values(path1,path2)



