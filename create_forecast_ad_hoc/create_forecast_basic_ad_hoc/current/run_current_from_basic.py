# import os
# import nbformat
# from nbconvert.preprocessors import ExecutePreprocessor

# def run_notebook(notebook_path):
#     try:
#         # קריאת המחברת עם קידוד UTF-8
#         with open(notebook_path, encoding='utf-8') as ff:
#             nb_in = nbformat.read(ff, as_version=4)

#         # יצירת ExecutePreprocessor
#         ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

#         # הרצת המחברת
#         nb_out = ep.preprocess(nb_in, {'metadata': {'path': './'}})

#         print(f"Notebook '{notebook_path}' executed successfully.")
#         return nb_out
#     except Exception as e:
#         print(f"Error running notebook: {e}")
#         return None

# path = os.getcwd()
# software_folder_location = r'{}\create_forecast_basic\current'.format(path)
# notebook_path = r'{}\run_current.ipynb'.format(software_folder_location)


import os
import subprocess

path = os.getcwd()
software_folder_location = r'{}\current'.format(path)

def run_notebook(notebook_path):
    try:
        subprocess.check_call(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_path, '--allow-errors'])
        return True
    except subprocess.CalledProcessError as e:
        print(f"שגיאה בהרצת המחברת: {e}")
        print(f"פלט הפקודה: {e.output}")
        return False

if __name__ == "__main__":
    notebook_path = r'{}\run_current.ipynb'.format(software_folder_location)
    run_notebook(notebook_path, encoding="utf8")
    execution_result = run_notebook(notebook_path, encoding="utf8")
    print("basic-Notebook execution result:", execution_result)