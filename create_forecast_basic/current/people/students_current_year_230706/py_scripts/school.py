import pandas as pd
import geopandas as gpd
from functions import drop_geo, up_load_df

def school(taz, student_gov, muni_JTMT, directory_path):
    taz_student=gpd.sjoin(taz.reset_index(),student_gov)

    taz['student_gov']=taz_student[['Taz_num','num_of_students']].pivot_table(index='Taz_num',aggfunc=sum)[['num_of_students']]

    col=['CR_PNIM','Muni_Heb']

    muni_JTMT=muni_JTMT[col]

    muni_JTMT['CR_PNIM']=muni_JTMT['CR_PNIM'].astype(int)

   # # Load each DataFrame separately
    df1 = up_load_df(directory_path, 'cbs_student_2020_by_muni_3')
    df2 = up_load_df(directory_path, 'cbs_student_2020_by_muni_1')
    df3 = up_load_df(directory_path, 'cbs_student_2020_by_muni_2')

    # # Concatenate the DataFrames
    student_gov_by_muni = pd.concat([df1, df2, df3])

    col=[ 'סמל_יישוב','ילדים_בגנים_של_משרד_החינוך_גיל_3_תש_ף_2019_20',
    'ילדים_בגנים_של_משרד_החינוך_גיל_4_תש_ף_2019_20',
    'ילדים_בגנים_של_משרד_החינוך_גיל_5_תש_ף_2019_20',
    'ילדים_בגנים_של_משרד_החינוך_גיל_6_תש_ף_2019_20',
    'תלמידים_בבתי_ספר_יסודיים_תש_ף_2019_20',
    'תלמידים_בבתי_ספר_עליסודיים_תש_ף_2019_20',
    'תלמידים_בחטיבות_ביניים_תש_ף_2019_20',
    'תלמידים_בבתי_ספר_תיכוניים_תש_ף_2019_20']

    student_gov_by_muni=student_gov_by_muni[col]

    student_gov_by_muni=student_gov_by_muni.merge(muni_JTMT,left_on='סמל_יישוב',right_on='CR_PNIM')

    student_gov_by_muni=student_gov_by_muni.drop_duplicates(subset='CR_PNIM',keep='first')

    col=[ 'ילדים_בגנים_של_משרד_החינוך_גיל_3_תש_ף_2019_20',
    'ילדים_בגנים_של_משרד_החינוך_גיל_4_תש_ף_2019_20',
    'ילדים_בגנים_של_משרד_החינוך_גיל_5_תש_ף_2019_20',
    'ילדים_בגנים_של_משרד_החינוך_גיל_6_תש_ף_2019_20',
    'תלמידים_בבתי_ספר_יסודיים_תש_ף_2019_20',
    'תלמידים_בחטיבות_ביניים_תש_ף_2019_20',
    'תלמידים_בבתי_ספר_תיכוניים_תש_ף_2019_20']

    student_gov_by_muni['student_gov']=student_gov_by_muni[col].sum(axis=1)

    col=[ 'CR_PNIM','Muni_Heb','student_gov']
    student_gov_by_muni=student_gov_by_muni[col].set_index('CR_PNIM').fillna(0)

    taz['CR_PNIM']=taz['CR_PNIM'].astype(int)

    jtmt_muni_student_gov=drop_geo(taz).pivot_table(index='CR_PNIM',aggfunc=sum)[['student_gov']].fillna(0)

    delta=jtmt_muni_student_gov.merge(student_gov_by_muni,left_index=True,right_index=True,suffixes=('_JTMT','_MUNI'),how='outer').fillna(0)

    delta['delta_student']=delta[['student_gov_JTMT','student_gov_MUNI']].max(axis=1)-delta['student_gov_JTMT']

    col=['CR_PNIM','delta_student']

    taz=taz.reset_index().merge(delta.reset_index()[col],on='CR_PNIM',how='left')

    taz['student_demand']=taz['pop_0']/5*2+taz['pop_5']+taz['pop_10']+taz['pop_15']/5*3

    taz['student_demand_left']=taz['student_demand']-taz['student_gov']
    taz.loc[taz['student_demand_left']<0,'student_demand_left']=0

    taz=taz.set_index('CR_PNIM')

    taz['student_demand_left_sum_by_muni']=drop_geo(taz).groupby(by='CR_PNIM').sum()[['student_demand_left']]

    taz['student_demand_left_pre']=taz['student_demand_left']/taz['student_demand_left_sum_by_muni']

    taz['cbs_muni_student_left_by_pre_of_demand_left']=taz['student_demand_left_pre']*taz['delta_student']
    
    return taz