from numpy.core.fromnumeric import sort
import pandas as pd

url = 'https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv'
df = pd.read_csv(url).dropna()


def get_pm25(sort=False):
    columns = ['Site', 'county', 'PM25']
    values = df[columns].values.tolist()
    update_time = df['DataCreationDate'][0]

    if sort:
        values = sorted(values, key=lambda x: x[-1], reverse=True)
    return columns, values, update_time


def get_six_pm25():
    six_pm25 = {}
    six_cities = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市"]
    for city in six_cities:
        six_pm25[city] = round(df.groupby(
            'county').get_group(city)['PM25'].mean(), 2)
    return six_pm25


def get_county_pm25(county):

    return df.groupby('county').get_group(county)[['Site', 'PM25']].values.tolist()


def get_county():
    countys = []
    for county in df['county']:
        if county not in countys:
            countys.append(county)
    return countys
