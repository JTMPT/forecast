import os
import pandas as pd
from adding_an_addition_following_the_index import adding_an_addition
from functions import change_Muni_Heb_to_Muni_Eng
from division_into_traffic_zones_of_plans import division_into_traffic_zones
from export_geo_layer_for_client_control import export_geo_layer
from export_index_layer_for_client_control import export_index_layer
from forecast import clientTaz
from geographical_features import add_geographical_Features
from index_layer import index_layer_fun
from status_exists_for_control import export_status_exists
from uploading_index_table_elements import uploading_index_table
from uploading_index_table_elements import uploading_index_table
from export_forecast_2040 import export_forecast
#הגדרות כלליות

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

file_date=pd.Timestamp.today().strftime('%y%m%d')

#העלת משתנים להרצת הקוד
path = os.getcwd()
software_data_folder_location = r'{}\create_forecast_ad_hoc'.format(path)
print(software_data_folder_location)
df_inputs_outputs = pd.read_excel(r'{}\inputs_outputs.xlsx'.format(software_data_folder_location))


create_forecast_basic_location=df_inputs_outputs['location'][0]
forecast_version_basic_folder_location=df_inputs_outputs['location'][4]
client_data_folder_location=df_inputs_outputs['location'][1]
forecast_version=df_inputs_outputs['location'][2]
v_date=df_inputs_outputs['location'][3]
index_file_name='index_format_for_creating_forecast_jtmt_input_{}_{}'.format(forecast_version,v_date)

# העלת אזורי תנועה לחישוב
forecast=clientTaz(client_data_folder_location)
#### הוספת מאפיינים גיאוגרפים לאזורי תנועה
forecast=add_geographical_Features(forecast, software_data_folder_location)

#### שינוי עמודה Muni_Heb
forecast=change_Muni_Heb_to_Muni_Eng(software_data_folder_location, forecast)

#### ייצוא שכבת אזורי תנועה לבקרת לקוח
forecast=export_geo_layer(forecast, client_data_folder_location, file_date)

#### מצב קיים לבקרה
forecast_2020=export_status_exists(create_forecast_basic_location, forecast_version_basic_folder_location, forecast, software_data_folder_location,client_data_folder_location, file_date)

#### העלאת מרכיבי טבלת אינדקס
index=uploading_index_table(forecast, client_data_folder_location, index_file_name)

## חלוקה לאזורי תנועה של התכניות
divided_index=division_into_traffic_zones(index,forecast)

### שכבת אינדקס
index_layer=index_layer_fun(divided_index, software_data_folder_location)

#### ייצוא שכבת אינדקס לבקרת לקוח
index_layer_for_client_control=export_index_layer(index_layer,client_data_folder_location,file_date,forecast_version)

### חישוב תחזית
#### הוספת תוספת בעקבות האינדקס
forecast=adding_an_addition(index_layer,forecast,forecast_2020,software_data_folder_location,client_data_folder_location,forecast_version)

#ייצוא תוצאות
export_forecast(forecast, client_data_folder_location, file_date, forecast_version,software_data_folder_location)

print('Done')