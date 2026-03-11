import pandas as pd

data = {
    "name":["Ghaffar","Aman","Fizan","Mohid"],
    "age": [19,19,21,18],
    "city": ["Jhoke","Madodhas","Jhoke","Madodhas"],
    "class": ["bsit","bscs","bba","bscs"],
    "salary": [20000,30000,40000,50000]
}

df = pd.DataFrame(data)
print(df)

#kisi specific column ya row ko update kerna ho to pher
# .loc(row index, column index) = new value method use krty ha

df.loc[1,'age'] = 20
print(df)

# ager ziyda row ya columns ko upddate krna ho to pher ye use krty ha 
# df ['coloum name'] = df['column name'] * value

df['salary'] = df['salary'] * 1.05
print(df)