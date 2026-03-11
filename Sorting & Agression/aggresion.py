"""
df["column_name"].mean()
df["column_name"].sum()
df["column_name"].min()
df["column_name"].max()
"""

import pandas as pd

Data = {
    "Name":['Ghaffar','Ali','Ahmad','Zain','Kaif','Shiraz'],
    "Age":[22,23,45,17,18,16],
    "Salary":[20000,30000,40000,50000,60000,70000]
}

df =pd.DataFrame(Data)
print(df)

avg_Salary =df['Salary'].mean()
print(avg_Salary) 