import geopandas as gpd

def remove_irrelevant_buildings(bld_point, taz, taz_not_relevant, stat):
    bld_point=gpd.sjoin(bld_point,taz.loc[(~taz['Taz_num'].isin(taz_not_relevant))&(taz['Palestinia']==0)])

    col=['bld_m3','centroid','Taz_num']

    bld_point=bld_point[col]

    bld_point=gpd.sjoin(bld_point,stat[['STAT','geometry']])

    bld_point['bld_m3']=bld_point['bld_m3'].astype(int)

    return bld_point