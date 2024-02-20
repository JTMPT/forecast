def adding_yeshiva_students_to_amount_of_population(taz):
    taz['hh']=taz['hh']+taz['yeshiva_dorms_pop_sum']

    taz.loc[taz['main_secto']!="U_Orthodox",'pop']=taz['pop']+taz['yeshiva_dorms_pop_sum']

    taz.loc[taz['main_secto']!="U_Orthodox",'pop_15']=taz['pop_15']+taz['yeshiva_dorms_pop_15']

    taz.loc[taz['main_secto']!="U_Orthodox",'pop_20']=taz['pop_20']+taz['yeshiva_dorms_pop_20']

    taz.loc[taz['main_secto']!="U_Orthodox",'pop_25']=taz['pop_25']+taz['yeshiva_dorms_pop_25']
    return taz