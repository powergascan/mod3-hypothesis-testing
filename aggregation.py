#this file contains function for aggregating our data

#the purpose of these functions is for better visualization
#all functions are supposed to be general enough to groupby at any level

def Aggregate_Mean(dataset,level):
    grouped_data = dataset.groupby(level).mean().reset_index()
    return grouped_data

def Aggregate_Sum(dataset,level):
    grouped_data = dataset.groupby(level).sum().reset_index()
    return grouped_data

def Aggregate_Median(dataset,level):
    grouped_data = dataset.groupby(level).median().reset_index()
    return grouped_data