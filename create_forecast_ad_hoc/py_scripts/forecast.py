import os
from find_file import find_files_with_pattern
from functions import up_load_gdb

def clientTaz(client_data_folder_location):
    folder_path=r'{}\For_approval\Reference_tabels\shp'.format(client_data_folder_location)
    gpd_name='tochnit_check.gdb'
    pattern='TAZ_V'
    matching_files=find_files_with_pattern(folder_path, pattern)

    # אם יש שכבות חדשות
    if len(matching_files) > 0:
        filename=os.path.basename(matching_files[0])
        filepath=r'{}\For_approval\Reference_tabels\shp\{}'.format(folder_path, filename)
        print(True)
    # אם אין שכבות חדשות
    else:
        print(False)

    forecast = up_load_gdb(r'{}\{}'.format(folder_path,gpd_name),'TAZ_211028_V3_Published_with_client_changes')

    return 'forecast'