import pandas as pd

def create_100_percent_for_every_AS(bld_point):
    sum_bld_m3=pd.pivot_table(bld_point.drop(columns='centroid'),index=['Taz_num','STAT'],aggfunc=sum)[['bld_m3']].reset_index()

    sum_bld_m3_by_stat=sum_bld_m3.pivot_table(index='STAT',aggfunc=sum)[['bld_m3']].rename(columns={'bld_m3':'bld_m3_stat'}).reset_index()

    sum_bld_m3=sum_bld_m3.merge(sum_bld_m3_by_stat,on='STAT')

    sum_bld_m3['precent_of_stat_data']=sum_bld_m3['bld_m3']/sum_bld_m3['bld_m3_stat']

    sum_bld_m3=sum_bld_m3.loc[(sum_bld_m3['precent_of_stat_data']>0.01)|(sum_bld_m3['Taz_num']==2001)]

    sum_bld_m3_by_stat=sum_bld_m3.pivot_table(index='STAT',aggfunc=sum)[['bld_m3']].rename(columns={'bld_m3':'bld_m3_stat_new'}).reset_index()

    sum_bld_m3=sum_bld_m3.merge(sum_bld_m3_by_stat,on='STAT')

    sum_bld_m3['precent_of_stat_data']=sum_bld_m3['bld_m3']/sum_bld_m3['bld_m3_stat_new']

    return sum_bld_m3