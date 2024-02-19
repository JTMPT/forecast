import pandas as pd

def fix_level_a_arab_jerus(col, stat_arab, cbs_pop_pre):
    col=['STAT', 'group_name']
    stat_arab=stat_arab[col]
    stat_arab=stat_arab.merge(cbs_pop_pre,left_on='STAT',right_on='main_stat',how='left')
    stat_arab=stat_arab.set_index('group_name')
    group_pop=stat_arab.groupby(by='group_name').sum()[['pop']]
    stat_arab['group_pop']=group_pop['pop']
    stat_arab['pre_from_group_pop']=stat_arab['pop']/stat_arab['group_pop']
    data = [['akev', 55000], ['Shuafat', 75000],['east_jeru_left',0]]
    group_pop_jtmt = pd.DataFrame(data, columns=['group_name', 'pop']).set_index('group_name')
    group_pop_delta=group_pop-group_pop_jtmt
    group_pop_delta=group_pop_delta.loc['east_jeru_left']+(group_pop_delta.loc['Shuafat']+group_pop_delta.loc['akev'])*0.8#בגלל שהדלתא מוסבר עי הגירה מיוש ולא רק מהעיר ירושלים
    group_pop_jtmt.loc['east_jeru_left','pop']=group_pop_delta.item()
    stat_arab['group_pop_jtmt']=group_pop_jtmt['pop']
    stat_arab['pop']=stat_arab['pre_from_group_pop']*stat_arab['group_pop_jtmt']
    return stat_arab