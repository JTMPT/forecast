import os
import pandas as pd
import geopandas as gpd
import fiona

def change_cols_names(df, old_col, new_col):
    df=df[old_col]
    df.columns=new_col
    return df

def double_taz_num(df):
    dup_taz_num=df.groupby(['Taz_num']).size().reset_index(name='count').query('count>1').Taz_num.to_list()
    return df.loc[df['Taz_num'].isin(dup_taz_num)]

def make_point(df):
    df_point=df.copy()
    df_point['centroid'] = df_point.representative_point()
    df_point=df_point.set_geometry('centroid')
    df_point=df_point.drop(columns=['geometry'],axis=1)
    return df_point

def up_load_gdb(path,layer_name):
    path='{}'.format(path)
    layer_list=fiona.listlayers(path)
    gpd_layer=gpd.read_file(path, layer=layer_list.index(layer_name))
    return gpd_layer

def up_load_shp(path):
    path='{}'.format(path)
    gpd_layer=gpd.read_file(path)
    return gpd_layer

def up_load_df(folder_path,file_name):
    path_df=r'{}\{}.xlsx'.format(folder_path,file_name)
    df=pd.read_excel(path_df)
    df=df.dropna(how='all')
    return df

def split_index_by_taz(index,taz,min_prec,col_name_to_split):
    index['index_area']=index.area
    
    taz['taz_area']=taz.area

    index_taz=index.overlay(taz[['Taz_num','taz_area','geometry']])

    index_taz['small_area']=index_taz.area

    index_taz['precent_from_big_index']=index_taz['small_area']/index_taz['index_area']
    
    index_taz['precent_from_big_taz']=index_taz['small_area']/index_taz['taz_area']

    index_taz=index_taz.loc[(index_taz['precent_from_big_index']>min_prec)|(index_taz['precent_from_big_taz']>0.9)]
    
    index_taz=index_taz[['id','Taz_num','precent_from_big_index']]

    new_big=index_taz.groupby(['id']).sum()

    index=index.set_index('id')
    index['new_big']=new_big['precent_from_big_index']

    index=pd.merge(index.reset_index(),index_taz,on='id')

    for c in col_name_to_split:
        index['{}'.format(c)]=index['{}'.format(c)]*(index['precent_from_big_index']/index['new_big'])     
    return index

def find_files_with_pattern(folder_path, pattern):
    """
    Find files in a directory that match a certain pattern.
    
    Args:
    - directory (str): The directory path.
    - pattern (str): The pattern to search for in file names.
    
    Returns:
    - List of file paths matching the pattern.
    """
    files = []
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if pattern in filename:
                files.append(os.path.join(root, filename))
    return files

