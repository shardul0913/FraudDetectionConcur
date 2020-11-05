import smogn #Synthetic Minority Over-Sampling Technique for Regression with Gaussian Noise
import pandas as pd

def dataTrans(dfOg):
 
    dfOg['Stay'] = (dfOg['travel_end_date'] - dfOg['travel_end_date']) / pd.offsets.Day(1)
    
    dfSmgn = dfOg.drop(columns=['travel_end_date','travel_start_date','date','approval_num','approval_date'])

    housing_smogn = smogn.smoter(
        data = dfSmgn,  ## pandas dataframe
        y = 'total_expense',  ## string ('header name')
        k = 4,                    ## positive integer (k < n) 
    )
    
    dfJoin = dfOg[['travel_start_date','expense_num']]
    alldf = housing_smogn.merge(dfJoin, on='expense_num', how='left')
    alldf = alldf.set_index('travel_start_date')
    
    return alldf
