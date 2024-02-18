import os
import subprocess

def create_documentation_file(software_data_folder_location):
    current_directory= os.getcwd()

    tag = subprocess.check_output(["git", "describe", "--tag"]).strip().decode()
    tag_link = 'https://github.com/JTMPT/forecast/releases/tag/{}'.format(tag)

    FOLDER_PATH = r'{}\background_files'.format(current_directory)
    # FOLDER_PATH = r'{}\background_files'.format(software_data_folder_location)
    print(FOLDER_PATH)
    # fileNames = os.listdir(FOLDER_PATH)

    # for fileName in fileNames:
    #     print(fileName)