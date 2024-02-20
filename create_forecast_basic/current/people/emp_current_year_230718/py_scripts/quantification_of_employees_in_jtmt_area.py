def quantification_of_employees_in_jtmt_area(taz):
    pre_woman=0.5

    pre_man=1-pre_woman

    work_age=[ 'pop_25',
    'pop_30',
    'pop_35',
    'pop_40',
    'pop_45',
    'pop_50',
    'pop_55',
    'pop_60']

    under_work_age=[ 'pop_15', 'pop_20']

    over_work_age=[ 'pop_65', 'pop_70', 'pop_75up']

    taz['work_age']=taz[work_age].sum(axis=1)

    taz['under_work_age']=taz[under_work_age].sum(axis=1)

    taz['over_work_age']=taz[over_work_age].sum(axis=1)

    sector='U_Orthodox'

    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['work_age']*pre_woman*0.75+taz['work_age']*pre_man*0.55
    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['pop_emp']+taz['under_work_age']*pre_woman*0.07+taz['under_work_age']*pre_man*0.09
    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['pop_emp']+taz['over_work_age']*pre_woman*0.05+taz['over_work_age']*pre_man*0.09

    sector='Jewish'

    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['work_age']*pre_woman*0.9+taz['work_age']*pre_man*0.92
    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['pop_emp']+taz['under_work_age']*pre_woman*0.20+taz['under_work_age']*pre_man*0.15
    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['pop_emp']+taz['over_work_age']*pre_woman*0.2+taz['over_work_age']*pre_man*0.15

    sector='Arab'

    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['work_age']*pre_woman*0.25+taz['work_age']*pre_man*0.7
    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['pop_emp']+taz['under_work_age']*pre_woman*0.2+taz['under_work_age']*pre_man*0.15
    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['pop_emp']+taz['over_work_age']*pre_woman*0.05+taz['over_work_age']*pre_man*0.09

    sector='arabs_behined_seperation_wall'

    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['work_age']*pre_woman*0.25+taz['work_age']*pre_man*0.7
    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['pop_emp']+taz['under_work_age']*pre_woman*0.2+taz['under_work_age']*pre_man*0.15
    taz.loc[taz['main_secto']==sector,'pop_emp']=taz['pop_emp']+taz['over_work_age']*pre_woman*0.05+taz['over_work_age']*pre_man*0.09


    return taz