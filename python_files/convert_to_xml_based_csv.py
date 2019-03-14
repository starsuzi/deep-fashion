import pandas as pd
import csv
import numpy as np

df_attr_chosen= pd.read_csv('./csv/merged_by_img_name.csv')
df_bbox= pd.read_csv('./csv/bbox.csv')

lst_img = df_attr_chosen['image_name'].tolist()

df_attr_chosen.insert(3, 'pattern', '')
df_attr_chosen.insert(3, 'colors', '')
df_attr_chosen.insert(3, 'season', '')
df_attr_chosen.insert(3, 'gender', '')
df_attr_chosen.insert(3, 'sleeves', '')

set_striped=set(df_attr_chosen.loc[df_attr_chosen['striped'] == 1]['image_name'])
set_floral = set(df_attr_chosen.loc[df_attr_chosen['floral'] == 1]['image_name'])
set_dotted = set(df_attr_chosen.loc[df_attr_chosen['dotted'] == 1]['image_name'])
set_checker = set(df_attr_chosen.loc[df_attr_chosen['checker'] == 1]['image_name'])
set_others = set(df_attr_chosen.loc[df_attr_chosen['others'] == 1]['image_name'])

for i,img_name in enumerate(df_attr_chosen['image_name']):
    #print(i)
    if img_name in set_striped:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('pattern')] = 'striped'
    elif img_name in set_floral:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('pattern')] = 'floral'
    elif img_name in set_dotted:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('pattern')] = 'dotted'
    elif img_name in set_checker:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('pattern')] = 'checker' 
    elif img_name in set_others:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('pattern')] = 'others'         
    else:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('pattern')] = ''

set_red=set(df_attr_chosen.loc[df_attr_chosen['red'] == 1]['image_name'])
set_pink = set(df_attr_chosen.loc[df_attr_chosen['pink'] == 1]['image_name'])
for i,img_name in enumerate(df_attr_chosen['image_name']):
    if img_name in set_red:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('colors')] = 'red'
    elif img_name in set_pink:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('colors')] = 'pink'
    else:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('colors')] = ''

set_woman=set(df_attr_chosen.loc[df_attr_chosen['woman'] == 1]['image_name'])
for i,img_name in enumerate(df_attr_chosen['image_name']):
    #print(i)
    if img_name in set_woman:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('gender')] = 'woman'
    else:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('gender')] = ''

set_summer = set(df_attr_chosen.loc[df_attr_chosen['summer'] == 1]['image_name'])
set_winter = set(df_attr_chosen.loc[df_attr_chosen['winter'] == 1]['image_name'])
for i,img_name in enumerate(df_attr_chosen['image_name']):
    #print(i)
    if img_name in set_summer:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('season')] = 'summer'    
    elif img_name in set_winter:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('season')] = 'winter'    
    else:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('season')] = ''

set_short = set(df_attr_chosen.loc[df_attr_chosen['short'] == 1]['image_name'])
set_long = set(df_attr_chosen.loc[df_attr_chosen['long'] == 1]['image_name'])
set_shortSleeves = set(df_attr_chosen.loc[df_attr_chosen['short sleeves'] == 1]['image_name'])
set_longSleeves = set(df_attr_chosen.loc[df_attr_chosen['long sleeves'] == 1]['image_name'])
set_noSleeves = set(df_attr_chosen.loc[df_attr_chosen['no sleeves'] == 1]['image_name'])
for i,img_name in enumerate(df_attr_chosen['image_name']):
    #print(i)
    if img_name in set_short:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('sleeves')] = 'short'
    elif img_name in set_long:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('sleeves')] = 'long'
    elif img_name in set_shortSleeves:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('sleeves')] = 'short sleeves'
    elif img_name in set_longSleeves:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('sleeves')] = 'long sleeves'
    elif img_name in set_noSleeves:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('sleeves')] = 'no sleeves'    
    else:
        df_attr_chosen.iat[i, df_attr_chosen.columns.get_loc('sleeves')] = ''

df_final = df_attr_chosen.iloc[:,:8]

df_final_bbox=pd.merge(df_final, df_bbox)

#final_csv_for_xml.csv
file_name = "final_csv_for_xml.csv"
df_final_bbox.to_csv("./csv/"+file_name, index=None)


