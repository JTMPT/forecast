import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(notebook_path):
    with open(notebook_path) as ff:
        nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
        
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    nb_out = ep.preprocess(nb_in)

path = os.getcwd()
software_folder_location = r'{}\create_forecast_basic\future'.format(path)
notebook_path = r'{}\bau\run_bau_from_future.ipynb'.format(software_folder_location)
