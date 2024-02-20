def promotes_employed_education_for_students(taz):
    emp_from_uni_student_jeru=taz.query('Muni_Heb=="ירושלים" & jew==1 ')[['emp_from_uni_student']].sum().item()

    emp_from_Yeshiva_student_jeru=taz.query('Muni_Heb=="ירושלים" & jew==1 ')[['emp_from_Yeshiva_student']].sum().item()

    emp_for_student_jeru_jew=51.1*1000-emp_from_Yeshiva_student_jeru-emp_from_uni_student_jeru

    emp_education_per_student=round(taz.query('Muni_Heb=="ירושלים" & jew==1 ')[['student']].sum().item()/emp_for_student_jeru_jew,2) 

    taz['emp_from_student']=taz['student']/emp_education_per_student

    taz.loc[taz['main_secto']=="Palestinian",'emp_from_student']=0

    taz.query('Muni_Heb=="ירושלים"').groupby(by='jew')[['emp_from_student']].sum()

    taz['emp_Education']=taz['emp_from_student']+taz['emp_from_Yeshiva_student']+taz['emp_from_uni_student']

    return taz