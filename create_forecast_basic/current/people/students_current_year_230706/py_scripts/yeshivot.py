def yeshivot(taz, student_yeshiva):
    taz['old_student_yeshiva']=0

    taz=taz.fillna(0)

    taz=taz.join(student_yeshiva).fillna(0)

    taz['add_from_old_student_yeshiva']=taz['old_student_yeshiva']-taz['student_yeshiva']

    taz.loc[taz['add_from_old_student_yeshiva']<0,'add_from_old_student_yeshiva']=0

    taz['kollim_demand']=(taz['pop_20']*0.8+taz['pop_25']*0.65+taz['pop_30']*0.30+taz['pop_35']*0.30+taz['pop_40']*0.30+taz['pop_45']*0.20+taz['pop_50']*0.20+taz['pop_55']*0.20+taz['pop_60']*0.20)*0.5 #הכפלה בחצי בשביל לקבל אוכלוסיית גברים מעורכת

    taz.loc[taz['main_secto']!='U_Orthodox','kollim_demand']=0  #אל אף שאנחנו יודעים שיש כוללים באזורים שהם לא מוגדרים כחרדים

    taz['add_from_kollim_demand']=0

    taz['student_yeshiva_with_add_from_old']=taz['add_from_old_student_yeshiva']+taz['student_yeshiva']

    taz.loc[(taz['main_secto']=='U_Orthodox')&(taz['kollim_demand']>taz['student_yeshiva_with_add_from_old']),'add_from_kollim_demand']=taz['kollim_demand']-taz['student_yeshiva_with_add_from_old']

    taz['student_yeshiva_and_kollim']=taz['add_from_kollim_demand']+taz['student_yeshiva_with_add_from_old']

    return taz