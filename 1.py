import pandas as pd
from timezonefinder import TimezoneFinder
from pytz import timezone
from datetime import datetime
from collections import Counter


tf = TimezoneFinder()

df = pd.read_csv("./data.csv")



for index,row in df.iterrows():
    if row['Timezone'] == '\\N':
        tzinfo = timezone(tf.timezone_at(lng=row['Longitude'], lat=row['Latitude']))
        dt = datetime.now(tzinfo)
        print(tzinfo)
        print(dt.utcoffset().total_seconds()/3600)
        df.set_value(index, 'Timezone', dt.utcoffset().total_seconds()/3600)


mapped = Counter(df['Country'])
print(mapped)
print(len(mapped))

df['Country New Values'] = ""

for index,row in df.iterrows():
    if mapped[row['Country']] >= 280:
        df.set_value(index, 'Country New Values', row['Country'])
    else:
        df.set_value(index, 'Country New Values', 'Others')

mappedNew = Counter(df['Country New Values'])
print(mappedNew)
print(len(mappedNew))

df.to_csv('data_mod.csv', index=False)

