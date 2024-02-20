def export_for_control(taz):
    taz=taz.reset_index()

    pre_yeshiva_from_20_30_age=taz[['student_yeshiva_with_add_from_old']].sum().sum()/taz.query('jew==1')[['pop_20_just_from_aprt','pop_25_just_from_aprt']].sum().sum()

    taz.main_secto.unique()

    pre_uni_from_20_30_age=taz[['uni_students']].sum().sum()/taz.query('main_secto!="Palestinian"')[['pop_20_just_from_aprt','pop_25_just_from_aprt']].sum().sum()

    list(taz)

    return taz