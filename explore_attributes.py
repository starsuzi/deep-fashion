import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random


def isAttribute(lst_attribute):
    for col in lst_attribute:
        try:
            df_attr_combined[col]
            print("'"+col+"' exists")
        except :
            print("'"+col+"' doesn't exist")
            pass

def plotRandomImage(attribute, img_num, df):
    print(attribute+'attribute')
    img_files = []
    dict_imgs = dict(zip(df.loc[df[attribute] == 1]['image_name'], df.loc[df[attribute] == 1]['category_name']))
    print(str(len(dict_imgs))+' images')
    lst_rand_imgs = random.sample(list(dict_imgs.items()), img_num)
    
    for tuple_img in lst_rand_imgs:
        img=mpimg.imread('./'+tuple_img[1]+'/'+tuple_img[0]+'.jpg')
        img_files.append(img)
    
    col_num = 4
    row_num = ((img_num // col_num)+1) if (img_num % col_num) != 0 else (img_num // col_num)
    
    fig, axes = plt.subplots(nrows=row_num, ncols=col_num, figsize=(20,20))
    
    for idx, img_file in enumerate(img_files):
        row = idx // col_num
        col = idx % col_num
        
        axes[row, col].axis("off")
        axes[row, col].imshow(img_file, cmap="gray", aspect="auto")

    plt.subplots_adjust(wspace=.05, hspace=.05)

    plt.show()

df_attr_combined = pd.read_csv('./Anno/changed/etri/attr_combined.csv')
df_attr_category_combined = pd.read_csv('./Anno/changed/etri/attr_category_combined.csv')

lst_color = ['white ', 'black ', 'gray ', 'pink ', 'red ', 'green ', 'blue ', 'brown ', 'navy ', 'beige ', 'yellow ', 'purple ', 'orange ']
lst_gender = ['man ', 'woman ']
lst_sleeves = ['short sleeves ', 'long sleeves ', 'no sleeves ', 'short ', 'long ']
lst_season = ['spring ', 'summer ', 'autumn ', 'winter ']
lst_pattern = ['single ', 'checker ', 'dotted ', 'floral ', 'striped ']

isAttribute(lst_color)