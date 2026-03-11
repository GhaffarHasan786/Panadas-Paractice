import pandas as pd

data = {
    "name":["Ghaffar","Aman","Fizan","Mohid"],
    "age": [19,20,21,18],
    "city": ["Jhoke","Madodhas","Jhoke","Madodhas"],
    "salary":[30000,50000,60000,70000]
}

df = pd.DataFrame(data)
print("sample dataframe")
print(df)

#single row filtring
print("filter one row")
high_salary = df[df["salary"]>50000]
print(high_salary)
#filter multiple row by condition or boolean indexing
print("Multiple row")
filtered = df[(df["salary"]>50000) & (df["age"]>18)]
print(filtered)