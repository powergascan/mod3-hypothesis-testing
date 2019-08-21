def pledge_rate_mean(dataset):
    country_grouped = dataset.groupby(['Country']).mean()
    country_grouped['Pledge Rate'] = country_grouped['Pledged'] / country_grouped['Goal']
    return country_grouped
