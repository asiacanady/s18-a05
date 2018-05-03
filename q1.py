import pandas as pd
df = pd.read_csv('crimes.csv')
'''
#1. How many crimes were recorded in 2017? What was the crime rate
(defined as the number of crimes per 1000 capita-- find an estimate of Chicago's
population online)?
'''
df.columns
df['Primary Type'].shape
population = 2705000
crime = 266980

crime_rate = round((crime/population)*1000, 2)
print('The crime rate per capita is:', crime_rate)
