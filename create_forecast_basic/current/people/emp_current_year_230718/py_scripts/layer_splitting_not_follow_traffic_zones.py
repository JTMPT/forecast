import geopandas as gpd
from functions import drop_geo

def layer_splitting_not_follow_traffic_zones(EMP_kibolet, taz, emp_in_jtmt_area_without_mobile):
    EMP_kibolet['emp_area']=EMP_kibolet.area

    EMP_kibolet['ID']=EMP_kibolet.index

    EMP_kibolet_by_taz=gpd.overlay(taz.reset_index()[['Taz_num','taz_area','geometry']],EMP_kibolet)

    EMP_kibolet_by_taz['small_area']=EMP_kibolet_by_taz.area

    EMP_kibolet_by_taz['pre_small_area_emp']=EMP_kibolet_by_taz['small_area']/EMP_kibolet_by_taz['emp_area']

    EMP_kibolet_by_taz['pre_small_area_taz']=EMP_kibolet_by_taz['small_area']/EMP_kibolet_by_taz['taz_area']

    EMP_kibolet_by_taz=EMP_kibolet_by_taz.query('(pre_small_area_taz >0.7) | (pre_small_area_emp >0.1)').drop(columns='geometry_buff')

    EMP_kibolet_by_taz=EMP_kibolet_by_taz.set_index('ID')

    EMP_kibolet_by_taz['id_area_for_pre']=EMP_kibolet_by_taz.reset_index().groupby(by='ID')['small_area'].sum()

    EMP_kibolet_by_taz[['id_area_for_pre']]

    EMP_kibolet_by_taz['prec_from_id']=EMP_kibolet_by_taz['small_area']/EMP_kibolet_by_taz['id_area_for_pre']

    EMP_kibolet_by_taz['emp_without_palestin_in_taz']=EMP_kibolet_by_taz['emp_without_palestin']*EMP_kibolet_by_taz['prec_from_id']

    taz['emp_not_okev']=drop_geo(EMP_kibolet_by_taz).pivot_table(index='Taz_num',aggfunc=sum)[['emp_without_palestin_in_taz']]

    taz=taz.fillna(0)

    taz['total_emp']=taz['emp_not_okev']+taz['emp_okev']+taz['emp_Education']

    taz.query('main_secto!="Palestinian"')['total_emp'].sum()-emp_in_jtmt_area_without_mobile

    return taz