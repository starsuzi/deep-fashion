import os
import glob

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


#rename_Image_name_in_txt_file("./Anno/changed/list_attr_img.txt")
#rename_Image_name_in_txt_file("./Anno/changed/list_bbox.txt")
#rename_Image_name_in_txt_file("./Anno/changed/list_category_img.txt")
#rename_Image_name_in_txt_file("./Anno/changed/list_landmarks.txt")

#renameImages('./coat/')
#renameImages('./dress/')
#renameImages('./jacket/')
#renameImages('./jumper/')
#renameImages('./pants/')
#renameImages('./skirt/')
#renameImages('./winter jacket/')
#renameImages('./shirt/')



