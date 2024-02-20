import geopandas as gpd

def higher_education(uni, taz):
    uni=uni.to_crs(crs=2039)

    uni=uni.fillna(0)

    taz['uni_students']=gpd.sjoin(taz[['geometry']].reset_index(),uni)[['Taz_num','num_students']].pivot_table(index='Taz_num',aggfunc=sum)

    taz['emp_from_uni_student']=gpd.sjoin(taz[['geometry']].reset_index(),uni)[['Taz_num','emp_uni']].pivot_table(index='Taz_num',aggfunc=sum)

    taz.loc[taz['main_secto']=="Palestinian",'emp_from_uni_student']=0

    taz=taz.fillna(0)

    return taz