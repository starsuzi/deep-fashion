import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import os

#check if the attributes in lst_attribute is the coloumn of the dataframe
def isAttribute(lst_attribute, df):
    for col in lst_attribute:
        try:
            df[col]
            print("'"+col+"' exists")
        except :
            print("'"+col+"' doesn't exist")
            pass

#plot random images that contain the given attribute           
def plotRandomImage_by_attribute(attribute, img_num, df):
    print(attribute+'attribute')
    img_files = []
    dict_imgs = dict(zip(df.loc[df[attribute] == 1]['image_name'], df.loc[df[attribute] == 1]['category_name']))
    print(str(len(dict_imgs))+' images')
    #random sampling
    lst_rand_imgs = random.sample(list(dict_imgs.items()), img_num)
    
    for tuple_img in lst_rand_imgs:
        img=mpimg.imread('./'+tuple_img[1]+'/'+tuple_img[0]+'.jpg')
        img_files.append(img)
    #plot
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

#plot random images that contain the given string in thier filename
#for example, plotRandomImage_by_imgName("./shirt/",12, 'Floral') randomly shows 12 images whose filename contains 'Floral' in shirt directory
def plotRandomImage_by_imgName(dir_name,img_num, string_in_imgName):
    #get filenams from directory(dir_name)
    fnames = os.listdir(dir_name)

    img_files = []
    lst = []

    for fname in fnames:
        #if filename contains the string(parameter)m append lst
        if string_in_imgName in fname :
            lst.append(fname)
    #random sampling
    for sample in random.sample(lst, img_num):
        if sample[-4:] == '.jpg':
            img=mpimg.imread(dir_name+sample)
            img_files.append(img)
    #plot
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

#merge two columns by OR operation
def mergeColumns(col1, col2, df_attr_category_combined) :
    return ((df_attr_category_combined[col1] == 1) | (df_attr_category_combined[col2] == 1)).astype(int).replace(0, -1)

#merge multiple columns by OR operation
def mergeMultipleColumns(lst_attr, merged_col, df_attr_category_combined, df_final):
    #check if temp column already exists. If it does, delete it
    if 'temp' in df_attr_category_combined:
        df_attr_category_combined = df_attr_category_combined.drop(['temp'], axis=1)
 
    #firstly, merge two columns in temp column
    df_attr_category_combined.insert(loc=0, column='temp', value=mergeColumns(lst_attr[0], lst_attr[1], df_attr_category_combined))
    #then, merge other columns in lst_attr by iterating for loop
    for i in range(2,len(lst_attr)):
        df_attr_category_combined['temp'] = mergeColumns('temp', lst_attr[i], df_attr_category_combined)
    df_final.insert(loc = 3,column=merged_col, value=df_attr_category_combined['temp'])
    
    #drop temp column
    df_attr_category_combined = df_attr_category_combined.drop(['temp'], axis=1)

    return df_attr_category_combined, df_final

# set same attributes by category's character.
#for example, all skirt and dress categories should have woman attribute, so set 'woman' attribute's value as 1
def set_attributes_by_category(df, attribute, df_attr_category_combined):
    df.insert(3, attribute, value=1)
    #merge dataframes by outer join
    df_attr_category_combined = df_attr_category_combined.merge(df, how='outer')
    df_attr_category_combined[attribute].fillna(value = -1, inplace = True)
    df_attr_category_combined[attribute] = df_attr_category_combined[attribute].astype(int)
    return df_attr_category_combined

#finds image's filename that contains pattern attributes(floral, striped, dot, checker), and returns image names in list
def find_pattern_attribute_in_name(dir_name, lst_floral, lst_striped, lst_dot, lst_checker):
    #all file names in the directory 
    fnames = os.listdir(dir_name)
    #if the file name conatins the following attritbuts, append
    for fname in fnames:
        if ('Floral'in fname) | ('Rose'in fname) | ('Daisy'in fname) | ('Lily'in fname) | ('Botaincal'in fname):
            lst_floral.append(fname[:-4])   
        elif 'Stripe' in fname:
            lst_striped.append(fname[:-4])
        elif 'Dot' in fname:
            lst_dot.append(fname[:-4])
        elif ('Check' in fname) | ('Flannel' in fname):
            lst_checker.append(fname[:-4])

    return lst_floral, lst_striped, lst_dot, lst_checker

#finds image's filename that contains sleeves attributes(short sleeves, long sleeves, no sleeves), and returns image names in list
def find_sleeves_attribute_in_name(dir_name, lst_short_sleeves, lst_long_sleeves, lst_no_sleeves):
    #all file names in the directory 
    fnames = os.listdir(dir_name)
    #if the file name conatins the following attritbuts, append
    for fname in fnames:
        if 'Short-Sleeve'in fname :
            lst_short_sleeves.append(fname[:-4])
        elif 'Long-Sleeved' in fname:
            lst_long_sleeves.append(fname[:-4])
        elif ('Sleeveless' in fname) | ('Strap' in fname) | ('Tank'in fname):
            lst_no_sleeves.append(fname[:-4])

    return lst_short_sleeves, lst_long_sleeves, lst_no_sleeves

#convert the dataframe's row as xml form
def convert_row(row):
    return """<?xml version="1.0" encoding="utf-8"?>
<annotation>
  <folder>{}</folder>
  <filename>{}</filename>
  <source>
    <database></database>
    <annotation></annotation>
    <image></image>
    <flickrid></flickrid> 
  </source>
  <owner>
    <flickrid></flickrid>
    <name></name>
  </owner>    
  <size>
    <width></width>
    <height></height>
    <depth>3</depth>
  </size>
  <segmented></segmented>
  <object>
    <name>{}</name>
    <pose></pose>
    <truncated></truncated>
    <difficult></difficult>
    <bndbox>
      <xmin>{}</xmin>
      <ymin>{}</ymin>
      <xmax>{}</xmax>
      <ymax>{}</ymax>
    </bndbox>
    <attributes>
        <colors>{}</colors>
        <gender>{}</gender>
        <season>{}</season>
        <sleeves>{}</sleeves>
        <pattern>{}</pattern>
        <leg_pose></leg_pose>
        <glasses></glasses>
    </attributes>
  </object>
</annotation>""".format(
        row.category_name,
        row.image_name,
        row.category_name,
        row.x_1,row.y_1,row.x_2,row.y_2,
        row.colors, row.gender,row.season,row.sleeves, row.pattern  
    )

#create the xml and save
def create_xml(category,df_category):
    category_final_xml = '\n\n'.join(df_category.apply(convert_row, axis=1))
    lst_category_final = []
    lst_category_final = category_final_xml.split('\n\n')
    lst_category_img = df_category['image_name'].tolist()
    #xml export
    for i, xml_file in enumerate(lst_category_final):
        with open("./"+category+"/"+lst_category_img[i]+'.xml', 'w') as f:
            f.write(xml_file)