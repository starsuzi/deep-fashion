import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

def isAttribute(lst_attribute, df):
    for col in lst_attribute:
        try:
            df[col]
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

def mergeColumns(col1, col2, df_attr_category_combined) :
    return ((df_attr_category_combined[col1] == 1) | (df_attr_category_combined[col2] == 1)).astype(int).replace(0, -1)

def mergeMultipleColumns(lst_attr, merged_col, df_attr_category_combined, df_final):

    if 'temp' in df_attr_category_combined:
        df_attr_category_combined = df_attr_category_combined.drop(['temp'], axis=1)
 
    df_attr_category_combined.insert(loc=0, column='temp', value=mergeColumns(lst_attr[0], lst_attr[1], df_attr_category_combined))

    for i in range(2,len(lst_attr)):
        df_attr_category_combined['temp'] = mergeColumns('temp', lst_attr[i], df_attr_category_combined)
    
    df_final.insert(loc = 3,column=merged_col, value=df_attr_category_combined['temp'])
    
    df_attr_category_combined = df_attr_category_combined.drop(['temp'], axis=1)

    return df_attr_category_combined, df_final

def same_attributes_by_category(df, attribute, df_attr_category_combined):
    df.insert(3, attribute, value=1)
    df_attr_category_combined = df_attr_category_combined.merge(df, how='outer')
    df_attr_category_combined[attribute].fillna(value = -1, inplace = True)
    df_attr_category_combined[attribute] = df_attr_category_combined[attribute].astype(int)
    return df_attr_category_combined