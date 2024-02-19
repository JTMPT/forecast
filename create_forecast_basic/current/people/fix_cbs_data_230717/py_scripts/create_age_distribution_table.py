import pandas as pd

def create_age_distribution_table(cbs_pop_pre, cbs_pop, stat):    
    col=list(cbs_pop_pre.iloc[:,1:])

    cbs_pop_pre.loc[:, col] = cbs_pop_pre.loc[:, col].div(cbs_pop_pre['pop'], axis=0)

    cbs_pop_pre=cbs_pop_pre.fillna(0)

    cbs_pop_pre=cbs_pop_pre.rename(columns={'pop':'pop_pre'})

    cbs_pop_pre=cbs_pop_pre.merge(cbs_pop[['main_stat', 'pop']],on='main_stat',how='left')

    stat=pd.merge(stat,cbs_pop_pre,on='main_stat',how='left')

    stat['pop']=stat['pop']*stat['precent_of_stat_data']

    return stat