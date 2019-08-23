"""
This module is for your data cleaning.
It should be repeatable.

## PRECLEANING
There should be a separate script recording how you transformed the json api calls into a dataframe and csv.

## SUPPORT FUNCTIONS
There can be an unlimited amount of support functions.
Each support function should have an informative name and return the partially cleaned bit of the dataset.
"""
import pandas as pd
from datetime import datetime

def data_type_changes(dirty_data):
    dirty_data['Pledged'] = dirty_data['Pledged'].astype('float')
    dirty_data['Goal']=dirty_data['Goal'].astype('float')
    dirty_data['Created_Datetime']= dirty_data['Created_Datetime'].apply(datetime.fromtimestamp)
    dirty_data['Funding_Deadline']= dirty_data['Funding_Deadline'].apply(datetime.fromtimestamp)
    dirty_data['Created_Datetime']= pd.to_datetime(dirty_data['Created_Datetime'])
    dirty_data['Funding_Deadline']= pd.to_datetime(dirty_data['Funding_Deadline'])
    dirty_data['Created_Month']= dirty_data['Created_Datetime'].dt.date+ pd.offsets.MonthBegin(0)
    dirty_data['Deadline_Month']= dirty_data['Funding_Deadline'].dt.date+ pd.offsets.MonthBegin(0)

def metrics(data):
    dirty_data=data[data['Status'].isin(["successful","failed"])]
    dirty_data['Pledge_Percentage']= dirty_data['Pledged']/ dirty_data['Goal']*100
    dirty_data.loc[dirty_data['Pledge_Percentage']>=1000,'Pledge_Percentage']=1000
    dirty_data['Funding_Duration']=(dirty_data['Funding_Deadline']-\
                                    dirty_data['Created_Datetime'])
    dirty_data['Funding_Status']=(dirty_data['Status']=='successful').astype(int)
    dirty_data.sort_values(['Created_Month'],inplace=True)
    dirty_data['Serial_Entrepreneur']=dirty_data.groupby(['Creater_ID'])['Funding_Status'].transform('cumsum')
    dirty_data['Year']=dirty_data['Created_Month'].dt.year
    return dirty_data
    
def date_filter_trump(dirty_data,min_date="2016-07-01", max_date="2017-03-01"):
    dirty_data['Trump_Election']=dirty_data['Created_Month']\
                                    >=pd.to_datetime("2016-11-01")
    dirty_data=dirty_data[((dirty_data['Created_Month']>=pd.to_datetime(min_date))\
                                           & (dirty_data['Created_Month']<=pd.to_datetime(max_date)))]
    dirty_data['Entrepreneur_Experience']=dirty_data.groupby('Creater_ID')['Serial_Entrepreneur'].\
                                            transform(lambda x: pd.cut(x, bins=[0,1,5,100], \
                                            labels=['Rookie','Experienced','Expert']))
    return dirty_data

def category_mapping(dirty_data, category):
    category.fillna(0, inplace=True)
    category=pd.melt(category,id_vars="Category")
    category.columns
    category=category[category['value']!=0].drop('value',axis=1)
    category.drop_duplicates('Category', inplace=True)
    category.columns=['Category','Sup_Category']
    return dirty_data.merge(category, on='Category')

def full_clean(dirty_data, category_data):
    """
    This is the one function called that will run all the support functions.
    Assumption: Your data will be saved in a data folder and named "dirty_data.csv"

    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    data_type_changes(dirty_data)
    dirty_data=metrics(dirty_data)
    dirty_data=category_mapping(dirty_data,category_data)
    dirty_data=date_filter_trump(dirty_data)
    dirty_data.to_pickle("data/cleaned_df.pickle")
    return dirty_data