import pandas as pd

def successive_coefficient(taz, emp_okev, software_data_folder_location):
    city_muni=['מודיעין עילית','בית שמש','ירושלים','מודיעין - מכבים - רעות']

    okev_level=0.15

    arab_city=taz.query('jew==0 & okev==1')['aprt_20'].sum().item()

    arab_sub=0

    ou_sub=taz.query('main_secto=="U_Orthodox" & ~Muni_Heb.isin(@city_muni) & okev==1')['aprt_20'].sum().item()

    ou_city=taz.query('main_secto=="U_Orthodox" & Muni_Heb.isin(@city_muni) & okev==1')['aprt_20'].sum().item()

    general_city=taz.query('main_secto=="Jewish" & Muni_Heb.isin(@city_muni) & okev==1')['aprt_20'].sum().item()

    general_sub=taz.query('main_secto=="Jewish" & ~Muni_Heb.isin(@city_muni) & okev==1')['aprt_20'].sum().item()

    base_okev_factor=(emp_okev-(okev_level*general_city-okev_level*(ou_sub+arab_city)-2*okev_level*arab_sub))/(general_sub+general_city+ou_city+ou_sub+arab_city+arab_sub)

    base_okev_factor=round(base_okev_factor,3)

    data = [['Jewish', base_okev_factor,base_okev_factor+okev_level],['arab', base_okev_factor-okev_level,base_okev_factor], ['U_Orthodox',base_okev_factor-2*okev_level,base_okev_factor-okev_level]]
 
    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['sector', 'sub','city'])
    okev_factor=df.set_index('sector')
    okev_factor.to_excel(r'{}\Intermediates\okev_factor.xlsx'.format(software_data_folder_location))

    taz['emp_okev']=0

    taz.loc[(taz['jew']==0)&(taz['okev']==1),'emp_okev']=taz['aprt_20']*okev_factor.loc['arab','city']

    taz.loc[(taz['main_secto']=="U_Orthodox")&(~taz['Muni_Heb'].isin(city_muni))&(taz['okev']==1),'emp_okev']=taz['aprt_20']*okev_factor.loc['U_Orthodox','sub']

    taz.loc[(taz['main_secto']=="U_Orthodox")&(taz['Muni_Heb'].isin(city_muni))&(taz['okev']==1),'emp_okev']=taz['aprt_20']*okev_factor.loc['U_Orthodox','city']

    taz.loc[(taz['main_secto']=="Jewish")&(taz['Muni_Heb'].isin(city_muni))&(taz['okev']==1),'emp_okev']=taz['aprt_20']*okev_factor.loc['Jewish','city']

    taz.loc[(taz['main_secto']=="Jewish")&(~taz['Muni_Heb'].isin(city_muni))&(taz['okev']==1),'emp_okev']=taz['aprt_20']*okev_factor.loc['Jewish','sub']

    taz.emp_okev.sum().item()-emp_okev

    return taz