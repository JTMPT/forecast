from functions import make_point
import geopandas as gpd

def calculation_of_days(taz, commuting, emp_Education, emp_without_palestin_not_okev):
    taz['commuting']=gpd.sjoin(make_point(taz.reset_index())[['Taz_num','centroid']],commuting[['commuting', 'geometry']]).set_index('Taz_num')['commuting']/100

    taz['pop_emp_employed_out_of_jtmt_area']=taz['pop_emp_employed']*taz['commuting']

    emp_left_jtmt_area=taz['pop_emp_employed_out_of_jtmt_area'].sum().item()

    round(emp_left_jtmt_area,-3)

    emp_from_jtmt_area=taz['pop_emp_employed'].sum().item()-emp_left_jtmt_area

    # יוממות פנימה מחוץ למרחב
    emp_in_jtmt_area=emp_from_jtmt_area*1.07

    round(emp_in_jtmt_area,-3)

    # הפחחת עובדים ניידים
    emp_in_jtmt_area_without_mobile=emp_in_jtmt_area*0.95

    round(emp_in_jtmt_area_without_mobile,-3)

    emp_okev=emp_in_jtmt_area_without_mobile-emp_Education-emp_without_palestin_not_okev

    return taz