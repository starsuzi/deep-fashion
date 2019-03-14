import numpy as np
import pandas as pd
import csv
import os, glob

#collapse blanks in original text files
def collapseBlanks(original_path, saving_path):
    with open(original_path, 'r') as file :
         lines = file.readlines()
    
    for i, line in enumerate(lines):
        collapsed = ' '.join(line.split())
        lines[i] = lines[i].replace(line, collapsed)
        
    with open(saving_path, 'w') as file :
        for i in range(len(lines)-1):
            file.write(lines[i+1]+'\n')

#rename image names in the given text file
def rename_Image_name_in_txt_file(path):
    with open(path, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('img/', '')
    with open(path, 'w') as file :
        file.write(filedata)
    
    with open(path, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('/', '_')
    with open(path, 'w') as file :
        file.write(filedata)
        
    with open(path, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('.jpg', '')
    #In XML form, & gives error
    with open(path, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('&', 'and')
    
    with open(path, 'w') as file :
        file.write(filedata)

#In XML form, & gives error, so rename the image filenames
def replaceNpercent(path):
    fnames = os.listdir(path)
    for fname in fnames:
        if '&'in fname:
            os.rename(path+fname, path+fname.replace('&', 'and'))

#Since the original img file names are not intuitive, we need to change them
#for example, img_00000012.jpg is saved in the Heathered_Pocket_Babydoll_Dress/img_00000012.jpg
#we need to change its name as Heathered_Pocket_Babydoll_Dress_img_00000012.jpg and save in already made dress folder
def renameImages(newPath):
    lst_specific_category_path = []

    for filename in glob.iglob(newPath+'**', recursive=True):
        if os.path.isfile(filename): # filter dirs
            specific_category_path = os.path.dirname(filename)
            lst_specific_category_path.append(specific_category_path)

    for specific_category_path in lst_specific_category_path:
        for i, filename in enumerate(os.listdir(specific_category_path)):
            try:
                os.rename(specific_category_path+ '/' + filename, newPath + os.path.basename(specific_category_path) +'_'+ filename)
            except Exception as ex:
                print(ex)
                #print(filename)

#create dataframes from text files
def createCategoryDataFrame(lst_category_fname, category_label, category_name):
    df_category = pd.DataFrame(lst_category_fname, columns=['image_name'])
    df_category.insert(1,'category_label', category_label)
    df_category.insert(1,'category_name', category_name)
    return df_category

renameImages('./coat/')
renameImages('./dress/')
renameImages('./jacket/')
renameImages('./jumper/')
renameImages('./pants/')
renameImages('./skirt/')
renameImages('./winter jacket/')
renameImages('./shirt/')

collapseBlanks("./Anno/original/list_attr_img.txt", "./Anno/changed/list_attr_img.txt")
collapseBlanks("./Anno/original/list_attr_cloth.txt", "./Anno/changed/list_attr_cloth.txt")
collapseBlanks("./Anno/original/list_category_cloth.txt", "./Anno/changed/list_category_cloth.txt")
collapseBlanks("./Anno/original/list_category_img.txt", "./Anno/changed/list_category_img.txt")
collapseBlanks("./Anno/original/list_bbox.txt", "./Anno/changed/lst_bbox.txt")

#add , for split
with open("./Anno/changed/list_attr_cloth.txt", 'r') as file :
    filedata = file.read()
filedata = filedata.replace('attribute_type', ',attribute_type')
for attribute_type in range(1,6):
    filedata = filedata.replace(str(attribute_type), ','+str(attribute_type))
with open("./Anno/changed/list_attr_cloth.txt", 'w') as file :
    file.write(filedata)

rename_Image_name_in_txt_file("./Anno/changed/list_attr_img.txt")
rename_Image_name_in_txt_file("./Anno/changed/list_bbox.txt")
rename_Image_name_in_txt_file("./Anno/changed/list_category_img.txt")
rename_Image_name_in_txt_file("./Anno/changed/list_landmarks.txt")

#create dataframes
df_attr_img = pd.read_csv('./Anno/changed/list_attr_img.txt', header = None, skiprows=1, sep = ' ')
df_attr_cloth = pd.read_csv('./Anno/changed/list_attr_cloth.txt', sep = ',') 
df_category_cloth = pd.read_csv('./Anno/changed/list_category_cloth.txt', sep = ' ')
df_category_img = pd.read_csv('./Anno/changed/list_category_img.txt',sep = ' ') #, index_col='image_name'
df_bbox = pd.read_csv('./Anno/changed/lst_bbox.txt',sep = ' ') 

#inserting category_label to category_cloth
df_category_cloth.insert(0, 'category_label', range(1, len(df_category_cloth)+1))

# combining dataframes
#- Combining image and category name
df_category_combined = pd.merge(df_category_cloth, df_category_img)
#- Combining image and attribute name
lst_attr = df_attr_cloth['attribute_name ']
df_attr_img.columns = pd.Series(['image_name']).append(lst_attr,ignore_index=True)
df_attr_combined= df_attr_img
#- Combining attributes and category
df_attr_category_combined = pd.merge(df_attr_combined, df_category_combined)

#list of image file names in category folder
lst_coat_fname = [f.name[:-4] for f in os.scandir('./coat') if f.is_file()]
lst_dress_fname = [f.name[:-4] for f in os.scandir('./dress') if f.is_file()]
lst_jacket_fname = [f.name[:-4] for f in os.scandir('./jacket') if f.is_file()]
lst_jumper_fname = [f.name[:-4] for f in os.scandir('./jumper') if f.is_file()]
lst_pants_fname = [f.name[:-4] for f in os.scandir('./pants') if f.is_file()]
lst_shirt_fname = [f.name[:-4] for f in os.scandir('./shirt') if f.is_file()]
lst_skirt_fname = [f.name[:-4] for f in os.scandir('./skirt') if f.is_file()]
lst_winterJacket_fname = [f.name[:-4] for f in os.scandir('./winter jacket') if f.is_file()]

#create dataframes for each category
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

#dataframe for the all categories
df_category_attr_combined_from_imgfile = pd.concat([df_shirt_attr_combined, df_jumper_attr_combined, df_jacket_attr_combined, df_winterJacket_attr_combined, df_coat_attr_combined, df_dress_attr_combined, df_pants_attr_combined, df_skirt_attr_combined],
                                      ignore_index=True)
#export
#attr_combined.csv
file_name = "attr_combined.csv"
df_attr_combined.to_csv("./Anno/changed/"+file_name, index=None)
#category_combined.csv
file_name = "category_combined.csv"
df_category_combined.to_csv("./Anno/changed/"+file_name, index=None)
#attr_category_combined.csv
file_name = "attr_category_combined.csv"
df_attr_category_combined.to_csv("./Anno/changed/"+file_name, index=None)
#bbox.csv
file_name = "bbox.csv"
df_bbox.to_csv("./Anno/changed/"+file_name, index=None)
#attr_category_combined_asdf
file_name = "attr_category_combined_asdf.csv"
df_category_attr_combined_from_imgfile.to_csv("./"+file_name, index=None)
