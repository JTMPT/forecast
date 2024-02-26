import pandas as pd

# הקבצים שאנחנו רוצים להשוות
df1 = pd.read_excel(r"C:\Users\dpere\Downloads\taz_with_pop_info_230717.xlsx")
df2 = pd.read_excel(r"C:\Users\dpere\Documents\JTMT\forecast\create_forecast_basic\current\Intermediates\taz_with_pop_info.xlsx")

# df1.sort_values('Taz_num')
# השוואה (יכול להיות שצריך לעשות מיון לעמודת האינדקס)
# מחזיר True or False
equal = df1.equals(df2)
# equal = df1.sort_values('Taz_num').equals(df2.sort_values('Taz_num'))

# השוואה (יכול להיות שצריך לעשות מיון לעמודת האינדקס)
# מחזיר את הערכים השונים
compare= df1.compare(df2)
# compare = df1.sort_values('TAZ').compare(df2.sort_values('TAZ'))

# compare['Taz_num'] = df1['Taz_num']

print(equal)
print(compare)
# df['TAZ'] = df1['TAZ']
# df['sector'] = df1['sector']

# compare.to_excel(r"C:\Users\dpere\Downloads\taz_with_pop_info_230717_compare.xlsx")

