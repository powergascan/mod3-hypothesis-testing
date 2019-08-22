#this file contains function for aggregating our data

#the purpose of these functions is for better visualization
#all functions are supposed to be general enough to groupby at any level

def Aggregate_Mean(dataset,level):
    grouped_data = dataset.groupby(level).mean().reset_index()
    #drop redundent vars
    grouped_data.drop(['Creater_ID','Creater_Name',\
                       'Funding_Deadline','Created_Datetime'], axis=1, inplace=True)
    return grouped_data

def Aggregate_Sum(dataset,level):
    grouped_data = dataset.groupby(level).sum().reset_index()
    #drop redundent vars
    grouped_data.drop(['Creater_ID','Creater_Name',\
                       'Funding_Deadline','Created_Datetime'], axis=1, inplace=True)
    return grouped_data
