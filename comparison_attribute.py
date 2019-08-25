import pandas as pd
import iso3166

def gen_trustdata(trustdata):
    # Load in csv file
    # Select only most recent trust data by country
    trustdata.sort_values(by=['Entity','Year'], inplace=True,ascending=[True,True])
    trustdata=trustdata[trustdata['Year']>=2010]
    trustdata.drop_duplicates("Entity",keep='last')
    print('''We use the year(s) {} in the trust data'''.format(trustdata.Year.unique()))

def trust_bins(trustdata,bins=[0,0.33,0.66,1],label=['Low','Medium','High']):
    trustdata['Trust_Rank']=trustdata['Trust in others (%)'].rank(pct=True)
    trustdata['Trust_Bin']=pd.cut(trustdata['Trust_Rank'], bins=bins, labels=label)

def add_trustdata(trustdata, country_dataset):
    gen_trustdata(trustdata)
    trust_bins(trustdata)
    trustdata['Country'] = trustdata['Code'].map(lambda x : iso3166.countries_by_alpha3[x][1])
    print("There are {} countries in the trust data".format(trustdata.Country.nunique()))
    country_by_trust = country_dataset.merge(trustdata[['Trust_Bin','Trust_Rank','Country']], how='inner')
    print('''After merge, there are {} countries in the country-trust-funding data'''.format(country_by_trust.Country.nunique()))
    return country_by_trust
