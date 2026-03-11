import pandas as pd


#load datasets
emp = pd.read_csv("employees.csv")
dept = pd.read_csv("Department.csv")
perf = pd.read_csv("Performance.csv")

#Merge data
merged = emp.merge(perf,on='Emp_ID').merge(dept,on='Department')

#calculate extra field
merged['Total_score'] = merged['Score'] + merged['Projects'] * 2

#Summary stats
Summar = merged.groupby('Department').agg({'Salary': ['mean','max'],'Score': 'mean',
                                  'project': 'sum'}).reset_index()

#save data

merged.to_csv("Company_analysis.csv", index=False)
merged.to_csv("Department_sammary.csv", index=False)

print("Company_Data Analysis complete!")
print("Summary")