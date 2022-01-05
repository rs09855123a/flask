from numpy.core.fromnumeric import sort
import pandas as pd


def get_pm25(sort=False):
    url = 'https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv'
    df = pd.read_csv(url).dropna()
    columns = ['Site', 'county', 'PM25']
    values = df[columns].values.tolist()
    update_time = df['DataCreationDate'][0]

    if sort:
        values = sorted(values, key=lambda x: x[-1], reverse=True)
    return columns, values, update_time
