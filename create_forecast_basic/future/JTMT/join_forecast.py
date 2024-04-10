#!/usr/bin/env python
# coding: utf-8

# ## קוד מבוא

# #### ספריות

# In[21]:


import os
import sys
import pathlib
import pandas as pd


# In[22]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# #### העלאת משתנים להרצת הקוד

# In[23]:


#df_inputs_outputs = pd.read_excel('inputs_outputs.xlsx')

# software_data_folder_location=df_inputs_outputs['location'][0]

# forecast_version_folder_location='W:\Data\Forecast\forecast_by_version\V4\BASE_YEAR'

# future_folder = os.path.dirname(software_data_folder_location)

# create_forecast_basic_software_location = os.path.dirname(future_folder)

# sys.path.append(create_forecast_basic_software_location)

# create_forecast_basic_software_df = pd.read_excel(r'{}\inputs_outputs.xlsx'.format(create_forecast_basic_software_location))

# TAZ_V4_date = create_forecast_basic_software_df['location'][1]


# ## פונקציות

# ### פונקציות גלובליות

# In[24]:


from global_functions import up_load_df, find_files_with_pattern, up_load_shp


# ##  העלאת טבלאות תחזית

# מצב קיים

# In[25]:


forecast_version_folder_location=r'W:\Data\Forecast\forecast_by_version\V4\BASE_YEAR'


# In[26]:


forecast_2020=up_load_df(forecast_version_folder_location, '2020_jtmt_forcast_full_240407')


# מצב עתידי כל שנה

# In[27]:


software_data_folder_location=r'W:\Data\Forecast\Tools\forecast_git\create_forecast_basic\future\JTMT'


# In[28]:


v_date = '240408'

year=['2025','2030','2035','2040','2045','2050']

for y in year: 
    folder_path=r'{}\Intermediates'.format(software_data_folder_location)
    file_name='{}_forecast_{}_full'.format(v_date,y)

    locals()['forecast_{}'.format(y)]=up_load_df(folder_path,file_name)


# In[29]:


col_2050=['Taz_num','student_yeshiva_and_kollim',
 'student',
 'univ','aprt',
 'pop_without_dorms_yeshiva','emp_Education','emp_okev', 'emp_not_okev',
 'total_emp',
 'agri',
 'Indus',
 'Com_hotel',
 'Business',
 'Public']


# In[30]:


col_2020=['Taz_num',
 'aprt_20','pop_without_dorms_yeshiva','student',
 'univ',
 'student_yeshiva_and_kollim','total_emp','emp_okev',
 'emp_not_okev','emp_Education',
 'agri',
 'Indus',
 'Com_hotel',
 'Business',
 'Public']


# שכבת אזורי תנועה

# In[31]:


taz=up_load_shp(r'W:\Data\Forecast\Tools\forecast_git\create_forecast_basic\background_files\TAZ_V4_{}_with_geo_info.shp'.format('240404'))

col_taz=['Taz_num',
 'Taz_name',
 'main_secto',
 'Muni_Heb',
 'jeru_metro',
 'zonetype',
 'in_jerusal',
 'SCHN_NAME',]


# חיבור הכל

# In[32]:


df=taz[col_taz].merge(forecast_2020[col_2020],on='Taz_num',how='left')


# שלב ראשון קיצרתי את השמות שלהם

# In[33]:


for y in year: 
    locals()['forecast_{}'.format(y)]=locals()['forecast_{}'.format(y)][col_2050]


# שלב שני לייצר לכל שנה רשימה חדשה של שמות השדות שלו עם שינוי

# In[34]:


for y in year: 
    col=['student_yeshiva_and_kollim',
         'student',
         'univ','aprt',
         'pop_without_dorms_yeshiva','emp_Education','emp_okev', 'emp_not_okev',
         'total_emp',
         'agri',
         'Indus',
         'Com_hotel',
         'Business',
         'Public']
    
    x=[]
    
    for i in col: x=x+[i+'_{}'.format(y)]
        
    x=['Taz_num']+x
    
    locals()['col_{}'.format(y)]=x


