#this file generate a json file for data_cleaning.py from numerous json files
import json
import os
from datetime import datetime as dt
import gzip
import pandas as pd

def json_filter(data_folder, min_date="2016-07-01", max_date="2017-06-30"):
    list_of_jsons=os.listdir(data_folder)
    filtered_json= [i for i in list_of_jsons if dt.strptime(i[0:10],'%Y-%m-%d') >=dt.strptime(min_date,'%Y-%m-%d') and dt.strptime(i[0:10],'%Y-%m-%d') <=dt.strptime(max_date, '%Y-%m-%d')]
    return filtered_json

def json_generator(filename,dir=r"json_data/"):
    table=[]
    with gzip.GzipFile(dir+filename,'r') as f:
        for line in f:
            table.append(json.loads(line))
    data=json.loads(json.dumps(table))
    return data

def generate_kickstarter_csv(directory, save=False, output_file=None):
    kickstarter_list_of_dicts = []
    for ks in range(0, len(directory)):
        try:
            temp = {'Name' : directory[ks]['data']['name'],
                    'Category': directory[ks]['data']['category']['name'],
                    'Status' : directory[ks]['data']['state'],
                    'Country' : directory[ks]['data']['location']['country'],
                    'State' : directory[ks]['data']['location']['state'],
                    'Goal' : directory[ks]['data']['goal'],
                    'Pledged' : directory[ks]['data']['usd_pledged'],
                    'Backers' : directory[ks]['data']['backers_count'],
                    'Creater_ID': directory[ks]['data']['creator']['id'],
                    'Creater_Name': directory[ks]['data']['creator']['name'],
                    'Created_Datetime': directory[ks]['data']['created_at'],
                    'Funding_Deadline': directory[ks]['data']['deadline'],
                    }
            kickstarter_list_of_dicts.append(temp)
        except:
            #print(directory[ks]['data']['country'])
            pass
    kickstarter = pd.DataFrame(kickstarter_list_of_dicts)
    if save:
        kickstarter.to_pickle(r'data_{}.pickle'.format(output_file))
    return kickstarter

def kickstarter_concat(list_of_df, output_file):
    all_df=pd.concat(list_of_df, ignore_index=True)
    return all_df
