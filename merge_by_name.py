import numpy as np
import pandas as pd
import csv
import module
import os

#module.plotRandomImage_by_imgName("./shirt/", 'Floral')
df_name_merged = pd.read_csv('./asdfasdf.csv')

lst_floral = []
lst_striped = []
lst_dot = []
lst_checker = []

lst_floral, lst_striped, lst_dot, lst_checker = module.find_pattern_in_name("./dress/",lst_floral, lst_striped, lst_dot, lst_checker)
lst_floral, lst_striped, lst_dot, lst_checker = module.find_pattern_in_name("./skirt/",lst_floral, lst_striped, lst_dot, lst_checker)
lst_floral, lst_striped, lst_dot, lst_checker = module.find_pattern_in_name("./shirt/",lst_floral, lst_striped, lst_dot, lst_checker)
lst_floral, lst_striped, lst_dot, lst_checker = module.find_pattern_in_name("./pants/",lst_floral, lst_striped, lst_dot, lst_checker)
lst_floral, lst_striped, lst_dot, lst_checker = module.find_pattern_in_name("./jumper/",lst_floral, lst_striped, lst_dot, lst_checker)
lst_floral, lst_striped, lst_dot, lst_checker = module.find_pattern_in_name("./winter jacket/",lst_floral, lst_striped, lst_dot, lst_checker)
lst_floral, lst_striped, lst_dot, lst_checker = module.find_pattern_in_name("./jacket/",lst_floral, lst_striped, lst_dot, lst_checker)
lst_floral, lst_striped, lst_dot, lst_checker = module.find_pattern_in_name("./coat/",lst_floral, lst_striped, lst_dot, lst_checker)

for i,img_name in enumerate(df_name_merged['image_name']):
    if img_name in lst_floral:
        df_name_merged.iat[i, df_name_merged.columns.get_loc('floral')] = 1
    elif img_name in lst_striped:
        df_name_merged.iat[i, df_name_merged.columns.get_loc('striped')] = 1
    elif img_name in lst_dot:
        df_name_merged.iat[i, df_name_merged.columns.get_loc('dotted')] = 1
    elif img_name in lst_checker:
        df_name_merged.iat[i, df_name_merged.columns.get_loc('checker')] = 1

lst_short_sleeves = []
lst_long_sleeves = []
lst_no_sleeves = []

lst_short_sleeves, lst_long_sleeves, lst_no_sleeves = module.find_sleeves_in_name("./dress/",lst_short_sleeves, lst_long_sleeves, lst_no_sleeves)
lst_short_sleeves, lst_long_sleeves, lst_no_sleeves = module.find_sleeves_in_name("./jacket/",lst_short_sleeves, lst_long_sleeves, lst_no_sleeves)
lst_short_sleeves, lst_long_sleeves, lst_no_sleeves = module.find_sleeves_in_name("./jumper/",lst_short_sleeves, lst_long_sleeves, lst_no_sleeves)
lst_short_sleeves, lst_long_sleeves, lst_no_sleeves = module.find_sleeves_in_name("./shirt/",lst_short_sleeves, lst_long_sleeves, lst_no_sleeves)
lst_short_sleeves, lst_long_sleeves, lst_no_sleeves = module.find_sleeves_in_name("./coat/",lst_short_sleeves, lst_long_sleeves, lst_no_sleeves)
lst_short_sleeves, lst_long_sleeves, lst_no_sleeves = module.find_sleeves_in_name("./winter jacket/",lst_short_sleeves, lst_long_sleeves, lst_no_sleeves)
lst_short_sleeves, lst_long_sleeves, lst_no_sleeves = module.find_sleeves_in_name("./skirt/",lst_short_sleeves, lst_long_sleeves, lst_no_sleeves)
lst_short_sleeves, lst_long_sleeves, lst_no_sleeves = module.find_sleeves_in_name("./pants/",lst_short_sleeves, lst_long_sleeves, lst_no_sleeves)

df_name_merged.insert(3, 'short sleeves', -1 )

for i,img_name in enumerate(df_name_merged['image_name']):
    if img_name in lst_short_sleeves:
        df_name_merged.iat[i, df_name_merged.columns.get_loc('short sleeves')] = 1
    elif img_name in lst_long_sleeves:
        df_name_merged.iat[i, df_name_merged.columns.get_loc('long sleeves')] = 1
    elif img_name in lst_no_sleeves:
        df_name_merged.iat[i, df_name_merged.columns.get_loc('no sleeves')] = 1

#df_name_merged.csv
file_name = "name_merged.csv"
df_name_merged.to_csv("./"+file_name, index=None)