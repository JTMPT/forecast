import pandas as pd

def create_client_documentation_df(client_data_folder_location, forecast_version_num):
    # Define the data
    data = {
        'Value': [forecast_version_num, 'כן', 'Nan']
    }

    # Create the DataFrame
    df = pd.DataFrame(data, index=['גירסא', 'איזורי תנועה חדשים', 'שכבות'])

    # Append empty rows with values 2, 3, and 4
    df = df._append(pd.DataFrame({'Value': [2, 3, 4]}, index=['', '', '']))

    print(df)
    return df

create_client_documentation_df(r'C:\Users\dpere\Documents\JTMT\Projects\תחזיות_דמוגרפיות\קבצי עבודה\142_מתחם_אנגל\בהת', 1)