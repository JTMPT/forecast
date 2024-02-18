from functions import split_index_by_taz

def division_into_traffic_zones(index,forecast):
    col=['add_uni_dorms',
    'add_old_age_home',
    'add_aprt',
    'Commerce_m2',
    'Business_m2',
    'Tourism_m2',
    'Public_m2',
    'Industry_m2',
    'emp_Public',
    'emp_Education',
    'emp_Commerce',
    'emp_Business',
    'emp_Industry',
    'emp_Tourism',
    'Classrooms',
    'add_uni_students']

    index=split_index_by_taz(index,forecast,0.05,col)
    return index
