def creating_apartments_according_to_household_size(stat):
    stat.loc[((stat['aprt_20'].isna())|(stat['aprt_20']==0))&(stat['pop']>0),'change_from_cbs']=stat['change_from_cbs']+'| aprt_created_from_pop_because_no_cbs_data |'

    stat.loc[((stat['aprt_20'].isna())|(stat['aprt_20']==0))&(stat['pop']>0),'aprt_20']=round(stat['pop']/stat['hh_size'])

    return stat