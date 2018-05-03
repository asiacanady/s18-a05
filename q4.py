import pandas as pd
df = pd.read_csv('crimes.csv')
'''
#4. Among those types of crime for which there are at least 1000 incidents,
which type is most likely to result in arrest?

Hint: Create a boolean series whose index is crime type and value is whether the
count is at least 1000. Use that to subset your answer to 3 and then sort.
'''
arrest_counts = df[df['Arrest'] == True]['Primary Type'].value_counts()
denominator = df['Primary Type'].value_counts()
proportions = arrest_counts/denominator

proportion_1000 = proportions[df['Primary Type'].value_counts() >= 1000]
print('Three crimes that occur at least 10000 times that are most likely to result in arrest:', proportion_1000.sort_values().tail(3))
