def authority_level_information(stat, stat_point, muni_under_JTMT_ITM):
    stat=stat.set_index('STAT')
    
    stat['CR_PNIM']=stat_point.sjoin(muni_under_JTMT_ITM)[['STAT','CR_PNIM']].set_index('STAT')
   
    stat=stat.reset_index()
    return stat