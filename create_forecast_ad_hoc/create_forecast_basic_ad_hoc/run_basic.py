import os
import subprocess

path = os.getcwd()
software_folder_location = r'{}\create_forecast_basic_ad_hoc'.format(path)

def run_notebook(notebook_path):
    try:
        subprocess.check_call(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_path])
        return True
    except subprocess.CalledProcessError as e:
        print(f"שגיאה בהרצת המחברת: {e}")
        print(f"פלט הפקודה: {e.output}")
        return False

if __name__ == "__main__":
    notebook_path = r'{}\run_basic.ipynb'.format(software_folder_location)
    run_notebook(notebook_path, encoding="utf8")
    execution_result = run_notebook(notebook_path, encoding="utf8")
    print("basic-Notebook execution result:", execution_result)