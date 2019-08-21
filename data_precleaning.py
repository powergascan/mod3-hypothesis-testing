def generate_kickstarter_csv(url, file_name):
    import json
    f = open(url, encoding='utf-8')
    directory = []
    for line in f:
        directory.append(json.loads(line))

    kickstarter_list_of_dicts = []
    for ks in range(0, len(directory)):
        temp = {'Name' : directory[ks]['data']['name'],
                    'Category': directory[ks]['data']['category']['name'],
                    'State' : directory[ks]['data']['state'],
                    'Country' : directory[ks]['data']['country'],
                    'Goal' : directory[ks]['data']['goal'],
                    'Pledged' : directory[ks]['data']['usd_pledged'],
                    'Backers' : directory[ks]['data']['backers_count']
                   }
        kickstarter_list_of_dicts.append(temp)

    import pandas as pd
    kickstarter = pd.DataFrame(kickstarter_list_of_dicts)

    kickstarter.to_csv(r'data\{}.csv'.format(file_name), index='False')
    print('csv saved to data\\{}.csv'.format(file_name))
