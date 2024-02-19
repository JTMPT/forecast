from py_scripts.functions import drop_geo

def create_GM_according_to_catalog(stat, hh_size):
    cbs_not_lie_lst=list(stat.query('fix_pop.isna() & fix_aprt.isna() & fix_class.isna() ').index)

    stat['count']=1

    stat=stat.reset_index()

    stat.loc[stat['STAT'].isin(cbs_not_lie_lst),['fix_pop','fix_aprt','fix_class']]=1

    hh_size_by_classification=drop_geo(stat).loc[(stat['aprt_20']>0)&(stat['STAT'].isin(cbs_not_lie_lst))].pivot_table(index='classification_name',aggfunc=sum)[['aprt_20','pop','count']]

    hh_size_by_classification['hh_size']=hh_size_by_classification['pop']/hh_size_by_classification['aprt_20']

    hh_size_by_classification=hh_size_by_classification[['hh_size','count']]

    hh_size=hh_size.merge(hh_size_by_classification.reset_index(),how='left',on='classification_name',suffixes=('','_cbs'))

    return stat