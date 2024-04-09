

import os
import sys
import pathlib
import pandas as pd
import geopandas as gpd


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


df_inputs_outputs = pd.read_excel('inputs_outputs.xlsx')

software_data_folder_location=df_inputs_outputs['location'][0]

forecast_version_folder_location=df_inputs_outputs['location'][1]


TAZ_V4_date = '240404'


from global_functions import up_load_df, find_files_with_pattern, make_point, up_load_gdb, up_load_shp, logic_test_for_forecast, drop_geo,add_geo_info_gdb,add_geo_info_shp,change_cols_names


year=['2025','2030','2035','2040','2045','2050']

for y in year: 
    
    col=['Taz_num',
 'aprt',
 'pop',
 'pop_0',
 'pop_10',
 'pop_15',
 'pop_20',
 'pop_25',
 'pop_30',
 'pop_35',
 'pop_40',
 'pop_45',
 'pop_5',
 'pop_50',
 'pop_55',
 'pop_60',
 'pop_65',
 'pop_70',
 'pop_75up']
    
    folder_path=r'W:\Data\Forecast\Tools\forecast_git\create_forecast_basic\future\JTMT\Intermediates'

    file_name='{}_pop_{}_jtmt'.format('240306',y)

    locals()['forecast_pop_{}_jtmt'.format(y)]=up_load_df(folder_path,file_name)[col]


col=['Taz_num',
     'Taz_name',
     'Muni_Heb',
     'jeru_metro',
     'zonetype',
     'in_jerusal',
     'main_secto',
     'aprt_20',
     'student_dorms',
     'Yeshiva',
     'student',
     'univ','emp_uni','pop','emp_from_Yeshiva_student','yeshiva_dorms_pop_15',
     'yeshiva_dorms_pop_20',
     'yeshiva_dorms_pop_25',
     'yeshiva_dorms_pop_sum','jew','Seminar_dorms_pop_15',
 'Seminar_dorms_pop_20',
 'Seminar_dorms_pop_25',
 'Seminar_dorms_pop_sum','emp_from_Seminar_student','Seminar','SEA1',
 'SEA2',
 'SEA3',
 'UOA1',
 'UOA2',
 'UOA3',
 'ARA1',
 'ARA2',
 'ARA3','Univ_AR',
 'Univ_SE',
 'Univ_UO','TOA1',
 'TOA2',
 'TOA3','pop_15_just_from_aprt','pop_20_just_from_aprt','pop_25_just_from_aprt','Agg_taz_nu']

new_column_names = {'aprt_20': 'aprt','Yeshiva':'student_yeshiva'}


forecast_2020=pd.read_excel(r'W:\Data\Forecast\forecast_by_version\V4\BASE_YEAR\2020_jtmt_forcast_full_240407.xlsx' )[col]


forecast_2020=forecast_2020.rename(columns=new_column_names)


pop_20_30_just_from_aprt_SE=forecast_2020.query('main_secto=="Jewish"').sum()[['pop_20_just_from_aprt']].item()+forecast_2020.query('main_secto=="Jewish"').sum()[['pop_25_just_from_aprt']].item()


Univ_SE_sum=forecast_2020.Univ_SE.sum()


Univ_SE_pre_from_pop_20_30=Univ_SE_sum/pop_20_30_just_from_aprt_SE


pop_20_30_just_from_aprt_AR=forecast_2020.query('main_secto=="arabs_behined_seperation_wall" |main_secto=="Arab" ').sum()[['pop_20_just_from_aprt']].item()+forecast_2020.query('main_secto=="arabs_behined_seperation_wall" |main_secto=="Arab" ').sum()[['pop_25_just_from_aprt']].item()


Univ_AR_sum=forecast_2020.Univ_AR.sum()


Univ_AR_pre_from_pop_20_30=Univ_AR_sum/pop_20_30_just_from_aprt_AR


pop_20_30_just_from_aprt_ou=forecast_2020.query('main_secto=="U_Orthodox"').sum()[['pop_20_just_from_aprt']].item()+forecast_2020.query('main_secto=="U_Orthodox"').sum()[['pop_25_just_from_aprt']].item()


Univ_ou_sum=forecast_2020.Univ_UO.sum()


Univ_UO_pre_from_pop_20_30=Univ_ou_sum/pop_20_30_just_from_aprt_ou


pop_15_20_just_from_aprt_ou=forecast_2020.query('main_secto=="U_Orthodox"').sum()[['pop_15_just_from_aprt']].item()+forecast_2020.query('main_secto=="U_Orthodox"').sum()[['pop_20_just_from_aprt']].item()
student_yeshiva=forecast_2020.student_yeshiva.sum().item()
student_yeshiva_pre_from_age_15_20=student_yeshiva/pop_15_20_just_from_aprt_ou
student_seminar=forecast_2020.Seminar.sum().item()
student_seminar_pre_from_age_15_20=student_seminar/pop_15_20_just_from_aprt_ou


EMP_kibolet=up_load_gdb(r'W:\Data\Forecast\Tools\forecast_git\create_forecast_basic\future\JTMT\background_files\EMP_kibolet.gdb','EMP_kibolet')

EMP_kibolet=EMP_kibolet.fillna(0)

EMP_kibolet['emp_kayim_no_palestinians']=EMP_kibolet['kayim_emp']-EMP_kibolet['Palestinians']

