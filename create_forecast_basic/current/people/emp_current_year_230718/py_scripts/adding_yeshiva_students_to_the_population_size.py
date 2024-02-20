def adding_yeshiva_students_to_the_population_size(taz):
    taz['pop_15_just_from_aprt']=taz['pop_15']
    
    taz.loc[taz['main_secto']=="U_Orthodox",'pop']=taz['pop']+taz['yeshiva_dorms_pop_sum']

    taz.loc[taz['main_secto']=="U_Orthodox",'pop_15']=taz['pop_15']+taz['yeshiva_dorms_pop_15']

    taz.loc[taz['main_secto']=="U_Orthodox",'pop_20']=taz['pop_20']+taz['yeshiva_dorms_pop_20']

    taz.loc[taz['main_secto']=="U_Orthodox",'pop_25']=taz['pop_25']+taz['yeshiva_dorms_pop_25']

    col=['pop_0',
    'pop_10',
    'pop_15',
    'pop_20',
    'pop_25',
    'pop_30',
    'pop_35',
    'pop_40',
    'pop_45',
    'pop_5',
    'pop_50',
    'pop_55',
    'pop_60',
    'pop_65',
    'pop_70',
    'pop_75up',]

    taz['pop_check']=round(taz[col].sum(axis=1)-taz['pop'])

    taz.loc[taz['main_secto']!="Palestinian"].loc[taz['pop_check']!=0]
    return taz