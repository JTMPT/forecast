def unemployment_calculation(taz):
    taz['pop_emp_employed']=0

    taz.loc[taz['main_secto']=="U_Orthodox",'pop_emp_employed']=taz['pop_emp']*0.97

    taz.loc[taz['main_secto']=="Jewish",'pop_emp_employed']=taz['pop_emp']*0.98

    taz.loc[taz['jew']==0,'pop_emp_employed']=taz['pop_emp']*0.95

    return taz