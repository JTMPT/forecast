import pandas as pd


def statistical_areas_layer(stat, stat_aprt, stat_join_from_main_to_secondary):
    col_name=['STAT','geometry']
    stat=stat[col_name]

    stat=pd.merge(stat,stat_aprt,on='STAT',how='left').merge(stat_join_from_main_to_secondary,left_on='STAT',right_on='secondary_stat',how='left')

    stat.loc[stat['precent_of_stat_data'].isna(),'main_stat']=stat['STAT']

    stat.loc[stat['precent_of_stat_data'].isna(),'secondary_stat']=stat['STAT']

    stat.loc[stat['precent_of_stat_data'].isna(),'precent_of_stat_data']=1
    
    return stat