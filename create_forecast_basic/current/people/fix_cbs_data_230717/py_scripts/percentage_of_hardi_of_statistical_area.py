def percentage_of_hardi_of_statistical_area(stat_hardi, stat):
    stat_hardi=stat_hardi[['pre_hardi','main_stat']].set_index('main_stat')
    stat=stat.set_index('main_stat')
    stat['pre_hardi']=stat_hardi['pre_hardi']
    stat['pre_hardi']=stat['pre_hardi'].fillna(0)
    return stat