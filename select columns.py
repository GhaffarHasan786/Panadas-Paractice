import pandas as pd

data = {
    "name":["Ghaffar","Aman","Fizan","Mohid"],
    "age": [19,19,21,18],
    "city": ["Jhoke","Madodhas","Jhoke","Madodhas"],
    "class": ["bsit","bscs","bba","bscs"],
    "salary":[20000,70000,60000,80000]
} 

df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)
#select one columns
print("Salary(signle columns return series)")
columns = df["salary"]
print(columns)

# multiple columns selection

subset = df[["salary","name"]]
print("\nsubset with salary and name")
print(subset)