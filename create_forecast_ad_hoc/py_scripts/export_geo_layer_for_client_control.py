import pandas as pd

def export_geo_layer(forecast, client_data_folder_location,file_date):
    save_shp_path=r'{}\For_approval\{}_taz_for_approval.shp'.format(client_data_folder_location,file_date)
    
    col=['Taz_num','Name_hebre','Muni_Eng', 'main_sector', 'classification_name','Student_by_Classrooms','geometry']

    
    forecast[col].to_file(save_shp_path,index=False,encoding='UTF-8')
    return forecast