import geopandas as gpd

def adding_students_to_the_population_and_age_distribution(student_dorms, taz):
    taz['student_dorms']=gpd.sjoin(taz[['geometry']].reset_index(),student_dorms)[['Taz_num','student_nu']].pivot_table(index='Taz_num',aggfunc=sum)

    taz=taz.fillna(0)

    taz['pop_without_dorms_yeshiva']=taz['pop']

    taz['pop']=taz['pop']+taz['student_dorms']

    taz['pop_20_just_from_aprt']=taz['pop_20']

    taz['pop_25_just_from_aprt']=taz['pop_25']

    taz['pop_20']=taz['pop_20']+taz['student_dorms']*0.6

    taz['pop_25']=taz['pop_25']+taz['student_dorms']*0.4

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