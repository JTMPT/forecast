def logical_controls(taz):
    taz.loc[taz['TAZ']<=0]

    taz.yosh.unique()

    taz.in_jerusalem_metropolin.unique()

    taz.jerusalem_city.unique()

    taz.sector.unique()

    col=['hh_total',
    'pop',
    'age0_4',
    'age5_9',
    'age10_14',
    'age15_19',
    'age20_24',
    'age25_29',
    'age30_34',
    'age35_39',
    'age40_44',
    'age45_49',
    'age50_54',
    'age55_59',
    'age60_64',
    'age65_69',
    'age70_74',
    'age75up',
    'emp_tot',
    'indus',
    'com_hotel',
    'business',
    'public',
    'education',
    'agri',
    'student',
    'univ',
    'UO_Hi_Ed',
    'pop_emp_employed']

    taz_to_check=[]
    
    for i in col:
        taz_to_check=taz_to_check+list(taz.loc[taz['{}'.format(i)]<0]['TAZ'])

    taz.loc[~(taz['hh_total']<=taz['pop'])]

    taz.loc[taz['sector']!="Palestinian"].loc[taz['hh_total']>0].loc[taz['pop']<=0]

    col=['age0_4',
    'age5_9',
    'age10_14',
    'age15_19',
    'age20_24',
    'age25_29',
    'age30_34',
    'age35_39',
    'age40_44',
    'age45_49',
    'age50_54',
    'age55_59',
    'age60_64',
    'age65_69',
    'age70_74',
    'age75up',]

    taz['pop_check']=round(taz[col].sum(axis=1)-taz['pop'])

    taz.loc[taz['sector']!="Palestinian"].loc[taz['pop_check']!=0].query('TAZ==511')#.to_excel('delet.xlsx')#[col].sum(axis=1)

    len(taz.loc[taz['sector']!="Palestinian"].loc[taz['pop_check']!=0])

    taz.loc[taz['sector']!="Palestinian"].loc[taz['pop']>0].loc[taz['hh_total']<=0]

    col=[
    'age0_4',
    'age5_9',
    'age10_14',
    'age15_19',
    'age20_24',
    'age25_29',
    'age30_34',
    'age35_39',
    'age40_44',
    'age45_49',
    'age50_54',
    'age55_59',
    'age60_64',
    'age65_69',
    'age70_74',
    'age75up']

    taz_to_check=[]
   
    for i in col:
        taz_to_check=taz_to_check+list(taz.loc[taz['{}'.format(i)]>0].loc[taz['pop']<=0]['TAZ'])
        taz_to_check=taz_to_check+list(taz.loc[taz['{}'.format(i)]>0].loc[taz['hh_total']<=0]['TAZ'])

    col=['indus',
    'com_hotel',
    'business',
    'public',
    'education',
    'agri']

    taz['emp_check']=round(taz[col].sum(axis=1)-taz['emp_tot'])

    taz.loc[taz['sector']!="Palestinian"].loc[taz['emp_check']!=0]

    taz_to_check=[]

    for i in col:
        taz_to_check=taz_to_check+list(taz.loc[taz['{}'.format(i)]>0].loc[taz['emp_tot']<=0]['TAZ'])
    
    taz.loc[taz['sector']!="Palestinian"].loc[taz['pop_emp_employed']>0].loc[taz['pop']<=0]

    return taz