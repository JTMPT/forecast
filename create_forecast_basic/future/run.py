import os
import sys
import pandas as pd

# Step 1: Change Directorys
df_inputs_outputs = pd.read_excel(r'{}\create_forecast_basic\future\inputs_outputs.xlsx'.format(os.getcwd()))

JTMT_directory = r'{}\JTMT'.format(df_inputs_outputs['location'][0])
os.chdir(JTMT_directory)

arab_and_palestinian_directory = r'{}\arab_and_palestinian'.format(df_inputs_outputs['location'][0])
os.chdir(arab_and_palestinian_directory)

bau_directory = r'{}\bau'.format(df_inputs_outputs['location'][0])
os.chdir(bau_directory)

iplan_directory = r'{}\iplan'.format(df_inputs_outputs['location'][0])
os.chdir(iplan_directory)

# # Step 2: Import Modules
sys.path.append(JTMT_directory)
sys.path.append(arab_and_palestinian_directory)
sys.path.append(bau_directory)
sys.path.append(iplan_directory)

import run_arab_and_palestinian_from_future
import run_JTMT_from_future
import run_iplan_from_future
import run_bau_from_future

# # Step 3: Call Function
run_arab_and_palestinian_from_future.run_notebook(r'{}\arab_and_palestinian\run_arab_and_palestinian.ipynb'.format(df_inputs_outputs['location'][0]))  # Call the function from the imported module
run_JTMT_from_future.run_notebook(r'{}\JTMT\run_jtmt.ipynb'.format(df_inputs_outputs['location'][0]))  # Call the function from the imported module
run_iplan_from_future.run_notebook(r'{}\iplan\run_iplan.ipynb'.format(df_inputs_outputs['location'][0]))  # Call the function from the imported module
run_bau_from_future.run_notebook(r'{}\bau\run_bau.ipynb'.format(df_inputs_outputs['location'][0]))  # Call the function from the imported module