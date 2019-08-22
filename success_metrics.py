def pledge_rate_mean(dataset,level):
    country_grouped = dataset.groupby(level).mean().reset_index()
    return country_grouped
