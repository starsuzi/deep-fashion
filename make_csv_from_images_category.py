import numpy as np
import pandas as pd
import csv
import os, glob

df_attr_combined = pd.read_csv('./Anno/changed/etri/attr_combined.csv')

def createCategoryDataFrame(lst_category_fname, category_label, category_name):
    df_category = pd.DataFrame(lst_category_fname, columns=['image_name'])
    df_category.insert(1,'category_label', category_label)
    df_category.insert(1,'category_name', category_name)
    return df_category

lst_coat_fname = [f.name[:-4] for f in os.scandir('./coat') if f.is_file()]
lst_dress_fname = [f.name[:-4] for f in os.scandir('./dress') if f.is_file()]
lst_jacket_fname = [f.name[:-4] for f in os.scandir('./jacket') if f.is_file()]
lst_jumper_fname = [f.name[:-4] for f in os.scandir('./jumper') if f.is_file()]
lst_pants_fname = [f.name[:-4] for f in os.scandir('./pants') if f.is_file()]
lst_shirt_fname = [f.name[:-4] for f in os.scandir('./shirt') if f.is_file()]
lst_skirt_fname = [f.name[:-4] for f in os.scandir('./skirt') if f.is_file()]
lst_winterJacket_fname = [f.name[:-4] for f in os.scandir('./winter jacket') if f.is_file()]

df_shirt = createCategoryDataFrame(lst_shirt_fname, 0, 'shirt')
df_jumper = createCategoryDataFrame(lst_jumper_fname, 1, 'jumper')
df_jacket = createCategoryDataFrame(lst_jacket_fname, 2, 'jacket')
#df_vest = createCategoryDataFrame(lst_vest_fname, 3, 'Vest')
df_winterJacket = createCategoryDataFrame(lst_winterJacket_fname, 4, 'winter jacket')
df_coat = createCategoryDataFrame(lst_coat_fname, 5, 'coat')
df_dress = createCategoryDataFrame(lst_dress_fname, 6, 'dress')
df_pants = createCategoryDataFrame(lst_pants_fname, 7, 'pants')
df_skirt = createCategoryDataFrame(lst_skirt_fname, 8, 'skirt')

df_shirt_attr_combined = pd.merge(df_shirt, df_attr_combined)
df_jumper_attr_combined = pd.merge(df_jumper, df_attr_combined)
df_jacket_attr_combined = pd.merge(df_jacket, df_attr_combined)
df_winterJacket_attr_combined = pd.merge(df_winterJacket, df_attr_combined)
df_coat_attr_combined = pd.merge(df_coat, df_attr_combined)
df_dress_attr_combined = pd.merge(df_dress, df_attr_combined)
df_pants_attr_combined = pd.merge(df_pants, df_attr_combined)
df_skirt_attr_combined = pd.merge(df_skirt, df_attr_combined)

df_attr_category_combined = pd.concat([df_shirt_attr_combined, df_jumper_attr_combined, df_jacket_attr_combined, df_winterJacket_attr_combined, df_coat_attr_combined, df_dress_attr_combined, df_pants_attr_combined, df_skirt_attr_combined],
                                      ignore_index=True)

#attr_category_combined.csv
file_name = "attr_category_combined_asdf.csv"
#df_attr_category_combined.to_csv("./Anno/changed/etri/"+file_name, index=None)
df_attr_category_combined.to_csv("./"+file_name, index=None)