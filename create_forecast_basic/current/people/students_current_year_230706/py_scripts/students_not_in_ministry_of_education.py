from functions import drop_geo
import geopandas as gpd

def students_not_in_ministry_of_education(taz, student_chardi_not_gov, student_arab_not_gov):
    taz=taz.set_index('Taz_num')

    taz['student_chardi_not_gov']=drop_geo(gpd.sjoin(taz.reset_index(),student_chardi_not_gov)).pivot_table(index='Taz_num',aggfunc=sum)[['num_students']]

    student_arab_not_gov=student_arab_not_gov.pivot_table(index='Taz_num',aggfunc=sum)[['num_student']]

    taz['student_arab_not_gov']=student_arab_not_gov[['num_student']]

    return taz