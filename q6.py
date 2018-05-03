import pandas as pd
df = pd.read_csv('crimes.csv')
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

crimes= len(df_weapons)/len(df)
print('Proportion of crimes involving a weapon', crimes)
