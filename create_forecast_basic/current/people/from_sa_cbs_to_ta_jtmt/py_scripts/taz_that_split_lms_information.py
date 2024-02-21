import pandas as pd

def taz_that_split_lms_information(taz_stat_conver, stat):
    col=['STAT',
    'aprt_20',
    'pop_0',
    'pop_5',
    'pop_10',
    'pop_15',
    'pop_20',
    'pop_25',
    'pop_30',
    'pop_35',
    'pop_40',
    'pop_45',
    'pop_50',
    'pop_55',
    'pop_60',
    'pop_65',
    'pop_70',
    'pop_75up',
    'pop',
    'pop_hardi']

    taz=pd.merge(taz_stat_conver,stat[col],on='STAT',how='left')

    col=['aprt_20',
    'pop_0',
    'pop_5',
    'pop_10',
    'pop_15',
    'pop_20',
    'pop_25',
    'pop_30',
    'pop_35',
    'pop_40',
    'pop_45',
    'pop_50',
    'pop_55',
    'pop_60',
    'pop_65',
    'pop_70',
    'pop_75up',
    'pop',
    'pop_hardi']

    taz[col]=taz[col].multiply(taz['precent_of_stat_data'], axis="index")

    taz=pd.pivot_table(taz,index='Taz_num',aggfunc=sum)

    taz['pre_hardi']=taz['pop_hardi']/taz['pop']

    taz['hh_size']=taz['pop']/taz['aprt_20']

    return taz