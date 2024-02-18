import pandas as pd


def export_index_layer(index_layer, client_data_folder_location,file_date,forecast_version):
    col=['id',
    'add_aprt',
    'add_aprt_nominally',
    'add_old_age_home',
    'add_old_age_home_nominally',
    'add_uni_dorms',
    'add_uni_dorms_nominally',
    'add_uni_students',
    'add_uni_students_nominally',
    'Classrooms','Classrooms_nominally',
    'Commerce_m2',
    'Commerce_m2_nominally',
    'add_emp_Commerce',
    'Tourism_m2',
    'Tourism_m2_nominally',
    'add_emp_Tourism',
    'Business_m2',
    'Business_m2_nominally',
    'add_emp_Business',
    'Public_m2',
    'Public_m2_nominally',
    'add_emp_Public',
    'Industry_m2',
    'Industry_m2_nominally',
    'add_emp_Industry']
    
    save_excel_path=r'{}\For_approval\Reference_tabels\{}_index_2040_{}_For_approval.xlsx'.format(client_data_folder_location,file_date,forecast_version)
    index_layer.pivot_table(index='id',aggfunc=sum).reset_index()[col].to_excel(save_excel_path,index=False)

    return index_layer