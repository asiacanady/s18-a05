import pandas as pd
df = pd.read_csv('crimes.csv')
'''
#2. Create a series of the frequency of each type of crime. What are the three most
common types of crime? What are the three least common?
'''
each_type = df['Primary Type'].value_counts()
print('The three most common crimes are:', each_type.sort_values().tail(3))
print('The three least common crimes are:',each_type.sort_values().head(3))
