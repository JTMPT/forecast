from functions import drop_geo

def students_in_jerus_by_sector(taz):
    taz['jew']=0
    taz.loc[(taz['main_secto']=="Jewish") |( taz['main_secto']=="U_Orthodox"),'jew']=1

    drop_geo(taz).query('Muni_Heb=="ירושלים"').groupby(by='jew').sum()[['student_gov','cbs_muni_student_left_by_pre_of_demand_left']]

    jeru_muni_arab_sum_demand=drop_geo(taz).groupby(by=['CR_PNIM','jew']).sum()[['student_demand']].loc[[3000][0],0].item()

    taz=taz.reset_index()

    taz.loc[(taz['jew']==0)&( taz['Muni_Heb']=="ירושלים"),'student_demand_pre']=taz['student_demand']/jeru_muni_arab_sum_demand

    taz.loc[(taz['jew']==0) &( taz['Muni_Heb']=="ירושלים")]['student_demand_pre'].sum()

    taz.loc[(taz['jew']==0) &( taz['Muni_Heb']=="ירושלים"),'cbs_muni_student_left_by_pre_of_demand']=taz['student_demand_pre']*(97600-drop_geo(taz).query('Muni_Heb=="ירושלים"').groupby(by='jew').sum()['student_gov'].loc[0])

    taz.loc[ taz['Muni_Heb']=="ירושלים",'cbs_muni_student_left_by_pre_of_demand_left']=0 # בגלל שנתוני מכון ירושלים משמע שבשכת נק' מצאנו יותר תלמידים מאשר המספר הרשמי

    drop_geo(taz).query('Muni_Heb=="ירושלים"').groupby(by='jew').sum()[['student_gov','cbs_muni_student_left_by_pre_of_demand_left','cbs_muni_student_left_by_pre_of_demand']]

    col=['student_gov','cbs_muni_student_left_by_pre_of_demand_left','cbs_muni_student_left_by_pre_of_demand','student_toddlers']

    taz['student_for_Control']=taz[col].sum(axis=1)

    drop_geo(taz).query('Muni_Heb=="ירושלים"').groupby(by='jew').sum()[['student_for_Control']]

    return taz