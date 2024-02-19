def assimilation_fix_level_a(stat_arab, stat):
    stat_arab=stat_arab.set_index('main_stat')
    stat['pop_cbs']=stat['pop']
    stat.loc[list(stat_arab.index),'pop']=stat_arab['pop']
    stat['change_from_cbs']=''
    stat.loc[list(stat_arab.index),'change_from_cbs']='| general_arab_change |'
    return stat