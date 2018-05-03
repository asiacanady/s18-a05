import pandas as pd
df = pd.read_csv('crimes.csv')
'''
#5. What is the number of the community area with the most homicides in 2017?
How many were there? What is the community area's name? (You can find a mapping
of community area numbers to names online.)
'''
homicides = df[df['Primary Type'] == 'HOMICIDE']
communityarea = homicides['Community Area'].value_counts()
sorted_homicides = communityarea.sort_values()
top_homicide = sorted_homicides.tail(1)
print('The community with the Most Homicides is Austin (community number# then homicide count):', top_homicide)
 #The number of the community area with the most homicides is number #25
 #There were 81 homicides in neighborhood 25.
 #Austin is the neighborhood with the most crimes.
