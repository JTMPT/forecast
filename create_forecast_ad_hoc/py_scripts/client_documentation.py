import pandas as pd

def create_client_documentation_df(client_data_folder_location, forecast_version_num):
    # Define the data
    data = {
        'Value': [forecast_version_num, 'כן', 'שכבות']
    }

    # Create the DataFrame
    documentation_df = pd.DataFrame(data, index=['גירסא', 'איזורי תנועה חדשים', 'שכבות'])

    documentation_df.to_excel(r'{}\documentation_df.xlsx'.format(client_data_folder_location))
    return documentation_df

def add_layer_for_documentation(client_data_folder_location, layer):
    excel_file_path = r'{}\documentation_df.xlsx'.format(client_data_folder_location)

    documentation_df = pd.read_excel(excel_file_path)
    
    documentation_df = documentation_df._append(pd.DataFrame({'Value': [layer]}, index=['']))

    modified_excel_file_path = excel_file_path
    documentation_df.to_excel(modified_excel_file_path, index=False)

    return documentation_df