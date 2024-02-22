import pandas as pd

# הקבצים שאנחנו רוצים להשוות
df1 = pd.read_excel(r"C:\Users\dpere\Downloads\forecast_2020_230720.xlsx")
df2 = pd.read_excel(r"C:\Users\dpere\Documents\JTMT\forecast_by_version\V4\BASE_YEAR\forecast_2020_240222.xlsx")

# השוואה (יכול להיות שצריך לעשות מיון לעמודת האינדקס)
# מחזיר True or False
equal = df1.equals(df2)

# השוואה (יכול להיות שצריך לעשות מיון לעמודת האינדקס)
# מחזיר את הערכים השונים
compare= df1.compare(df2)

print(equal)
print(compare)
# df['TAZ'] = df1['TAZ']
# df['sector'] = df1['sector']

# compare.to_excel(r"C:\Users\dpere\Downloads\empty_compare.xlsx")

