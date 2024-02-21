import pandas as pd
import numpy as np

def category_for_age_distribution(sectors, data_df, prototypes_df):
    data_df=sectors.merge(data_df,left_on='Taz_num',right_on='TAZ',how='right')

    data_df['sector_for_age']=data_df['sector']

    data_df.loc[
    (data_df['zonetype'] == 'Judea and Samaria') &
    (data_df['sector'] != 'U_Orthodox'),'sector_for_age'
    ]='hitnachlut'

    lst_muni=['מעלה אדומים',
    'גבעת זאב',
    'הר אדר',
    '0',
    'מעלה אפרים',
    'מגילות ים המלח\r\n',
    'קרני שומרון',
    'אלפי מנשה',
    'בית אריה-עופרים',
    'ערבות הירדן\r\n',
    'אריאל']

    data_df.loc[data_df['Muni_Heb'].isin(lst_muni),'sector_for_age'
    ]='Jewish'

    data_df.loc[
    (data_df['sector'] == 'arabs_behined_seperation_wall') |
    (data_df['sector'] == 'Arab'),'sector_for_age'
    ]='Arab'

    data_df=data_df.loc[
    (data_df['sector'] != 'Palestinian')
    ]

    col=[ 'age0_4',
    'age5_9',
    'age10_14',
    'age15_19',
    'age20_24',
    'age25_29',
    'age30_34',
    'age35_39',
    'age40_44',
    'age45_49',
    'age50_54',
    'age55_59',
    'age60_64',
    'age65_69',
    'age70_74',
    'age75up']

    # Convert counts to percentages
    data_df_pre = data_df[col].apply(lambda x: x / x.sum(), axis=1)

    data_df=data_df.join(data_df_pre,lsuffix='', rsuffix='_prec')

    col_name_prototype=['pop_0','pop_5',
    'pop_10',
    'pop_15',
    'pop_20',
    'pop_25',
    'pop_30',
    'pop_35',
    'pop_40',
    'pop_45',
    'pop_50',
    'pop_55',
    'pop_60',
    'pop_65',
    'pop_70',
    'pop_75up']

    col_name_row=['age0_4_prec',
    'age5_9_prec',
    'age10_14_prec',
    'age15_19_prec',
    'age20_24_prec',
    'age25_29_prec',
    'age30_34_prec',
    'age35_39_prec',
    'age40_44_prec',
    'age45_49_prec',
    'age50_54_prec',
    'age55_59_prec',
    'age60_64_prec',
    'age65_69_prec',
    'age70_74_prec',
    'age75up_prec']

    ls_sector=['U_Orthodox', 'Jewish', 'hitnachlut', 'Arab']

    for s in ls_sector:
        locals()['data_df_{}'.format(s)]=data_df.loc[data_df['sector_for_age']=='{}'.format(s)]
        locals()['prototypes_df_{}'.format(s)]=prototypes_df.loc[prototypes_df['sector']=='{}'.format(s)]

    for s in ls_sector:
        for index, row in locals()['data_df_{}'.format(s)].iterrows():
            # Step 3: Calculate similarity scores
            similarity_scores = []
            for _, prototype_row in locals()['prototypes_df_{}'.format(s)].iterrows():
                prototype_age_distributions = prototype_row[col_name_prototype].values 
                data_age_distributions = row[col_name_row].values         
                similarity_score = np.linalg.norm(prototype_age_distributions - data_age_distributions)
                similarity_scores.append(similarity_score)

            # Step 4: Determine closest prototype
            closest_index = np.argmin(similarity_scores)
            closest_prototype = locals()['prototypes_df_{}'.format(s)].iloc[closest_index]['classification_name']
            

            # Assign closest_prototype to the corresponding row in data_df or perform any desired action
            locals()['data_df_{}'.format(s)].at[index,'classification_name'] = closest_prototype
    data_df=pd.concat([locals()['data_df_U_Orthodox'],locals()['data_df_Jewish'],locals()['data_df_hitnachlut'],locals()['data_df_Arab']],axis=0)
        
    return data_df