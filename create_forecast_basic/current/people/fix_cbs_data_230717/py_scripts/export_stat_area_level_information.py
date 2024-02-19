def export_stat_area_level_information(stat):
    stat=stat.fillna(0)

    stat['pop_delta']=stat['pop']-stat['pop_cbs']

    stat['aprt_20_delta']=stat['aprt_20']-stat['aprt_20_cbs']

    return stat