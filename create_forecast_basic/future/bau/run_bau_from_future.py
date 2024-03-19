
import os
import subprocess

path = os.getcwd()
software_folder_location = r'{}\create_forecast_basic\current'.format(path)

def run_notebook(notebook_path):
    try:
        subprocess.check_call(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_path])
        return True  # Execution successful
    except subprocess.CalledProcessError as e:
        print(f"Error executing notebook: {e}")
        return False  # Execution failed

if __name__ == "__main__":
    notebook_path = r'{}\run_bau.ipynb'.format(software_folder_location)
    run_notebook(notebook_path, encoding="utf8")
    execution_result = run_notebook(notebook_path, encoding="utf8")
    print("basic-Notebook execution result:", execution_result)