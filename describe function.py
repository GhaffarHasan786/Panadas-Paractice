import pandas as pd

data = {
    "name":["Ghaffar","Aman","Fizan","Mohid"],
    "age": [19,19,21,18],
    "city": ["Jhoke","Madodhas","Jhoke","Madodhas"],
    "class": ["bsit","bscs","bba","bscs"],
    
}

df =pd.DataFrame(data)
print(df)
print("discriptive statistics")
print(df.describe)