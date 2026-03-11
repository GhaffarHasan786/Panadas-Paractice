import pandas as pd
Data = {
    "Name":['Ghaffar','Ali','Ahmad','Zain','Kaif','Shiraz'],
    "Age":[22,23,45,17,18,16],
    "Salary":[20000,30000,40000,50000,60000,70000]
}

df = pd.DataFrame(Data)
print(df)

grouped = df.groupby(["Age"]["Salary"].sum())
print(grouped)