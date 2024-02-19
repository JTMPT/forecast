import pandas as pd

def upload_population_information(stat, classification):
    col_name=['main_stat','classification_name']
    classification=classification[col_name]
    classification=classification.drop_duplicates(subset='main_stat',keep='first')
    stat=pd.merge(stat,classification,on='main_stat',how='left')

    return stat