import pandas as pd

def gen_trustdata():
    # Load in csv file
    trustdata = pd.read_csv('data/self-reported-trust-attitudes.csv')

    # Select only most recent trust data by country
    maxyear = trustdata.groupby('Entity')['Year'].max()
    trustdata['Most Recent Year'] = False
    for entry in range(0,len(trustdata)):
        print(entry, "\r", end="")
        x = trustdata.iloc[entry]['Entity']
        if trustdata.iloc[entry]['Year'] == maxyear[x]:
            trustdata['Most Recent Year'].iloc[entry] = True
    trustdata = trustdata[trustdata['Most Recent Year']==True]

    return trustdata

def trust_bins(dataset):
    trust_median = dataset['Trust in others (%)'].median()
    dataset['Trust Bin'] = dataset['Trust in others (%)'].map(lambda x : 'High' if x > trust_median else 'Low')
    return dataset

def add_trustdata(country_dataset):
    import iso3166
    trustdata = gen_trustdata()
    trustdata.index = trustdata['Code'].map(lambda x : iso3166.countries_by_alpha3[x][1])
    country_by_trust = pd.DataFrame.join(country_dataset, trustdata['Trust in others (%)'], how='inner')
    country_by_trust = trust_bins(country_by_trust)
    return country_by_trust
