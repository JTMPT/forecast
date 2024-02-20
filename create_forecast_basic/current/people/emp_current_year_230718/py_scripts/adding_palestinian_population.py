def adding_palestinian_population(taz, taz_demo_pls_2020):
    col=['pop',
    'pop_0',
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
    'pop_75up',
    'student',
    'uni_students',
    'student_yeshiva_and_kollim',
    'emp_Education',
    'pop_emp_employed',
    'total_emp',
    'agri',
    'Indus',
    'Com_hotel',
    'Business',
    'Public',
    'hh']

    taz.loc[taz['main_secto']=='Palestinian',col]=0

    taz.loc[taz['main_secto']=='Palestinian','pop']=taz['pop']+taz_demo_pls_2020['pop_2020']

    return taz