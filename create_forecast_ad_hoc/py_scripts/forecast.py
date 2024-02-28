from functions import up_load_gdb

def clientTaz(client_data_folder_location):
    folder_path=r'{}\For_approval\Reference_tabels\shp'.format(client_data_folder_location)
    gpd_name='tochnit_check.gdb'

    forecast = up_load_gdb(r'{}\{}'.format(folder_path,gpd_name),'TAZ_211028_V3_Published_with_client_changes')
    return forecast
