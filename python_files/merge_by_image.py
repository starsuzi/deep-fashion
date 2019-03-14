import numpy as np
import pandas as pd
import csv
import module

#df_attr_category_combined = pd.read_csv('./Anno/changed/etri/attr_category_combined.csv')
df_attr_category_combined = pd.read_csv('./attr_category_combined_asdf.csv')
df_final = df_attr_category_combined.iloc[:,:3]

#Since all elements in winter jacket category should have winter attribute, create df_winter
df_winter = df_attr_category_combined.groupby('category_name').get_group('winter jacket')
df_attr_category_combined = module.set_attributes_by_category(df_winter,'winter', df_attr_category_combined)
df_final.insert(loc = 3,column='winter', value=df_attr_category_combined['winter'])

#Since all elements in winter skirt and dress category should have winter attribute, create df_woman
df_woman_dress = df_attr_category_combined.groupby('category_name').get_group('dress')
df_woman_skirt = df_attr_category_combined.groupby('category_name').get_group('skirt')
df_woman = pd.concat([df_woman_skirt, df_woman_dress])
df_attr_category_combined = module.set_attributes_by_category(df_woman,'woman', df_attr_category_combined)
df_final.insert(loc = 3,column='woman', value=df_attr_category_combined['woman'])

#long skirts
lst_long_skirt = ['belted maxi ', 'chiffon maxi ', 'combo maxi ', 'crochet maxi ', 'cutout maxi ',
 'embroidered maxi ', 'floral maxi ', 'flounce maxi ', 'gauze maxi ', 'high-slit maxi ',
 'knit maxi ', 'lace maxi ', 'm-slit maxi ', 'maxi ', 'longline ']

df_woman_skirt_temp = df_woman_skirt.iloc[:, :3]
#merge two columns in temp column with OR operation
df_woman_skirt.insert(loc=0,column='temp',value=((df_woman_skirt[lst_long_skirt[0]] == 1) | (df_woman_skirt[lst_long_skirt[1]] == 1)).astype(int).replace(0, -1))
#merge other columns in lst_long_skirt by iterating for loop
for i in range(2,len(lst_long_skirt)):
    df_woman_skirt['temp'] = ((df_woman_skirt['temp'] == 1) | (df_woman_skirt[lst_long_skirt[i]] == 1)).astype(int).replace(0, -1)
df_woman_skirt_temp.insert(loc = 2,column='long', value= (df_woman_skirt['temp']))
#drop temp column in df_woman_skirt
df_woman_skirt = df_woman_skirt.drop(['temp'], axis=1)
#insert 'long' column to df_attr_category_combined
df_attr_category_combined.insert(3, 'long',np.NaN )
# if df_woman_skirt_temp's data in 'long' column's value is 1, get image name from 'image_name' column
set_long_skirt_name=set(df_woman_skirt_temp.loc[df_woman_skirt_temp['long'] == 1]['image_name'])
# iterate df_attr_category_combined['image_name'], and if the element is in set_long_skirt_name,
# set value of df_attr_category_combined['long'] with 1
for i,img_name in enumerate(df_attr_category_combined['image_name']):
    if img_name in set_long_skirt_name:
       df_attr_category_combined.loc[i,'long'] = 1
df_attr_category_combined.fillna(value = -1, inplace = True)
df_attr_category_combined['long'] = df_attr_category_combined['long'].astype(int)

#short long pants
df_attr_category_combined_temp = df_attr_category_combined
#set image name as index
df_attr_category_combined_temp.set_index('image_name', inplace= True)
#if the image name contains Shorts or Trunk or Sweatshorts, append lst_short
lst_short = df_attr_category_combined.filter(like='Shorts', axis=0).index.tolist() + df_attr_category_combined.filter(like='Trunk', axis=0).index.tolist() + df_attr_category_combined.filter(like='Sweatshorts', axis=0).index.tolist()
#create df_short for short pants
df_short = df_attr_category_combined_temp[df_attr_category_combined_temp.index.isin(lst_short)]
#insert 'short' column in df_short with value 1
df_short.insert(2,  'short', value=1)
df_short.reset_index(inplace=True)
df_attr_category_combined_temp.reset_index(inplace=True)
#merge df_attr_category_combined and df_short with outer join
df_attr_category_combined = df_attr_category_combined_temp.merge(df_short, how='outer')
#fill Nan value with -1
df_attr_category_combined['short'].fillna(value = -1, inplace = True)
df_attr_category_combined['short'] = df_attr_category_combined['short'].astype(int)
#create dataframe for pants
df_pants = df_attr_category_combined.groupby('category_name').get_group('pants')
#create dataframe for the long pants
#all the pants that are not shorts are long pants
df_long_pants = df_pants[~df_pants['image_name'].isin(lst_short)]
df_long_pants.insert(3, 'long_pants', 1)
# set_long_pants_name: if df_long_pants's data in 'long_pants' column's value is 1, get image name from 'image_name' column
# set_short_pants_name: if df_short's data in 'short' column's value is 1, get image name from 'image_name' column
set_long_pants_name=set(df_long_pants.loc[df_long_pants['long_pants'] == 1]['image_name'])
set_short_pants_name =set(df_short.loc[df_short['short'] == 1]['image_name'])
# iterate df_attr_category_combined['image_name'], and if the element is in set_long_pants_name,
# set value of df_attr_category_combined['long_pants'] with 1
# if the element is in set_short_pants_name,
# set value of df_attr_category_combined['short'] with 1
for i,img_name in enumerate(df_attr_category_combined['image_name']):
    if img_name in set_long_pants_name:
        df_attr_category_combined.loc[i,'long_pants'] = 1
    elif img_name in set_short_pants_name:
        df_attr_category_combined.loc[i,'short'] = 1
