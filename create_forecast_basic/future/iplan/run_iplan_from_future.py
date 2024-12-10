import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(notebook_path):
    try:
        # קריאת המחברת עם קידוד UTF-8
        with open(notebook_path, encoding='utf-8') as ff:
            nb_in = nbformat.read(ff, as_version=4)

        # יצירת ExecutePreprocessor
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

        # הרצת המחברת
        nb_out = ep.preprocess(nb_in, {'metadata': {'path': './'}})

        print(f"Notebook '{notebook_path}' executed successfully.")
        return nb_out
    except Exception as e:
        print(f"Error running notebook: {e}")
        return None


path = os.getcwd()
software_folder_location = r'{}\create_forecast_basic\future'.format(path)
notebook_path = r'{}\iplan\run_iplan_from_future.ipynb'.format(software_folder_location)
