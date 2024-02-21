def create_information_at_taz(stat, precent_of_stat_data):
    col=['pop_0',
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
    'pop_75up']

    stat[col]=stat[col].multiply(stat['pop'], axis="index")

    stat['pop_hardi']=stat['pop']*(stat['pre_hardi']/100)

    taz_stat_conver=precent_of_stat_data

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

    return taz_stat_conver