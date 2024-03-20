import pandas as pd
from functions import up_load_df, up_load_shp
from client_documentation import add_layer_for_documentation

def uploading_index_table(client_data_folder_location, index_file_name):
    borders_index=up_load_shp(r'{}\For_approval\Reference_tabels\shp\gvul_index.shp'.format(client_data_folder_location))

    add_layer_for_documentation(client_data_folder_location, 'gvul_index')

    index=up_load_df(r'{}\For_approval\Reference_tabels'.format(client_data_folder_location),index_file_name)
    index=pd.merge(borders_index,index,on='id',how='right')
   
    return index