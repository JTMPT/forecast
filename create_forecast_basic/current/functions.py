import pandas as pd
import geopandas as gpd
import numpy as np
from shapely import wkt
from matplotlib import pyplot as plt 
import folium
import fiona
from mpl_toolkits.axes_grid1 import make_axes_locatable
from shapely.geometry import Point

def drop_geo(geoDF):
    geoDF = geoDF.drop(columns='geometry')
    return geoDF

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

def unique_id_in_one_taz(df_to_geoode,unique_field,gpd_for_geocode,taz):
    
    code_to_find=list(df_to_geoode[unique_field].unique())

    gpd_for_geocode_to_sum_by_taz=gpd_for_geocode[[unique_field,'geometry']].loc[gpd_for_geocode[unique_field].isin(code_to_find)]

    gpd_for_geocode_to_sum_by_taz=gpd.sjoin(taz[['Taz_num','geometry']],gpd_for_geocode_to_sum_by_taz)

    gpd_for_geocode_in_one_taz=list(gpd_for_geocode_to_sum_by_taz.groupby(unique_field)[['Taz_num']].nunique().query('Taz_num==1').reset_index()[unique_field])

    return gpd_for_geocode_in_one_taz

def up_load_df(folder_path,file_name):
    
    path_df=r'{}\{}.xlsx'.format(folder_path,file_name)
    df=pd.read_excel(path_df)
    df=df.dropna(how='all')

    return df