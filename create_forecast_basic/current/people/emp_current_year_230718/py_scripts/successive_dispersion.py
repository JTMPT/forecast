import geopandas as gpd

def successive_dispersion(EMP_kibolet, taz):
    EMP_kibolet['geometry_buff']=EMP_kibolet.buffer(250)

    EMP_buffer=EMP_kibolet.set_geometry('geometry_buff').query('kayim_emp>0')

    EMP_buffer=EMP_buffer.dissolve()[['geometry_buff']]

    taz['taz_area']=taz.area

    emp_buffer_taz=gpd.overlay(EMP_buffer,taz.reset_index())

    emp_buffer_taz['emp_samll_area']=emp_buffer_taz.area

    emp_buffer_taz['emp_pre_from_taz']=emp_buffer_taz['emp_samll_area']/emp_buffer_taz['taz_area']

    taz_num_no_need_okev=emp_buffer_taz.loc[emp_buffer_taz['emp_pre_from_taz']>0.4].Taz_num.to_list()

    taz['okev']=0
    taz.loc[(~taz.index.isin(taz_num_no_need_okev))&(taz['pop']>0)&(taz['main_secto']!="Palestinia"),'okev']=1

    taz.loc[taz['main_secto']=="arabs_behined_seperation_wall",'okev']=1

    city_muni=['מודיעין עילית','בית שמש','ירושלים','מודיעין - מכבים - רעות']

    return taz