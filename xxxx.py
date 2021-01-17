import requests
pname = "pikachu"
response = requests.get("https://pokeapi.co/api/v2/pokemon/"+ pname)
print(response)

import pandas as pd
data3 = [['Gdynia',100],['Gdansk',120],['Sopot',130], ['Gdynia',90],
['Gdansk',100]]
df3 = pd.DataFrame(data3, columns=['City','Sales'])

print(df3.groupby('City').agg(['count', 'first', 'last', 'mean', 'max', 'min', 'sum']))

def SampleFunction(a, b):
    a = 3
    c = a + b
    return(c)

print(SampleFunction(a= 2, b = 3))

x = ["a", "b", "c", "d"]
y = ["w", "x", "y", "z"]
print(x + y)

data1 = [['Gdansk', 10, 100], ['Sopot',12, 345], ['Gdynia', 20, 500]]
SampleDF = pd.DataFrame(data1, columns=['City', 'Sales', 'Income'])
print(SampleDF)
print(SampleDF.iloc[1,2])

x = [1,2,3]
a,b,c = x
print(a,b,c)


date1 = pd.Series(pd.date_range('2012-1-1 12:00:00', periods=7, freq='M'))
date2 = pd.Series(pd.date_range('2013-3-11 21:45:00', periods=7, freq='W'))
dates_df = pd.DataFrame(dict(Start_date = date1, End_date = date2))
dates_df['YM'] = dates_df['Start_date'].map(lambda x: x.month).apply(str) + "-" + dates_df['Start_date'].map(lambda x: x.year).apply(str)
print(dates_df)

t = pd.datetime.strptime('2018-12-13', "%Y-%m-%d")
t1 = pd.datetime.strptime('2018-11-10', "%Y-%m-%d")
t2 = t - t1
print(t2.days//30)


