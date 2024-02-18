import pandas as pd
from functions import up_load_df

def adding_an_addition(index_by_taz,forecast,forecast_2020,software_data_folder_location,client_data_folder_location,forecast_version):
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

    col=[ 'add_aprt','add_uni_dorms', 'add_emp_Business',
    'add_emp_Commerce',
    'add_emp_Industry',
    'add_emp_Public',
    'add_emp_Tourism','add_uni_students','add_old_age_home','Classrooms']

    forecast=forecast.merge(index_by_taz[col],left_index=True,right_index=True,how='left')

    forecast=forecast.fillna(0)

    col=['aprt_20','student','uni_students','student_dorms','student_yeshiva','emp_not_okev']

    forecast_2020=forecast_2020.set_index('Taz_num')

    forecast=forecast.merge(forecast_2020[col],left_index=True,right_index=True,how='left')

    forecast=forecast.rename(columns={'student':'student_20','uni_students':'uni_students_20','student_dorms':'student_dorms_20','student_yeshiva':'student_yeshiva_and_kollim_20','emp_not_okev':'emp_not_okev_20'})

    age_des_types=up_load_df(r'{}\background_files'.format(software_data_folder_location),'age_des_types')

    forecast=forecast.merge(age_des_types,on='classification_name',how='left').fillna(0)

    #### יח"ד של השכונה ויצירת אנשים לפי קטלוג
    forecast['aprt']=forecast['aprt_20']+forecast['add_aprt']

    forecast['pop_without_dorms_yeshiva']=forecast['aprt']*forecast['hh_size']

    #### תלמידים בעקבות האוכלוסיה
    forecast['student_demand_pre']=forecast['pop_0']/5*2+forecast['pop_5']+forecast['pop_10']+forecast['pop_15']/5*3+forecast['pop_0']/5*3*0.5

    forecast['student_demand']=forecast['student_demand_pre']*forecast['pop_without_dorms_yeshiva']

    total_student_to_fill_forecast_demand=forecast['student_demand'].sum()-forecast['student_20'].sum()

    forecast['student_to_fill_demand']=forecast['student_demand']-forecast['student_20']

    forecast.loc[forecast['student_to_fill_demand']<0,'student_to_fill_demand']=0

    forecast['student_to_fill_demand_pre']=forecast['student_to_fill_demand']/forecast['student_to_fill_demand'].sum().item()

    forecast['student']=forecast['student_to_fill_demand_pre']*total_student_to_fill_forecast_demand+forecast['student_20']

    forecast.loc[forecast['Student_by_Classrooms']==1,'student']=forecast['Classrooms']*30

    forecast.loc[forecast['Student_by_Classrooms']==1,'student']=forecast['Classrooms']*30

    #### תעסוקה בעקבות תלמידים
    forecast['emp_from_student']=forecast['student']/emp_education_per_student

    #### סטודנטים
    forecast['student_dorms']=forecast['add_uni_dorms']*uni_student_dorm_fill+forecast['student_dorms_20']

    #### מספר הסטודנטים יהיה בהתאם לגודל של הקיים
    forecast['uni_students']=forecast['uni_students_20']+forecast['add_uni_students']

    #### תעסוקה בעקבות סטודנטים
    forecast['emp_from_uni_student']=forecast['uni_students']*emp_Education_per_uni_student

    #### תלמידי ישיבה ותעסוקה מישיבה
    forecast['student_yeshiva_and_kollim']=forecast['student_yeshiva_and_kollim_20']*1.15 #גידול מינורי

    forecast['emp_from_Yeshiva_student']=forecast['student_yeshiva_and_kollim']*emp_Education_per_Yeshiva_student

    forecast['emp_Education']=forecast['emp_from_student']+forecast['emp_from_Yeshiva_student']+forecast['emp_from_uni_student']

    #### תעסוקה לא עוקב
    #### מקומות עבודה תעשייה

    forecast['Indus']=forecast['add_emp_Industry']+forecast['emp_not_okev_20']*0.7 #חלוקת מצב הקיים הערכה 

    #### מקומות עבודה מסחר ומלונאות
    forecast['Com_hotel']=forecast['add_emp_Commerce']+forecast['add_emp_Tourism']+forecast['emp_not_okev_20']*0.2 #חלוקת מצב הקיים הערכה 

    #### מקומות עבודה משרדים
    forecast['Business']=forecast['add_emp_Business']+forecast['emp_not_okev_20']*0.1 #חלוקת מצב הקיים הערכה 

    forecast['agri']=0

    forecast['Public']=0

    #### מקומות עבודה עוקב משקי בית 
    forecast['emp_okev']=forecast['aprt']*precent_emp_per_hh

    #### מקומות עבודה עוקב אוכלוסייה
    list_category=[	'Com_hotel','Business','Indus','Public'] 
    list_category_index=['Commerce','Business','Industry','Public'] 

    for c,i in zip(list_category, list_category_index):
        forecast['{}'.format(c)]= forecast['{}'.format(c)].fillna(0)+forecast['emp_okev']*locals()['{}_precent_per_hh'.format(i)]

    #### סך מקומות עבודה
    col_to_sum_emp=['Indus',
    'Com_hotel',
    'Business',
    'Public',
    'emp_Education','agri']

    forecast['total_emp']=forecast[col_to_sum_emp].sum(axis=1)

    #### המרת התפלגות גילים מאחוזים למספרים מוחלטים
    col=['pop_0',
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
    'pop_75up']

    forecast[col]=forecast[col].multiply(forecast['pop_without_dorms_yeshiva'], axis="index")

    #### הוספת סטודנטים למשקי הבית, אוכלוסיה ותפלגות גילים
    forecast['pop']=forecast['pop_without_dorms_yeshiva']+forecast['student_dorms']

    forecast['pop_20']=forecast['pop_20']+forecast['student_dorms']*0.6

    forecast['pop_25']=forecast['pop_25']+forecast['student_dorms']*0.4

    forecast['hh']=forecast['aprt']+forecast['student_dorms']/uni_student_dorm_fill

    #### הוספת דיור מוגן למשקי הבית, אוכלוסיה ותפלגות גילים
    forecast['pop']=forecast['pop']+forecast['add_old_age_home']*old_age_home_fill

    forecast['pop_75up']=forecast['pop_75up']+forecast['add_old_age_home']*old_age_home_fill

    forecast['hh']=forecast['hh']+forecast['add_old_age_home']

    #### יצירת עמודת יוצאים לעבודה מתוך האוכלוסייה שגרה
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

    forecast['work_age']=forecast[work_age].sum(axis=1)

    forecast['under_work_age']=forecast[under_work_age].sum(axis=1)

    forecast['over_work_age']=forecast[over_work_age].sum(axis=1)

    sector='U_Orthodox'

    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['work_age']*pre_woman*0.75+forecast['work_age']*pre_man*0.44
    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['pop_emp']+forecast['under_work_age']*pre_woman*0.07+forecast['under_work_age']*pre_man*0.09
    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['pop_emp']+forecast['over_work_age']*pre_woman*0.05+forecast['over_work_age']*pre_man*0.09

    sector='Jewish'

    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['work_age']*pre_woman*0.84+forecast['work_age']*pre_man*0.87
    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['pop_emp']+forecast['under_work_age']*pre_woman*0.20+forecast['under_work_age']*pre_man*0.15
    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['pop_emp']+forecast['over_work_age']*pre_woman*0.05+forecast['over_work_age']*pre_man*0.09

    sector='Arab'

    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['work_age']*pre_woman*0.23+forecast['work_age']*pre_man*0.78
    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['pop_emp']+forecast['under_work_age']*pre_woman*0.2+forecast['under_work_age']*pre_man*0.15
    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['pop_emp']+forecast['over_work_age']*pre_woman*0.05+forecast['over_work_age']*pre_man*0.09

    sector='arabs_behined_seperation_wall'

    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['work_age']*pre_woman*0.23+forecast['work_age']*pre_man*0.78
    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['pop_emp']+forecast['under_work_age']*pre_woman*0.2+forecast['under_work_age']*pre_man*0.15
    forecast.loc[forecast['main_sector']==sector,'pop_emp']=forecast['pop_emp']+forecast['over_work_age']*pre_woman*0.05+forecast['over_work_age']*pre_man*0.09

    ## חישוב אבטלה
    forecast['pop_emp_employed']=0

    forecast.loc[forecast['main_sector']=="U_Orthodox",'pop_emp_employed']=forecast['pop_emp']*0.95

    forecast.loc[forecast['main_sector']=="Jewish",'pop_emp_employed']=forecast['pop_emp']*0.96

    arab_sector=['arabs_behined_seperation_wall','Arab']

    forecast.loc[forecast['main_sector'].isin(arab_sector),'pop_emp_employed']=forecast['pop_emp']*0.98

    #### הוספת תלמידי ישיבה  למשקי הבית, אוכלוסיה ותפלגות גילים
    forecast['hh']=forecast['hh']+forecast['student_yeshiva_and_kollim']

    forecast['pop']=forecast['pop']+forecast['student_yeshiva_and_kollim']

    forecast['pop_15']=forecast['pop_15']+forecast['student_yeshiva_and_kollim']*0.7

    forecast['pop_20']=forecast['pop_20']+forecast['student_yeshiva_and_kollim']*0.3


    return forecast