def fix_lebel_b(stat):
    stat.loc[(stat['fix_pop']==0)&(stat['fix_aprt']==1)&(stat['fix_class']==1),'pop']=stat['aprt_20']*stat['hh_size']

    stat.loc[(stat['fix_pop']==0)&(stat['fix_aprt']==1)&(stat['fix_class']==1),'change_from_cbs']=stat['change_from_cbs']+'| pop_created_from_cbs_aprt |'

    stat.loc[(stat['fix_pop']==0)&(stat['fix_aprt']==0)&(stat['fix_class']==0),'pop']=0

    stat.loc[(stat['fix_pop']==0)&(stat['fix_aprt']==0)&(stat['fix_class']==0),'change_from_cbs']=stat['change_from_cbs']+'| cbs_pop_deleted |'

    stat['aprt_20_cbs']=stat['aprt_20']

    stat.loc[(stat['fix_pop']==0)&(stat['fix_aprt']==0)&(stat['fix_class']==0),'aprt_20']=0

    stat.loc[(stat['fix_pop']==0)&(stat['fix_aprt']==0)&(stat['fix_class']==0),'change_from_cbs']=stat['change_from_cbs']+'| cbs_aprt_deleted |'

    stat.loc[(stat['fix_pop']==1)&(stat['fix_aprt']==0)&(stat['fix_class']==1),'aprt_20']=stat['pop']/stat['hh_size']

    stat.loc[(stat['fix_pop']==1)&(stat['fix_aprt']==0)&(stat['fix_class']==1),'change_from_cbs']=stat['change_from_cbs']+'| aprt_created_from_pop |'
    
    return stat