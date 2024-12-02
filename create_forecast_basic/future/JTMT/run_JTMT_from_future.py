
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

path = os.getcwd()
software_folder_location = r'{}\create_forecast_basic\current'.format(path)

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


if __name__ == "__main__":
    notebook_path = r'{}\run_JTMT_from_future.ipynb'.format(software_folder_location)
    run_notebook(notebook_path, encoding="utf8")
    execution_result = run_notebook(notebook_path, encoding="utf8")
    print("basic-Notebook execution result:", execution_result)