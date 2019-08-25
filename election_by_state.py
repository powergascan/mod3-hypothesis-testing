import pandas as pd

def DT_Effect(election_data, labels=['US Blue','US Red']):
    election_data=election_data[election_data['year'].isin([2012, 2016])]
    election_data=election_data[election_data['party'].isin(['republican'])]
    election_data.sort_values(['state_po','year'],inplace=True)
    election_data['Vote_Percent']=election_data['candidatevotes']/election_data['totalvotes']
    election_data['Vote_Percent_shift']=election_data.groupby(['state'])['Vote_Percent'].shift(1)
    election_data=election_data[~election_data['Vote_Percent_shift'].isnull()]
    election_data['DT_Effect']=election_data['Vote_Percent']-election_data['Vote_Percent_shift']
    election_data=election_data[['state_po','Vote_Percent','DT_Effect']]
    election_data=election_data[~election_data['DT_Effect'].isnull()]
    election_data.rename(columns={"state_po":"State"},inplace=True)
    election_data['Ideology_Bin']=pd.qcut(election_data['DT_Effect'], 2, labels=labels)
    return election_data