# שלב שלישי לקחת את השמות החדשים ולשנות את העמודות של כל אחד

# In[35]:


for y in year: 
    locals()['forecast_{}'.format(y)].columns=locals()['col_{}'.format(y)]


# שלב אחרון לחבר את כולם אל הקיים

# In[36]:


for y in year: 
    df=df.merge(locals()['forecast_{}'.format(y)],on='Taz_num',how='left')


# In[37]:


col_order=['zonetype',
 'jeru_metro',
 'Muni_Heb',
 'main_secto',
 'in_jerusal',
 'SCHN_NAME',
 'Taz_num',
 'Taz_name',
 'aprt_20',
 'aprt_2025',
 'aprt_2030',
 'aprt_2035',
 'aprt_2040',
 'aprt_2045',
 'aprt_2050',
 'pop_without_dorms_yeshiva',
 'pop_without_dorms_yeshiva_2025',
 'pop_without_dorms_yeshiva_2030',
 'pop_without_dorms_yeshiva_2035',
 'pop_without_dorms_yeshiva_2040',
 'pop_without_dorms_yeshiva_2045',
 'pop_without_dorms_yeshiva_2050',
 'student',
 'student_2025',
 'student_2030',
 'student_2035',
 'student_2040',
 'student_2045',
 'student_2050',
 'univ',
 'univ_2025',
 'univ_2030',
 'univ_2035',
 'univ_2040',
 'univ_2045',
 'univ_2050',
 'student_yeshiva_and_kollim',
 'student_yeshiva_and_kollim_2025',
 'student_yeshiva_and_kollim_2030',
 'student_yeshiva_and_kollim_2035',
 'student_yeshiva_and_kollim_2040',
 'student_yeshiva_and_kollim_2045',
 'student_yeshiva_and_kollim_2050',
 'total_emp',
 'total_emp_2025',
 'total_emp_2030',
 'total_emp_2035',
 'total_emp_2040',
 'total_emp_2045',
 'total_emp_2050',
 'emp_okev',
 'emp_okev_2025',
 'emp_okev_2030',
 'emp_okev_2035',
 'emp_okev_2040',
 'emp_okev_2045',
 'emp_okev_2050',
 'emp_not_okev',
 'emp_not_okev_2025',
 'emp_not_okev_2030',
 'emp_not_okev_2035',
 'emp_not_okev_2040',
 'emp_not_okev_2045',
 'emp_not_okev_2050',
 'emp_Education',
 'emp_Education_2025',
 'emp_Education_2030',
 'emp_Education_2035',
 'emp_Education_2040',
 'emp_Education_2045',
 'emp_Education_2050',
 'agri',
 'agri_2025',
 'agri_2030',
 'agri_2035',
 'agri_2040',
 'agri_2045',
 'agri_2050',
 'Indus',
 'Indus_2025',
 'Indus_2030',
 'Indus_2035',
 'Indus_2040',
 'Indus_2045',
 'Indus_2050',
 'Com_hotel',
 'Com_hotel_2025',
 'Com_hotel_2030',
 'Com_hotel_2035',
 'Com_hotel_2040',
 'Com_hotel_2045',
 'Com_hotel_2050',
 'Business',
 'Business_2025',
 'Business_2030',
 'Business_2035',
 'Business_2040',
 'Business_2045',
 'Business_2050',
 'Public',
 'Public_2025',
 'Public_2030',
 'Public_2035',
 'Public_2040',
 'Public_2045',
 'Public_2050']


# In[38]:


# תאריך
file_date=pd.Timestamp.today().strftime('%y%m%d')


# In[39]:


forecast_version_folder_location=r'W:\Data\Forecast\forecast_by_version\V4'


# In[40]:


save_file_path=r'{}'.format(forecast_version_folder_location)

save_excel_path=r'{}\{}_forecast_2020_till_2050_jtmt.xlsx'.format(save_file_path,file_date)

df[col_order].to_excel(save_excel_path,index=False)

