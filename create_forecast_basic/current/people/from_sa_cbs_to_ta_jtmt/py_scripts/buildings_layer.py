from functions import make_point

def buildings_layer(bld, bld_poi):
    bld=bld.merge(bld_poi[[ 'FCODE', 'USG_GROUP', 'USG_CODE','USG_SP_NM_LTN','BLDG_ID']],how='left',left_on='UNIQ_ID',right_on='BLDG_ID')

    bld=bld.loc[(bld['FCODE_y'].isna())|(bld['USG_CODE']==7600)] #זה קוד לבניינים מעורב שימושים אני מניח שעדיף לשים בניינים מיותרים מאשר הפוך

    bld['bld_area']=bld.area

    bld_point=make_point(bld).fillna(0)

    bld_point.loc[bld_point['HEIGHT']<=0,'HEIGHT']=bld_point['HI_PNT_Z']-bld_point['HT_LAND']

    ceiling_height=3

    bld_point['bld_m3']=(bld_point['HEIGHT']/ceiling_height).astype(int)*bld_point['bld_area'].astype(int)

    bld_point.loc[(bld_point['HEIGHT']-ceiling_height)<=0,'bld_m3']=bld_point['bld_area']
    
    return bld_point