EMP_kibolet['emp_current']=EMP_kibolet['emp_kayim_no_palestinians']


col=[ 'F2025',
 'F2030',
 'F2035',
 'F2040',
 'F2045',
 'F2050']

EMP_kibolet[col]=EMP_kibolet[col].apply(lambda x: x * (EMP_kibolet['kibolt']-EMP_kibolet['kayim_emp']))

EMP_kibolet[col]=EMP_kibolet[col].cumsum(axis=1)

EMP_kibolet[col]=EMP_kibolet[col].apply(lambda x: x +EMP_kibolet['emp_kayim_no_palestinians'])

emp_not_okev_current=EMP_kibolet['emp_kayim_no_palestinians'].sum().item()


taz=up_load_shp(r'W:\Data\Forecast\Tools\forecast_git\create_forecast_basic\background_files\TAZ_V4_{}_with_geo_info.shp'.format(TAZ_V4_date))


taz['taz_area']=taz.area

EMP_kibolet['emp_area']=EMP_kibolet.area

EMP_kibolet['ID']=EMP_kibolet.index


EMP_kibolet_by_taz=gpd.overlay(taz[['Taz_num','taz_area','geometry']],EMP_kibolet[['ID','emp_area','geometry']])

EMP_kibolet_by_taz['small_area']=EMP_kibolet_by_taz.area

EMP_kibolet_by_taz['pre_small_area_emp']=EMP_kibolet_by_taz['small_area']/EMP_kibolet_by_taz['emp_area']

EMP_kibolet_by_taz['pre_small_area_taz']=EMP_kibolet_by_taz['small_area']/EMP_kibolet_by_taz['taz_area']

EMP_kibolet_by_taz=EMP_kibolet_by_taz.query('(pre_small_area_taz >0.7) | (pre_small_area_emp >0.1)')[['ID','Taz_num','geometry']]

EMP_kibolet_by_taz['small_area']=EMP_kibolet_by_taz.area

EMP_kibolet_by_taz=EMP_kibolet_by_taz.set_index('ID')

EMP_kibolet_by_taz['id_area_for_pre']=drop_geo(EMP_kibolet_by_taz).groupby(by='ID').sum()['small_area']

EMP_kibolet_by_taz['prec_from_id']=EMP_kibolet_by_taz['small_area']/EMP_kibolet_by_taz['id_area_for_pre']


EMP_kibolet['geometry_buff']=EMP_kibolet.buffer(250)


software_data_folder_location=r'W:\Data\Forecast\Tools\forecast_git\create_forecast_basic\future\JTMT'


city_muni=['מודיעין עילית','בית שמש','ירושלים','מודיעין - מכבים - רעות']

okev_factor=up_load_df(r'{}\background_files'.format(software_data_folder_location),'okev_factor').set_index('sector')

work_factor=up_load_df(r'{}\background_files'.format(software_data_folder_location),'work_factor_230719').set_index('sector')


emp_category_type=up_load_shp(r'{}\background_files\emp_category_type.shp'.format(software_data_folder_location)).fillna(0)


col=['agri', 'Indus', 'Com_hotel', 'Business', 'Public']

emp_category_type[col]=emp_category_type[col]/100

emp_category_type=gpd.sjoin(make_point(taz.reset_index())[['Taz_num','centroid']],emp_category_type).set_index('Taz_num')


commuting=up_load_shp(r'{}\background_files\commuting_230712.shp'.format(software_data_folder_location))


pre_woman=0.5

pre_man=1-pre_woman

work_age=[ 'pop_25',
'pop_30',
'pop_35',
'pop_40',
'pop_45',
'pop_50',
'pop_55',
'pop_60']

under_work_age=[ 'pop_15', 'pop_20']

over_work_age=[ 'pop_65', 'pop_70', 'pop_75up']


forecast_2020['sector_for_chinuc']=forecast_2020['main_secto']


forecast_2020.loc[forecast_2020['main_secto']=='arabs_behined_seperation_wall','sector_for_chinuc']='Arab'


Supply_crurent=forecast_2020.query('main_secto!="Palestinian"').pivot_table(index=['Muni_Heb','main_secto'],aggfunc=sum)[['TOA1',
 'TOA2',
 'TOA3']]
col=['Taz_num','sector_for_chinuc',
    'Taz_name',
    'Muni_Heb',
    'jeru_metro',
    'zonetype',
    'in_jerusal',
    'main_secto','jew',
    'student_dorms',
    'student_yeshiva',
    'student', 'univ', 'emp_uni','emp_from_Yeshiva_student','yeshiva_dorms_pop_15',
    'yeshiva_dorms_pop_20',
    'yeshiva_dorms_pop_25',
    'yeshiva_dorms_pop_sum','TOA1',
'TOA2',
'TOA3','Univ_SE','Univ_AR','Univ_UO','Seminar_dorms_pop_15',
'Seminar_dorms_pop_20',
'Seminar_dorms_pop_25','emp_from_Seminar_student','Seminar','Agg_taz_nu']


forecast_current=forecast_2020[col]


years=['2025','2030','2035','2040','2045','2050']

