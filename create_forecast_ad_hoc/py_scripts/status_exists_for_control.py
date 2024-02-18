import pandas as pd
from functions import up_load_df

def export_status_exists(forecast, software_data_folder_location,client_data_folder_location, file_date):
    forecast_2020=up_load_df(r'{}\background_files'.format(software_data_folder_location),'2020_jtmt_forcast_full_230720')

    col=[]

    col_20=['Taz_num','Taz_name',
    'main_secto',
    'aprt_20', 'pop_without_dorms_yeshiva',
    'student_toddlers',
    'student_gov',
    'cbs_muni_student_left_by_pre_of_demand_left',
    'uni_students', 'student_dorms',
    'emp_from_uni_student',
    'student_yeshiva',
    'emp_okev',
    'emp_not_okev','student']

    forecast_2020=pd.merge(forecast[col].reset_index(),forecast_2020[col_20],how='left',on='Taz_num').fillna(0)

    save_excel_path=r'{}\For_approval\{}_forecast_2020_For_approval.xlsx'.format(client_data_folder_location,file_date)

    forecast_2020[col_20].to_excel(save_excel_path,index=False)
    return forecast_2020[col_20]