def logic_test_for_forecast(taz):
    print ('taz num under 0:',list(taz.loc[taz['TAZ']<=0]['TAZ']))
    
    print ('taz num duplicate:',list(taz.loc[taz.duplicated(subset='TAZ',keep=False)]['TAZ']))
    
    print ('yosh_unique:',list(taz.yosh.unique()))
    
    print ('in_jerusalem_metropolin_unique:',list(taz.in_jerusalem_metropolin.unique()))
    
    print ('jerusalem_city_unique:',list(taz.jerusalem_city.unique()))
    
    print ('sector_unique:',list(taz.sector.unique()))

    col=['hh_total',
    'pop',
    'age0_4',
    'age5_9',
    'age10_14',
    'age15_19',
    'age20_24',
    'age25_29',
    'age30_34',
    'age35_39',
    'age40_44',
    'age45_49',
    'age50_54',
    'age55_59',
    'age60_64',
    'age65_69',
    'age70_74',
    'age75up',
    'emp_tot',
    'indus',
    'com_hotel',
    'business',
    'public',
    'education',
    'agri',
    'student',
    'univ',
    'UO_Hi_Ed',
    'pop_emp_employed']

    taz_to_check_minus=[]
    col_to_check_minus=[]
    for i in col:
        taz_to_check_minus=taz_to_check_minus+list(taz.loc[taz['{}'.format(i)]<0]['TAZ'])
    
    print ('taz num with minus:',list(set(taz_to_check_minus)))
    
    print ('pop more then hh:',list(taz.loc[taz['sector']!="Palestinian"].loc[~(taz['hh_total']<=taz['pop'])]['TAZ']))
    
    print ('hh missing pop:',list(taz.loc[taz['sector']!="Palestinian"].loc[taz['hh_total']>0].loc[taz['pop']<=0]['TAZ']))
    
    print ('pop missing hh:',list(taz.loc[taz['sector']!="Palestinian"].loc[taz['pop']>0].loc[taz['hh_total']<=0]['TAZ']))

    col=['age0_4',
    'age5_9',
    'age10_14',
    'age15_19',
    'age20_24',
    'age25_29',
    'age30_34',
    'age35_39',
    'age40_44',
    'age45_49',
    'age50_54',
    'age55_59',
    'age60_64',
    'age65_69',
    'age70_74',
    'age75up',]

    taz['pop_check']=taz[col].sum(axis=1)-taz['pop']
    
    taz['pop_check']=taz['pop_check'].round(0)
    
    print ('pop vs age dis Mistake:',list(taz.loc[taz['sector']!="Palestinian"].loc[taz['pop_check']!=0]['TAZ']))   

    col=[
    'age0_4',
    'age5_9',
    'age10_14',
    'age15_19',
    'age20_24',
    'age25_29',
    'age30_34',
    'age35_39',
    'age40_44',
    'age45_49',
    'age50_54',
    'age55_59',
    'age60_64',
    'age65_69',
    'age70_74',
    'age75up']

    taz_to_check_for_age=[]
    for i in col:
        taz_to_check_for_age=taz_to_check_for_age+list(taz.loc[taz['{}'.format(i)]>0].loc[taz['pop']<=0]['TAZ'])
        taz_to_check_for_age=taz_to_check_for_age+list(taz.loc[taz['{}'.format(i)]>0].loc[taz['hh_total']<=0]['TAZ'])
        
    print ('taz num with age dis prob:',taz_to_check_for_age)

    col=['indus',
    'com_hotel',
    'business',
    'public',
    'education',
    'agri']

    taz['emp_check']=taz[col].sum(axis=1)-taz['emp_tot']
    taz['emp_check']=abs(taz['emp_check'].round(0))
    
    taz_prob_emp_total=list(taz.loc[taz['emp_check']>1]['TAZ'])
    
    print ('taz num with emp total prob:',taz_prob_emp_total)

    taz_to_check_for_split_emp=[]
    
    for i in col:
        taz_to_check_for_split_emp=taz_to_check_for_split_emp+list(taz.loc[taz['{}'.format(i)]>0].loc[taz['emp_tot']<=0]['TAZ'])
        
    print ('taz num with emp dis prob:',taz_to_check_for_split_emp)

    print ('taz num with pop_emp_employed worng :',list(taz.loc[taz['sector']!="Palestinian"].loc[taz['pop_emp_employed']>0].loc[taz['pop']<=0]['TAZ']))
    return

def drop_geo(geoDF):
    geoDF = geoDF.drop(columns='geometry')
    return geoDF

def add_geo_info_shp(taz,taz_border,software_folder_location,shp_name,col_name): #זה אמור להיות כפונקציה גלובלית

    forecast_point = make_point(taz_border)

    # Load data layers
    geo_info = up_load_shp(r'{}\background_files\{}.shp'.format(software_folder_location,shp_name))
    
    forecast_point_geo_info = forecast_point.sjoin(geo_info)[['Taz_num', '{}'.format(col_name)]]

    taz = taz.merge(forecast_point_geo_info, on='Taz_num', how='left')

    taz=taz.fillna(0)

    return taz