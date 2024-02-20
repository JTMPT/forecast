import geopandas as gpd
from functions import make_point

def distribution_of_employment_branches(emp_category_type, taz):
    col=['agri', 'Indus', 'Com_hotel', 'Business', 'Public']

    emp_category_type[col]=emp_category_type[col]/100

    emp_category_type=gpd.sjoin(make_point(taz.reset_index())[['Taz_num','centroid']],emp_category_type).set_index('Taz_num')

    col=['agri', 'Indus', 'Com_hotel', 'Business', 'Public']

    taz.join(emp_category_type[col]).query('(emp_not_okev>0 | emp_okev>0 )& agri.isna() & main_secto!="Palestinian" ')

    taz=taz.join(emp_category_type[col]).fillna(0)

    for i in col:
        taz['{}'.format(i)]=taz['{}'.format(i)]*(taz['emp_not_okev']+taz['emp_okev'])
    
    taz['check_emp_sum']=taz[col].sum(axis=1)-(taz['emp_not_okev']+taz['emp_okev'])

    taz.query('check_emp_sum>10 |check_emp_sum<-10')

    return taz