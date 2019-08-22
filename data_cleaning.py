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

def metrics(dirty_data):
    dirty_data['Pledge_Percentage']= dirty_data['Pledged']/ dirty_data['Goal']*100
    dirty_data['Funding_Duration']=(dirty_data['Funding_Deadline']-dirty_data['Created_Datetime'])
    
def full_clean(dirty_data):
    """
    This is the one function called that will run all the support functions.
    Assumption: Your data will be saved in a data folder and named "dirty_data.csv"

    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    #dirty_data = pd.read_csv("./data/dirty_data.csv")
    data_type_changes(dirty_data)
    metrics(dirty_data)
    #dirty_data.to_csv('./data/cleaned_for_testing.csv')
    return dirty_data