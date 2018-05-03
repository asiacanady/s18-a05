
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

crime_rate = (crime/population)*1000

'''
#2. Create a series of the frequency of each type of crime. What are the three most
common types of crime? What are the three least common?
'''
df['Primary Type'].value_counts()
#Most common crime = Theft, Battery, Criminal Damage
#Least Common crime = Non-Criminal, Human Trafficking, Public Indency

'''
#3. Create a series of the proportion of each type of crime that results in arrest. Which crime type is most likely to result in arrest? Hint:

First subset the data to rows where Arrest is True.
Use this to calculate the number of crimes of each type that lead to arrest.
Divide this by the series you created in 2
Finally, sort the values
'''

arrest_counts = df[df['Arrest'] == True]['Primary Type'].value_counts()
denominator = df['Primary Type'].value_counts()
proportions = arrest_counts/denominator
print(proportions.sort_values())

'''
#4. Among those types of crime for which there are at least 1000 incidents,
which type is most likely to result in arrest?

Hint: Create a boolean series whose index is crime type and value is whether the
count is at least 1000. Use that to subset your answer to 3 and then sort.
'''
proportion_1000 = proportions[df['Primary Type'].value_counts() >= 1000]
print(proportion_1000.sort_values().tail(3))

'''
#5. What is the number of the community area with the most homicides in 2017?
How many were there? What is the community area's name? (You can find a mapping
of community area numbers to names online.)
'''
 homicides = df[df['Primary Type'] == 'HOMICIDE']
 communityarea = homicides['Community Area'].value_counts()
 #The number of the community area with the most homicides is number #25
 #There were 81 homicides in neighborhood 25.
 #Austin is the neighborhood with the most crimes.

'''
#6. Create a boolean series indicating whether each crime involved a weapon.
Then calculate the percentage of crimes involving a weapon. Hint: Look for
descriptions containing words like 'WEAPON', 'GUN', and 'ARM'; but be careful
because some descriptions contain 'NO WEAPON'.
'''
no_weapon = df['Description'].str.find('NO WEAPON') > 0
df_weapons = df[~no_weapon]

weapon = df_weapons['Description'].str.find('WEAPON') > 0
gun = df_weapons['Description'].str.find('GUN') > 0
firearm = df_weapons['Description'].str.find('ARM') > 0
knife = df_weapons['Description'].str.find('KNIFE') > 0
knives = df_weapons['Description'].str.find('KNIVES') > 0

df_weapons = df_weapons[(weapon) | (gun) | (firearm) | (knife) | (knives)]

len(df_weapons)/len(df)