# merge long column and long_pants column
df_attr_category_combined['long'] = module.mergeColumns('long', 'long_pants', df_attr_category_combined)
df_attr_category_combined.drop(['long_pants'], axis=1, inplace=True)
#insert long column and short column
df_final.insert(loc = 3,column='long', value=df_attr_category_combined['long'])
df_final.insert(loc = 3,column='short', value=df_attr_category_combined['short'])

# merge columns in list to one column to df_final
lst_long_sleeves = ['long sleeve ', 'long-sleeve ', 'long-sleeved ']
_ , df_final = module.mergeMultipleColumns(lst_long_sleeves, 'long sleeves', df_attr_category_combined, df_final)

lst_no_sleeves = ['sleeveless ','print strapless ','print strappy ','strap ', 'strapless ', 'strapless tribal ', 'strappy ']
_ , df_final = module.mergeMultipleColumns(lst_no_sleeves, 'no sleeves', df_attr_category_combined, df_final)

lst_checker = ['checked ', 'checkered ', 'grid print ','grid ']
_ , df_final = module.mergeMultipleColumns(lst_checker, 'checker', df_attr_category_combined, df_final)

lst_dotted = ['dotted ', 'dot ', 'dots ', 'polka dot ']
_ , df_final = module.mergeMultipleColumns(lst_dotted, 'dotted', df_attr_category_combined, df_final)

lst_floral = ['abstract floral ','abstract floral print ','belted floral ','belted floral print ','chiffon floral ',
 'crochet floral ','ditsy floral ','ditsy floral print ','embroidered floral ','floral ','floral flutter ','floral knit ',
 'floral lace ','floral lace mini ','floral lace sheath ','floral lace skater ','floral maxi ','floral mesh ','floral midi ','floral mini ',
 'floral paisley ','floral pattern ','floral peasant ','floral pleated ','floral print ','floral print skater ',
 'floral print strapless ','floral print surplice ','floral shift ', 'floral skater ','floral surplice ',
 'floral textured ','floral-embroidered ','flower ','sunflower ', 'wildflower ',
 'daisy print ', 'botanical print ', 'rose ', 'roses ', 'rose skater ', 'print tulip ', 'botanical ']
_ , df_final = module.mergeMultipleColumns(lst_floral, 'floral', df_attr_category_combined, df_final)

lst_striped = ['stripe ', 'abstract stripe ', 'back striped ', 'boxy striped ', 'breton stripe ', 'classic striped ',
 'heathered stripe ', 'knit stripe ',  'knit striped ', 'marled stripe ','mixed stripe ', 'multi-stripe ',
 'nautical stripe ', 'nautical striped ', 'neck striped ', 'ribbed stripe ', 'rugby stripe ', 'rugby striped ',
 'striped ','striped trapeze ', 'striped v-neck ', 'stripes ' ]
_ , df_final = module.mergeMultipleColumns(lst_striped, 'striped', df_attr_category_combined, df_final)

lst_other_print = ['abstract chevron print ', 'abstract geo print ', 'abstract print ', 'abstract printed ',
 'animal print ', 'bandana print ', 'baroque print ', 'bird print ', 'brushstroke print ', 'butterfly print ',
 'chevron print ', 'diamond print ', 'elephant print ', 'folk print ', 'geo print ', 'giraffe print ', 'heart print ',
 'ikat print ', 'kaleidoscope print ', 'lace print ', 'leaf print ', 'leopard print ', 'mandala print ',
 'marble print ', 'medallion print ', 'mixed print ', 'mosaic print ', 'ornate print ', 'paisley print ', 'palm print ',
 'print ', 'print racerback ', 'print satin ', 'print scuba ', 'print shift ', 'print shirt ', 'print skater ',
 'print smock ', 'print smocked ', 'print strapless ', 'print strappy ', 'print surplice ', 'print v-neck ',
 'print woven ', 'printed ', 'southwestern-print ', 'graphic ', 'graphic muscle ', 'graphic racerback ']
_ , df_final = module.mergeMultipleColumns(lst_other_print, 'others', df_attr_category_combined, df_final)

#insert columns which does not have to be merged
df_final.insert(loc = 3, column = 'summer', value=df_attr_category_combined['summer '])
df_final.insert(loc = 3,column='pink', value=df_attr_category_combined['pink '])
df_final.insert(loc = 3,column='red', value=df_attr_category_combined['red '])

#save
file_name = "asdfasdf.csv"
df_final.to_csv("./"+file_name, index=None)