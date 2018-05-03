import pandas as pd
df = pd.read_csv('crimes.csv')

'''
#3. Create a series of the proportion of each type of crime that results in arrest.
Which crime type is most likely to result in arrest? Hint:

First subset the data to rows where Arrest is True.
Use this to calculate the number of crimes of each type that lead to arrest.
Divide this by the series you created in 2
Finally, sort the values
'''

arrest_counts = df[df['Arrest'] == True]['Primary Type'].value_counts()
denominator = df['Primary Type'].value_counts()
proportions = arrest_counts/denominator
print('A List of crimes and their likelihood to result in arrest', proportions.sort_values())
print('The crimes most likely to result in arrest: Prostitution, Public Indency, Gambling, Liquor Law Violation')
