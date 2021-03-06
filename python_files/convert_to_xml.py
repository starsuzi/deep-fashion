import pandas as pd
import csv
import numpy as np
import module

df_final= pd.read_csv('./csv/final_csv_for_xml.csv')
df_final = df_final.fillna('')

df_shirt = df_final.groupby('category_name').get_group('shirt')
df_coat = df_final.groupby('category_name').get_group('coat')
df_dress = df_final.groupby('category_name').get_group('dress')
df_jacket = df_final.groupby('category_name').get_group('jacket')
df_jumper = df_final.groupby('category_name').get_group('jumper')
df_pants = df_final.groupby('category_name').get_group('pants')
df_skirt = df_final.groupby('category_name').get_group('skirt')
df_winterJacket = df_final.groupby('category_name').get_group('winter jacket')

module.create_xml('shirt',df_shirt)
module.create_xml('coat',df_coat)
module.create_xml('dress',df_dress)
module.create_xml('jacket',df_jacket)
module.create_xml('jumper',df_jumper)
module.create_xml('pants',df_pants)
module.create_xml('skirt',df_skirt)
module.create_xml('winter jacket',df_winterJacket)
