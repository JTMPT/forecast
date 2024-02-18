import pandas as pd
from functions import up_load_df,delet_and_add_by_TAZ

import pandas as pd
from functions import up_load_df, delet_and_add_by_TAZ

def export_forecast(forecast, client_data_folder_location, file_date, forecast_version):
    col = [
        'Taz_num', 
        'Name_hebre', 
        'main_sector', 
        'classification_name', 
        'aprt_20', 
        'add_aprt', 
        'aprt', 
        'hh_size', 
        'pop_without_dorms_yeshiva', 
        'pop_emp_employed', 
        'student_20', 
        'student', 
        'uni_students_20', 
        'add_uni_students', 
        'uni_students', 
        'student_dorms_20', 
        'add_uni_dorms', 
        'student_dorms', 
        'student_yeshiva_and_kollim', 
        'add_old_age_home', 
        'emp_from_student', 
        'emp_from_uni_student', 
        'emp_from_Yeshiva_student', 
        'emp_Education', 
        'emp_okev', 
        'add_emp_Business', 
        'add_emp_Commerce', 
        'add_emp_Industry', 
        'add_emp_Public', 
        'add_emp_Tourism', 
        'total_emp'
    ]

    save_excel_path = r'{}\For_approval\{}_forecast_2040_{}_for_approval.xlsx'.format(client_data_folder_location, file_date, forecast_version)

    forecast[col].to_excel(save_excel_path, index=False)

    BaseProjections2040 = pd.read_csv(r'W:\Data\Forecast\Tools\creat_forecast_ad_hoc\background_files\BaseProjections2040.csv')
    puma2040 = pd.read_csv(r'W:\Data\Forecast\Tools\creat_forecast_ad_hoc\background_files\puma2040.csv')

    forecast.loc[forecast['Taz_num'] < 7001, 'AGG_TAZ'] = forecast['Taz_num'] // 100
    forecast.loc[forecast['Taz_num'] >= 7001, 'AGG_TAZ'] = forecast['Taz_num'] // 10

    forecast.rename(columns={'Taz_num': 'TAZ'}, inplace=True)

    save_excel_path = r'{}\{}_puma2040.csv'.format(client_data_folder_location, file_date)

    delet_and_add_by_TAZ(forecast, puma2040).to_csv(save_excel_path, index=False)

    forecast_col =[
         'TAZ', 
         'yosh', 
         'in_jerusalem_metropolin', 
         'jerusalem_city', 
         'main_sector', 
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
         'uni_students',
         'student_yeshiva_and_kollim', 
         'pop_emp_employed', 
         'slop', 
         'urban'
      ] 

    format_needed_col = [
      'TAZ', 
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
      'slope', 
      'urban'
      ]


    forecast_for_model = forecast[forecast_col]
    forecast_for_model.columns = format_needed_col

    save_excel_path = r'{}\{}_BaseProjections2040_{}.csv'.format(client_data_folder_location, file_date, forecast_version)
    delet_and_add_by_TAZ(forecast_for_model, BaseProjections2040).to_csv(save_excel_path, index=False)

    return
