def total_students(taz):
    taz=taz.fillna(0)

    col=['student_for_Control','student_chardi_not_gov','student_arab_not_gov','student_toddlers']

    taz['student']=taz[col].sum(axis=1)

    return taz