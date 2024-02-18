import pandas as pd
import geopandas

def index_layer_fun(divided_index):
    index=divided_index.fillna(0)

        #מקדים לייצרת תעסוקה עוקב משקי בית
    Industry_precent_per_hh=0
    Commerce_precent_per_hh=0.55
    Business_precent_per_hh=0.2
    Public_precent_per_hh=0.25
    Agriculture_precent_per_hh=0

    precent_emp_per_hh=0.0

    #מקדימים לייצרת מקומות עבודה מ"ר לפי ייעוד קרקע
    m2_Industry_to_emp=200
    m2_Commerce_Hotel_to_emp=30
    m2_Business_to_emp=30
    m2_Public_to_emp=60
    m2_Agriculture_to_emp=0
    m2_Education_to_emp=0
    m2_Commerce_to_emp=m2_Commerce_Hotel_to_emp
    m2_Tourism_to_emp=100

    #מילוי

    old_age_home_fill=1.5
    uni_student_dorm_fill=3


    #מקדימי תעסוקה בעקבות חינוך


    emp_education_per_student=3.75
    emp_Education_per_uni_student=0.1
    emp_Education_per_Yeshiva_student=0.10


    convert_dict={
    'add_old_age_home': float,
    'add_aprt': float,
    'Commerce_m2': float,
    'Business_m2': float,
    'Tourism_m2': float,
    'Public_m2': float,
    'Industry_m2': float,
    'emp_Public': float,
    'emp_Education': float,
    'emp_Commerce': float,
    'emp_Business': float,
    'emp_Industry': float,
    'emp_Tourism': float,
    'Classrooms': float,
    'F2025': float,
    'F2030': float,
    'F2035': float,
    'F2040': float,
    'F2045': float,
    'F2050': float,
    'F2050_plus': float,
    'Risk_factor': float,
    'emp_fill_factor': float}

    index = index.astype(convert_dict)

    col_to_sum=['F2025',
    'F2030',
    'F2035',
    'F2040']

    index['precent_till_2040']=index[col_to_sum].sum(axis=1)

    index['add_aprt_nominally']=index['add_aprt']

    index['add_aprt']=index['add_aprt']*index['precent_till_2040']*index['Risk_factor']

    index['Classrooms_nominally']=index['Classrooms']

    index['Classrooms']=index['Classrooms']*index['precent_till_2040']*index['Risk_factor']

    index['add_old_age_home_nominally']=index['add_old_age_home']

    index['add_old_age_home']=index['add_old_age_home']*index['precent_till_2040']*index['Risk_factor']

    index['add_uni_students_nominally']=index['add_uni_students']

    index['add_uni_students']=index['add_uni_students']*index['precent_till_2040']*index['Risk_factor']

    index['add_uni_dorms_nominally']=index['add_uni_dorms']

    index['add_uni_dorms']=index['add_uni_dorms']*index['precent_till_2040']*index['Risk_factor']

    list_category=['Commerce','Business','Industry','Tourism','Public']   #'Agriculture','Education','Public'
    for c in list_category:
        index['{}_m2_nominally'.format(c)]=index['{}_m2'.format(c)]
        index['{}_m2'.format(c)]=index['{}_m2'.format(c)]*index['Risk_factor']*index['emp_fill_factor']*index['precent_till_2040']
        index['emp_{}_nominally'.format(c)]=index['emp_{}'.format(c)]
        index['emp_{}'.format(c)]=index['emp_{}'.format(c)]*index['precent_till_2040']*index['Risk_factor']*index['emp_fill_factor']
        index['add_emp_{}'.format(c)]=index['emp_{}'.format(c)]+index['{}_m2'.format(c)]/locals()['m2_{}_to_emp'.format(c)]

    drop_geometry=index.drop(['geometry'], axis=1)
    index_by_taz=drop_geometry.pivot_table(index='Taz_num', aggfunc='sum').fillna(0)
    return index_by_taz