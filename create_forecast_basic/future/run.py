import os
import sys
import pandas as pd

os.getcwd()
# Step 1: Change Directory
df_inputs_outputs = pd.read_excel(r'{}\create_forecast_basic\future\inputs_outputs.xlsx'.format(os.getcwd()))

JTMT_directory = r'{}\JTMT'.format(df_inputs_outputs['location'][0])
os.chdir(JTMT_directory)

arab_and_palestinian_directory = r'{}\arab_and_palestinian'.format(df_inputs_outputs['location'][0])
os.chdir(arab_and_palestinian_directory)

# # Step 2: Import Module
sys.path.append(JTMT_directory)  # Add target directory to sys.path
sys.path.append(arab_and_palestinian_directory)  # Add target directory to sys.path
import run_JTMT_from_future  # Assuming my_function.py is named as my_function_module.py

# # Step 3: Call Function
run_JTMT_from_future.run_notebook(r'{}\JTMT\run_JTMT_from_future.ipynb'.format(df_inputs_outputs['location'][0]))  # Call the function from the imported module