for y in years:
    forecast=pd.merge(forecast_current,locals()['forecast_pop_{}_jtmt'.format(y)],on="Taz_num",how='right')
        
    forecast['student_demand_TOA1']=forecast['pop_5']/5*4+forecast['pop_10']/5*2
    forecast['student_demand_TOA2']=forecast['pop_10']/5*3
    forecast['student_demand_TOA3']=forecast['pop_15']/5*4


    demad_for_students_by_muni_and_sector=forecast.pivot_table(index=('Muni_Heb','sector_for_chinuc'),aggfunc='sum')[['student_demand_TOA1','student_demand_TOA2','student_demand_TOA3','TOA1','TOA2','TOA3']]


    demad_for_students_by_muni_and_sector['add_from_demad_TOA1_muni_sector']=demad_for_students_by_muni_and_sector['student_demand_TOA1']-demad_for_students_by_muni_and_sector['TOA1']
    demad_for_students_by_muni_and_sector['add_from_demad_TOA2_muni_sector']=demad_for_students_by_muni_and_sector['student_demand_TOA2']-demad_for_students_by_muni_and_sector['TOA2']
    demad_for_students_by_muni_and_sector['add_from_demad_TOA3_muni_sector']=demad_for_students_by_muni_and_sector['student_demand_TOA3']-demad_for_students_by_muni_and_sector['TOA3']


    demad_for_students_by_muni_and_sector.loc[demad_for_students_by_muni_and_sector['add_from_demad_TOA1_muni_sector']<0,'add_from_add_from_demad_TOA1_muni_sectordemad_TOA1']=0
    demad_for_students_by_muni_and_sector.loc[demad_for_students_by_muni_and_sector['add_from_demad_TOA2_muni_sector']<0,'add_from_demad_TOA2_muni_sector']=0
    demad_for_students_by_muni_and_sector.loc[demad_for_students_by_muni_and_sector['add_from_demad_TOA3_muni_sector']<0,'add_from_demad_TOA3_muni_sector']=0
    demad_for_students_by_muni_and_sector=demad_for_students_by_muni_and_sector.reset_index()


    col=['Muni_Heb','sector_for_chinuc','add_from_demad_TOA1_muni_sector', 'add_from_demad_TOA2_muni_sector', 'add_from_demad_TOA3_muni_sector']

    forecast=forecast.merge(demad_for_students_by_muni_and_sector[col],on=['Muni_Heb','sector_for_chinuc'])

    forecast=forecast.fillna(0)


    forecast['student_TOA1_to_fill_demand']=forecast['student_demand_TOA1']-forecast['TOA1']
    forecast['student_TOA2_to_fill_demand']=forecast['student_demand_TOA2']-forecast['TOA2']
    forecast['student_TOA3_to_fill_demand']=forecast['student_demand_TOA3']-forecast['TOA3']


    forecast.loc[forecast['student_TOA1_to_fill_demand']<0,'student_TOA1_to_fill_demand']=0
    forecast.loc[forecast['student_TOA2_to_fill_demand']<0,'student_TOA2_to_fill_demand']=0
    forecast.loc[forecast['student_TOA3_to_fill_demand']<0,'student_TOA3_to_fill_demand']=0


    forecast=forecast.merge(forecast.groupby(by=['Muni_Heb','sector_for_chinuc']).sum()[['student_TOA1_to_fill_demand']].reset_index(),on=['Muni_Heb','sector_for_chinuc'],suffixes=('','_sum'))
    forecast=forecast.merge(forecast.groupby(by=['Muni_Heb','sector_for_chinuc']).sum()[['student_TOA2_to_fill_demand']].reset_index(),on=['Muni_Heb','sector_for_chinuc'],suffixes=('','_sum'))
    forecast=forecast.merge(forecast.groupby(by=['Muni_Heb','sector_for_chinuc']).sum()[['student_TOA3_to_fill_demand']].reset_index(),on=['Muni_Heb','sector_for_chinuc'],suffixes=('','_sum'))

    forecast=forecast.fillna(0)


    forecast['student_to_fill_TOA1_demand_pre']=forecast['student_TOA1_to_fill_demand']/forecast['student_TOA1_to_fill_demand_sum']
    forecast['student_to_fill_TOA2_demand_pre']=forecast['student_TOA2_to_fill_demand']/forecast['student_TOA2_to_fill_demand_sum']
    forecast['student_to_fill_TOA3_demand_pre']=forecast['student_TOA3_to_fill_demand']/forecast['student_TOA3_to_fill_demand_sum']


    forecast['add_to_TOA1_student_current']=forecast['student_to_fill_TOA1_demand_pre']*forecast['add_from_demad_TOA1_muni_sector']
    forecast['add_to_TOA2_student_current']=forecast['student_to_fill_TOA2_demand_pre']*forecast['add_from_demad_TOA2_muni_sector']
    forecast['add_to_TOA3_student_current']=forecast['student_to_fill_TOA3_demand_pre']*forecast['add_from_demad_TOA3_muni_sector']


    forecast['TOA1']=forecast['TOA1']+forecast['add_to_TOA1_student_current']
    forecast['TOA2']=forecast['TOA2']+forecast['add_to_TOA2_student_current']
    forecast['TOA3']=forecast['TOA3']+forecast['add_to_TOA3_student_current']

    forecast['student']=forecast['TOA1']+forecast['TOA2']+forecast['TOA3']


    sector_for_loop=['SE','AR','UO']
    sector_for_chinuc_for_loop=[ 'Jewish','Arab', 'U_Orthodox']
    num_for_loop=['A1','A2','A3']

    for sc,s in zip(sector_for_chinuc_for_loop,sector_for_loop):
        for n in num_for_loop:
            forecast.loc[forecast['sector_for_chinuc']==sc,'{}{}'.format(s,n)]=forecast['TO{}'.format(n)]
    emp_education_per_student=7

    forecast['emp_from_student']=forecast['student']/emp_education_per_student


    forecast['uni_students_pre_Univ_SE']=forecast['Univ_SE']/forecast['Univ_SE'].sum().item()
    forecast['uni_students_pre_Univ_AR']=forecast['Univ_AR']/forecast['Univ_AR'].sum().item()

    forecast['uni_students_pre_Univ_UO']=forecast['Univ_UO']/forecast['Univ_UO'].sum().item()


    dorms_vs_uni_students=(forecast['student_dorms'].sum().item())/(forecast['univ'].sum().item())


    uni_SE_students=Univ_SE_pre_from_pop_20_30*(forecast.query('sector_for_chinuc=="Jewish"').sum()['pop_20'].item()+forecast.query('sector_for_chinuc=="Jewish"').sum()['pop_25'].item())


    uni_AR_students=Univ_AR_pre_from_pop_20_30*(forecast.query('sector_for_chinuc=="Arab"').sum()['pop_20'].item()+forecast.query('sector_for_chinuc=="Arab"').sum()['pop_25'].item())


    uni_UO_students=Univ_UO_pre_from_pop_20_30*(forecast.query('sector_for_chinuc=="U_Orthodox"').sum()['pop_20'].item()+forecast.query('sector_for_chinuc=="U_Orthodox"').sum()['pop_25'].item())


    sector_for_loop=['SE','AR','UO']

    for s in sector_for_loop:

        forecast['add_Univ_{}_students'.format(s)]=forecast['uni_students_pre_Univ_{}'.format(s)]*uni_SE_students-forecast['Univ_{}'.format(s)]

        forecast['Univ_'.format(s)]=forecast['Univ_{}'.format(s)]+forecast['add_Univ_{}_students'.format(s)]


    forecast['current_univ']=forecast['univ']


    forecast['univ']=forecast['Univ_SE']+forecast['Univ_AR']+forecast['Univ_UO']


    forecast['add_uni_students']=forecast['univ']-forecast['current_univ']


    growth_dorms=((forecast['univ'].sum().item())*dorms_vs_uni_students)/(forecast['student_dorms'].sum().item())

    forecast['student_dorms']=forecast['student_dorms']*growth_dorms
    emp_Education_per_uni_student=0.18

    forecast['emp_uni']=forecast['add_uni_students']*emp_Education_per_uni_student+forecast['emp_uni']


    total_student_yeshiva=forecast.query('main_secto=="U_Orthodox"')[['pop_20','pop_15']].sum().sum()*student_yeshiva_pre_from_age_15_20


    total_student_seminar=forecast.query('main_secto=="U_Orthodox"')[['pop_20','pop_15']].sum().sum()*student_seminar_pre_from_age_15_20
    forecast['student_yeshiva_vs_yeshiva_emp']=forecast['student_yeshiva']/forecast['emp_from_Yeshiva_student']
    forecast['seminar_vs_seminar_emp']=forecast['Seminar']/forecast['emp_from_Seminar_student']


    forecast['student_yeshiva_pre']=forecast['student_yeshiva']/forecast['student_yeshiva'].sum().item()
    forecast['student_seminar_pre']=forecast['Seminar']/forecast['Seminar'].sum().item()


    forecast['student_yeshiva_growth']=(forecast['student_yeshiva_pre']*total_student_yeshiva)/forecast['student_yeshiva']
    forecast['seminar_growth']=(forecast['student_seminar_pre']*total_student_seminar)/forecast['Seminar']

    forecast['student_yeshiva']=forecast['student_yeshiva_pre']*total_student_yeshiva
    forecast['Seminar']=forecast['student_seminar_pre']*total_student_seminar

    forecast['emp_from_Yeshiva_student']=forecast['student_yeshiva']/forecast['student_yeshiva_vs_yeshiva_emp']
    forecast['emp_from_Seminar_student']=forecast['Seminar']/forecast['seminar_vs_seminar_emp']
    forecast['yeshiva_dorms_pop_15']=forecast['yeshiva_dorms_pop_15']*forecast['student_yeshiva_growth']
    forecast['yeshiva_dorms_pop_20']=forecast['yeshiva_dorms_pop_20']*forecast['student_yeshiva_growth']
    forecast['yeshiva_dorms_pop_25']=forecast['yeshiva_dorms_pop_25']*forecast['student_yeshiva_growth']
    col_dorms_yeshiva=['yeshiva_dorms_pop_15', 'yeshiva_dorms_pop_20', 'yeshiva_dorms_pop_25']
    forecast['yeshiva_dorms_pop_sum']=forecast[col_dorms_yeshiva].sum(axis=1)
    forecast['Seminar_dorms_pop_15']=forecast['Seminar_dorms_pop_15']*forecast['seminar_growth']
    forecast['Seminar_dorms_pop_20']=forecast['Seminar_dorms_pop_20']*forecast['seminar_growth']
    forecast['Seminar_dorms_pop_25']=forecast['Seminar_dorms_pop_25']*forecast['seminar_growth']
    col_dorms_seminar=['Seminar_dorms_pop_15', 'Seminar_dorms_pop_20', 'Seminar_dorms_pop_25']
    forecast['seminar_dorms_pop_sum']=forecast[col_dorms_seminar].sum(axis=1)
    forecast['kollim_demand']=(forecast['pop_20']*0.8+forecast['pop_25']*0.65+forecast['pop_30']*0.30+forecast['pop_35']*0.30+forecast['pop_40']*0.30+forecast['pop_45']*0.20+forecast['pop_50']*0.20+forecast['pop_55']*0.20+forecast['pop_60']*0.20)*0.5 #הכפלה בחצי בשביל לקבל אוכלוסיית גברים מעורכת

    forecast.loc[forecast['main_secto']!='U_Orthodox','kollim_demand']=0  #אל אף שאנחנו יודעים שיש כוללים באזורים שהם לא מוגדרים כחרדים

    forecast['add_from_kollim_demand']=0

    forecast.loc[(forecast['main_secto']=='U_Orthodox')&(forecast['kollim_demand']>forecast['student_yeshiva']),'add_from_kollim_demand']=forecast['kollim_demand']-forecast['student_yeshiva']

    forecast['student_yeshiva_and_kollim']=forecast['add_from_kollim_demand']+forecast['student_yeshiva']

    forecast['UO_Hi_Ed']=forecast['student_yeshiva_and_kollim']+forecast['Seminar']

    forecast=forecast.fillna(0)
    forecast['emp_Education']=forecast['emp_from_student']+forecast['emp_from_Yeshiva_student']+forecast['emp_uni']

    emp_Education=forecast.query('main_secto!="Palestinian"')['emp_Education'].sum().item()
    EMP_buffer=EMP_kibolet.set_geometry('geometry_buff').query('F{} > 0'.format(y))

    EMP_buffer=EMP_buffer.dissolve()[['geometry_buff']]

    emp_buffer_taz=gpd.overlay(EMP_buffer,taz)

    emp_buffer_taz['emp_samll_area']=emp_buffer_taz.area

    emp_buffer_taz['emp_pre_from_taz']=emp_buffer_taz['emp_samll_area']/emp_buffer_taz['taz_area']

    taz_num_no_need_okev=emp_buffer_taz.loc[emp_buffer_taz['emp_pre_from_taz']>0.4].Taz_num.to_list()

    forecast['okev']=0

    forecast.loc[(~forecast['Taz_num'].isin(taz_num_no_need_okev))&(taz['main_secto']!="Palestinia"),'okev']=1

    forecast.loc[forecast['main_secto']=="arabs_behined_seperation_wall",'okev']=1
    forecast['emp_okev']=0

    forecast.loc[(forecast['jew']==0)&(forecast['okev']==1),'emp_okev']=forecast['aprt']*okev_factor.loc['arab','city']

    forecast.loc[(forecast['main_secto']=="U_Orthodox")&(~forecast['Muni_Heb'].isin(city_muni))&(forecast['okev']==1),'emp_okev']=forecast['aprt']*okev_factor.loc['U_Orthodox','sub']

    forecast.loc[(forecast['main_secto']=="U_Orthodox")&(forecast['Muni_Heb'].isin(city_muni))&(forecast['okev']==1),'emp_okev']=forecast['aprt']*okev_factor.loc['U_Orthodox','city']

    forecast.loc[(forecast['main_secto']=="Jewish")&(forecast['Muni_Heb'].isin(city_muni))&(forecast['okev']==1),'emp_okev']=forecast['aprt']*okev_factor.loc['Jewish','city']

    forecast.loc[(forecast['main_secto']=="Jewish")&(~forecast['Muni_Heb'].isin(city_muni))&(forecast['okev']==1),'emp_okev']=forecast['aprt']*okev_factor.loc['Jewish','sub']

    emp_okev=forecast['emp_okev'].sum().item()
    forecast=forecast.fillna(0)

    forecast['pop_without_dorms_yeshiva']=forecast['pop']

    forecast['pop']=forecast['pop']+forecast['student_dorms']

    forecast['pop_20_just_from_aprt']=forecast['pop_20']

    forecast['pop_25_just_from_aprt']=forecast['pop_25']

    forecast['pop_20']=forecast['pop_20']+forecast['student_dorms']*0.6

    forecast['pop_25']=forecast['pop_25']+forecast['student_dorms']*0.4
    forecast['pop_15_just_from_aprt']=forecast['pop_15']

    forecast.loc[forecast['main_secto']=="U_Orthodox",'pop']=forecast['pop']+forecast['yeshiva_dorms_pop_sum']

    forecast.loc[forecast['main_secto']=="U_Orthodox",'pop_15']=forecast['pop_15']+forecast['yeshiva_dorms_pop_15']

    forecast.loc[forecast['main_secto']=="U_Orthodox",'pop_20']=forecast['pop_20']+forecast['yeshiva_dorms_pop_20']

    forecast.loc[forecast['main_secto']=="U_Orthodox",'pop_25']=forecast['pop_25']+forecast['yeshiva_dorms_pop_25']
    forecast=forecast.fillna(0)

    forecast['hh']=forecast['aprt']+forecast['student_dorms']/1.5

    forecast['hh']=forecast['hh']+forecast['yeshiva_dorms_pop_sum']
    forecast['work_age']=forecast[work_age].sum(axis=1)

    forecast['under_work_age']=forecast[under_work_age].sum(axis=1)

    forecast['over_work_age']=forecast[over_work_age].sum(axis=1)

    sector=['U_Orthodox','Jewish','Arab','arabs_behined_seperation_wall']

    for s in sector:   
        work_age_factor_woman=work_factor.loc[(work_factor.index==s) & (work_factor['age']=='work_age') & (work_factor['gender']=='woman')& (work_factor['year']==int(y)),'value'].item()
        work_age_factor_man=work_factor.loc[(work_factor.index==s) & (work_factor['age']=='work_age') & (work_factor['gender']=='man')& (work_factor['year']==int(y)),'value'].item()
        under_work_age_factor_woman=work_factor.loc[(work_factor.index==s) & (work_factor['age']=='under_work_age') & (work_factor['gender']=='woman')& (work_factor['year']==int(y)),'value'].item()
        under_work_age_factor_man=work_factor.loc[(work_factor.index==s) & (work_factor['age']=='under_work_age') & (work_factor['gender']=='man')& (work_factor['year']==int(y)),'value'].item()
        over_work_age_factor_woman=work_factor.loc[(work_factor.index==s) & (work_factor['age']=='over_work_age') & (work_factor['gender']=='woman')& (work_factor['year']==int(y)),'value'].item()
        over_work_age_factor_man=work_factor.loc[(work_factor.index==s) & (work_factor['age']=='over_work_age') & (work_factor['gender']=='man')& (work_factor['year']==int(y)),'value'].item()
        
        forecast.loc[forecast['main_secto']==s,'pop_emp']=forecast['work_age']*pre_woman*work_age_factor_woman+forecast['work_age']*pre_man*work_age_factor_man
        forecast.loc[forecast['main_secto']==s,'pop_emp']=forecast['pop_emp']+forecast['under_work_age']*pre_woman*under_work_age_factor_woman+forecast['under_work_age']*pre_man*under_work_age_factor_man
        forecast.loc[forecast['main_secto']==s,'pop_emp']=forecast['pop_emp']+forecast['over_work_age']*pre_woman*over_work_age_factor_woman+forecast['over_work_age']*pre_man*over_work_age_factor_man
    forecast['pop_emp_employed']=0

    forecast.loc[forecast['main_secto']=="U_Orthodox",'pop_emp_employed']=forecast['pop_emp']*0.96

    forecast.loc[forecast['main_secto']=="Jewish",'pop_emp_employed']=forecast['pop_emp']*0.97

    forecast.loc[forecast['jew']==0,'pop_emp_employed']=forecast['pop_emp']*0.96
    forecast=forecast.set_index('Taz_num')

    forecast['commuting']=gpd.sjoin(make_point(taz)[['Taz_num','centroid']],commuting[['commuting', 'geometry']]).set_index('Taz_num')['commuting']/100

    forecast['pop_emp_employed_out_of_jtmt_area']=forecast['pop_emp_employed']*forecast['commuting']

    emp_from_jtmt_area=forecast['pop_emp_employed'].sum().item()-forecast['pop_emp_employed_out_of_jtmt_area'].sum().item()

    emp_in_jtmt_area=emp_from_jtmt_area*1.06 #יוממות פנימה מחוץ למרחב

    emp_in_jtmt_area_without_mobile=emp_in_jtmt_area*0.94 #הפחחת עובדים ניידים
    add_emp_not_okev=emp_in_jtmt_area_without_mobile-emp_Education-emp_okev-emp_not_okev_current

    add_emp_not_okev_kibolet=EMP_kibolet['F{}'.format(y)].sum().item()-emp_not_okev_current
            
    add_emp_not_okev_filling=add_emp_not_okev/add_emp_not_okev_kibolet

    EMP_kibolet['emp_current']=(EMP_kibolet['F{}'.format(y)]-EMP_kibolet['emp_current'])*add_emp_not_okev_filling+EMP_kibolet['emp_current']

    emp_not_okev_current=EMP_kibolet['emp_current'].sum().item()

    col=['Taz_num','ID','prec_from_id']

    df=EMP_kibolet_by_taz.reset_index()[col].merge(EMP_kibolet,on='ID',how='left')

    df['emp_current']=df['emp_current']*df['prec_from_id']

    forecast['emp_not_okev']=df.drop(columns=['geometry', 'geometry_buff']).pivot_table(index='Taz_num',aggfunc='sum')[['emp_current']]

    forecast=forecast.fillna(0)

    forecast['total_emp']=forecast['emp_not_okev']+forecast['emp_okev']+forecast['emp_Education']
    forecast.loc[forecast['main_secto']!="U_Orthodox",'pop']=forecast['pop']+forecast['yeshiva_dorms_pop_sum']

    forecast.loc[forecast['main_secto']!="U_Orthodox",'pop_15']=forecast['pop_15']+forecast['yeshiva_dorms_pop_15']

    forecast.loc[forecast['main_secto']!="U_Orthodox",'pop_20']=forecast['pop_20']+forecast['yeshiva_dorms_pop_20']

    forecast.loc[forecast['main_secto']!="U_Orthodox",'pop_25']=forecast['pop_25']+forecast['yeshiva_dorms_pop_25']

    col=['agri', 'Indus', 'Com_hotel', 'Business', 'Public']

    forecast=forecast.join(emp_category_type[col]).fillna(0)

    for i in col:
        forecast['{}'.format(i)]=forecast['{}'.format(i)]*(forecast['emp_not_okev']+forecast['emp_okev'])

    locals()['forecast_{}'.format(y)]=forecast


