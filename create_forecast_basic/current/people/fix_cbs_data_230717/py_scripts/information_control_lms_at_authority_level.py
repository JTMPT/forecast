import os
import sys
import pandas as pd

path = os.getcwd()
parent = os.path.dirname(path)
software_data_folder_location = os.path.dirname(parent)
sys.path.append(software_data_folder_location)

from functions import drop_geo

def information_control_lms_at_authority_level(stat, pop_2020_cbs_muni):
    stat['CR_PNIM']=stat['CR_PNIM'].fillna(0).astype(int)

    stat_by_muni_sum=drop_geo(stat).pivot_table(index='CR_PNIM',aggfunc=sum)[['pop_cbs','pop']]

    pop_2020_cbs_muni=pop_2020_cbs_muni.set_index('CR_PNIM')

    pop_2020_cbs_muni.join(stat_by_muni_sum,how='inner')

    return stat