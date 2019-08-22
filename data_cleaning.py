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
    dirty_data['Created_Datetime']= dirty_data['Created_Datetime'].apply(datetime.fromtimestamp)
    dirty_data['Funding_Deadline']= dirty_data['Funding_Deadline'].apply(datetime.fromtimestamp)
    dirty_data['Created_Month']= dirty_data['Created_Datetime']+ pd.offsets.MonthBegin(0)
    dirty_data['Deadline_Month']= dirty_data['Funding_Deadline']+ pd.offsets.MonthBegin(0)

def metrics(dirty_data):
    dirty_data['Pledge_Percentage']= dirty_data['Pledged']/ dirty_data['Goal']*100
    dirty_data['Funding_Duration']=(dirty_data['Funding_Deadline']-\
                                    dirty_data['Created_Datetime'])
    dirty_data['Trump_Election']=dirty_data['Created_Datetime']\
                                    >=datetime.strptime("2016-11-09",'%Y-%m-%d')
    
def date_filter(dirty_data,min_date="2016-07-01", max_date="2017-06-30"):
    dirty_data=dirty_data[(dirty_data['Created_Datetime']>=datetime.strptime(min_date,'%Y-%m-%d')) & (dirty_data['Created_Datetime']<=datetime.strptime(max_date,'%Y-%m-%d'))]
    
def full_clean(dirty_data):
    """
    This is the one function called that will run all the support functions.
    Assumption: Your data will be saved in a data folder and named "dirty_data.csv"

    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    data_type_changes(dirty_data)
    metrics(dirty_data)
    date_filter(dirty_data)
    dirty_data.to_pickle("data/cleaned_df.pickle")
    return dirty_data