for y in years:

    taz=locals()['forecast_{}'.format(y)]
    
    software_folder_location=r'W:\Data\Forecast\Tools\forecast_git\create_forecast_basic\current'


    col=['Taz_num','geometry']
    taz_border=up_load_shp(r'W:\Data\Forecast\Tools\forecast_git\create_forecast_basic\background_files\TAZ_V4_{}_with_geo_info.shp'.format(TAZ_V4_date))[col]
    forecast_point = make_point(taz_border)

    urban = up_load_gdb(r'{}\background_files\GIS_jtmt_forcast_v_3_2_Published.gdb'.format(software_folder_location), 'TAZ_V3_2_220123_urban')

    forecast_point_urban = forecast_point.sjoin(urban)[['Taz_num', 'BaseProjections2040_csv_urban']]
    taz = (taz.merge(forecast_point_urban, on='Taz_num', how='left'))
    taz.rename(columns={'BaseProjections2040_csv_urban': 'urban'}, inplace=True)


    taz['tazSector']=1 #ערבי


    taz.loc[taz['main_secto']=='U_Orthodox','tazSector']=2


    taz.loc[taz['main_secto']=='Jewish','tazSector']=3


    taz.loc[taz['main_secto']=='Palestinian','tazSector']=4


    poly_pumas=up_load_shp(r'{}\background_files\poly_pumas.shp'.format(software_folder_location))


    col_old=['poly_puma',  'F3', 'F2', 'F1', 'geometry']


    col_new=['poly_puma',  '3', '2', '1', 'geometry']


    poly_pumas=drop_geo(change_cols_names(poly_pumas,col_old,col_new))


    pumas_by_poly_sector=poly_pumas.melt(id_vars='poly_puma',var_name='tazSector',value_name='PUMA')


    pumas_by_poly_sector['tazSector']=pumas_by_poly_sector['tazSector'].astype(int)


    taz=add_geo_info_shp(taz,taz_border,software_folder_location,'poly_pumas','poly_puma')


    taz=taz.merge(pumas_by_poly_sector,on=['poly_puma','tazSector'],how='left')


    taz.loc[taz['PUMA']==0,'PUMA']=999


    taz.loc[taz['pop']==0,'PUMA']=999


    taz.loc[taz['main_secto']=='Palestinian','PUMA']=999


    taz.loc[taz['jeru_metro']==0,'PUMA']=999


    taz['REGION'] = 1
    taz['slop'] = 0


    taz=add_geo_info_shp(taz,taz_border,software_folder_location,'schDistrict','ID').rename(columns={'ID':'SCHOOLDISTRICT'})


    taz.loc[taz['SCHOOLDISTRICT']==0,'SCHOOLDISTRICT']=999


    taz['yosh']=0

    taz.loc[taz['zonetype']=='Judea and Samaria','yosh']=1

    taz['jerusalem_city']=0

    taz.loc[taz['in_jerusal']=='yes','jerusalem_city']=1

    taz=taz.reset_index()
    file_date=pd.Timestamp.today().strftime('%y%m%d')


    col_needed=['Taz_num',
    'yosh',
    'jeru_metro',
    'jerusalem_city',
    'main_secto',
    'hh',
    'pop',
    'pop_0',
    'pop_5',
    'pop_10',
    'pop_15',
    'pop_20',
    'pop_25',
    'pop_30',
    'pop_35',
    'pop_40',
    'pop_45',
    'pop_50',
    'pop_55',
    'pop_60',
    'pop_65',
    'pop_70',
    'pop_75up',
    'total_emp',
    'Indus',
    'Com_hotel',
    'Business',
    'Public',
    'emp_Education',
    'agri',
    'student',
    'univ',
    'UO_Hi_Ed',
    'pop_emp_employed',
    'slop',
    'urban']

    col_new_name=['TAZ',
    'yosh',
    'in_jerusalem_metropolin',
    'jerusalem_city',
    'sector',
    'hh_total',
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
    'pop_emp_employed',
    'slop',
    'urban']
    file_date=pd.Timestamp.today().strftime('%y%m%d')

    output_location=r'W:\Data\Forecast\forecast_by_version\V4\JTMT'


    change_cols_names(taz, col_needed, col_new_name).to_excel(r'{}\BaseProjections{}_{}.xlsx'.format(output_location,y,file_date),index=False)


    taz['DISTRICT']=999


    taz.loc[taz['jew']==0,'DISTRICT']=1
    taz.loc[(taz['main_secto']=='U_Orthodox')&(taz['in_jerusal']==1),'DISTRICT']=2
    taz.loc[(taz['main_secto']=='Jewish')&(taz['in_jerusal']==1),'DISTRICT']=3
    taz.loc[(taz['main_secto']=='Jewish')&(taz['in_jerusal']==0)&(taz['jeru_metro']==1),'DISTRICT']=5
    taz.loc[(taz['main_secto']=='U_Orthodox')&(taz['in_jerusal']==0)&(taz['jeru_metro']==1),'DISTRICT']=6


    taz.loc[taz['pop']==0,'DISTRICT']=999


    col_needed=['Taz_num','Agg_taz_nu','PUMA','DISTRICT','REGION','SCHOOLDISTRICT']

    col_new_name=['TAZ','AGG_TAZ','PUMA','DISTRICT','REGION','SCHOOLDISTRICT']


    change_cols_names(taz, col_needed, col_new_name).to_excel(r'{}\puma{}_{}.xlsx'.format(output_location,y,file_date),index=False)


    col_with_fix_num=['area',
    'CITYCODE1',
    'CITYCODE2',
    'CITYCODE3',
    'CITYCODE4',
    'codeseq',
    'codeseqCons',
    'county',
    'majunivenr',
    'parktot',
    'superZone',
    'Taz1']


    taz[col_with_fix_num]=1


    taz['UNIVENRORTHFEMALE']=taz['Univ_UO']/2
    taz['UNIVENRORTHMALE']=taz['Univ_UO']/2


    forecast_point = make_point(taz_border)
    hibiz = up_load_shp(r'{}\background_files\highBusinessFlag.shp'.format(software_folder_location))[['HighBiz', 'geometry']]


    forecast_point_hibiz = forecast_point.sjoin(hibiz)[['Taz_num', 'HighBiz']]

    taz = taz.merge(forecast_point_hibiz, on='Taz_num', how='left')

    taz.rename(columns={'HighBiz': 'highBusinessFlag'}, inplace=True)


    col_parking=['FreeBuffer',
    'PaidBuffer',
    'Rest_EmpBuffer',
    'searchtime',
    'walktime',
    'cost']


    for c in col_parking:
        taz=add_geo_info_gdb(taz,taz_border,software_folder_location,'parking_abm',c,c)


    taz=add_geo_info_gdb(taz,taz_border,software_folder_location,'emp_EI','EIProp','EIProp')


    taz['perScaled']=1-taz['EIProp']


    taz['ieold']=0
    taz.loc[taz['jeru_metro']==1,'ieold']=taz['commuting']
    taz['IEProp']=taz['ieold']


    col_needed=['Taz_num',
    'Taz_num',
    'hh',
    'PUMA',
    'DISTRICT',
    'county',
    'area',
    'parktot',
    'majunivenr',
    'tazSector',
    'Indus',
    'Com_hotel',
    'Business',
    'Public',
    'emp_Education',
    'agri',
    'total_emp',
    'UOA1',
    'UOA2',
    'UOA3',
    'SEA1',
    'SEA2',
    'SEA3',
    'ARA1',
    'ARA2',
    'ARA3',
    'TOA1',
    'TOA2',
    'TOA3',
    'Univ_AR',
    'Univ_SE',
    'UNIVENRORTHMALE',
    'UNIVENRORTHFEMALE',
    'ieold',
    'superZone',
    'IEProp',
    'Taz1',
    'perScaled',
    'EIProp',
    'CITYCODE1',
    'CITYCODE2',
    'CITYCODE3',
    'CITYCODE4',
    'codeseq',
    'codeseqCons',
    'PaidBuffer',
    'Rest_EmpBuffer',
    'FreeBuffer',
    'SCHOOLDISTRICT',
    'SCHOOLDISTRICT',
    'highBusinessFlag',
    'searchtime',
    'walktime',
    'cost']


    col_new_name=['maz',
    'taz',
    'hh_total',
    'puma',
    'district',
    'county',
    'area',
    'parktot',
    'majunivenr',
    'tazSector',
    'Indus',
    'Com_hotel',
    'Off_Bsness',
    'Public',
    'Education',
    'Agri',
    'totemp',
    'UOA1',
    'UOA2',
    'UOA3',
    'SEA1',
    'SEA2',
    'SEA3',
    'ARA1',
    'ARA2',
    'ARA3',
    'TOA1',
    'TOA2',
    'TOA3',
    'UNIVENRARAB',
    'UNIVENRSEC',
    'UNIVENRORTHMALE',
    'UNIVENRORTHFEMALE',
    'ieold',
    'superZone',
    'IEProp',
    'Taz1',
    'perScaled',
    'EIProp',
    'CITYCODE1',
    'CITYCODE2',
    'CITYCODE3',
    'CITYCODE4',
    'codeseq',
    'codeseqCons',
    'PaidBuffer',
    'Rest_EmpBuffer',
    'FreeBuffer',
    'schDistrict',
    'schDistrictAgg',
    'highBusinessFlag',
    'searchtime',
    'walktime',
    'cost']


    change_cols_names(taz, col_needed, col_new_name).to_excel(r'{}\SED_{}_{}.xlsx'.format(output_location,y,file_date),index=False)

    save_file_path=r'{}\Intermediates'.format(software_data_folder_location)

    save_excel_path=r'{}\{}_forecast_{}_full.xlsx'.format(save_file_path,file_date,y)

    taz.to_excel(save_excel_path,index=False)

