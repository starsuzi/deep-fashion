import numpy as np
import pandas as pd
import csv
import module

df_attr_combined = pd.read_csv('./Anno/changed/etri/attr_combined.csv')
df_attr_category_combined = pd.read_csv('./Anno/changed/etri/attr_category_combined.csv')

#basically given attributes
#check if bascially given attributes(etri's attributes) are in DeepFashion dataset's attributes
print("===basically given attributes===")

lst_color = ['white ', 'black ', 'gray ', 'pink ', 'red ', 'green ', 'blue ', 'brown ', 'navy ', 'beige ', 'yellow ', 'purple ', 'orange ']
lst_gender = ['man ', 'woman ']
lst_sleeves = ['short sleeves ', 'long sleeves ', 'no sleeves ', 'short ', 'long ']
lst_season = ['spring ', 'summer ', 'autumn ', 'winter ']
lst_pattern = ['single ', 'checker ', 'dotted ', 'floral ', 'striped ']

module.isAttribute(lst_color, df_attr_combined)

#Check similar columns' images by name
#for example, check all attributes that contain 'dot'.
#the result is ['dot ', 'dots ', 'dotted ', 'polka dot ']
#then, check if they really are same as ETRI's dotted by random images from plotRandomImage()

print("\n===Check similar columns' images by name===")
#sleeve
print([col for col in df_attr_combined if 'sleeve' in col])
#long
print([col for col in df_attr_combined if 'long' in col])
#checker
print([col for col in df_attr_combined if 'check' in col])
#dot
print([col for col in df_attr_combined if 'dot' in col])
#floral
print([col for col in df_attr_combined if 'flo' in col])
#stripe
print([col for col in df_attr_combined if 'stripe' in col])
#other print
#print([col for col in df_attr_combined if 'print' in col])

#sleeveless
print([col for col in df_attr_combined if 'strap' in col])
#short
print([col for col in df_attr_combined if 'mini' in col])
#long
print([col for col in df_attr_combined if 'maxi' in col] )
#rose
print([col for col in df_attr_combined if 'rose' in col])
#botanical
print([col for col in df_attr_combined if 'botanical' in col])
#daisy
print([col for col in df_attr_combined if 'daisy' in col])